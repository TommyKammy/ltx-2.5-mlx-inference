"""Regression tests for non-24fps pipeline timing propagation."""

from __future__ import annotations

from types import SimpleNamespace

import mlx.core as mx
import pytest


class _StopAfterProbeError(RuntimeError):
    """Stop a pipeline once the timing call under test has been observed."""


class _FakeKeyframeConditioner:
    def __call__(self, _callback, *, free_after):
        del free_after
        token = mx.zeros((1, 1, 128), dtype=mx.bfloat16)
        return [token], [token]


class _FakeStage2ImageConditioner:
    def __init__(self, latent):
        self._latent = latent

    def __call__(self, _callback, *, free_after):
        del free_after
        return self._latent, []


def _text_embeddings():
    video = mx.zeros((1, 2, 32), dtype=mx.bfloat16)
    audio = mx.zeros((1, 2, 16), dtype=mx.bfloat16)
    return video, audio, video, audio


def test_keyframe_audio_token_count_uses_requested_frame_rate(tmp_path, monkeypatch):
    """A 30fps interpolation must not size audio using the 24fps default."""
    import ltx_pipelines_mlx.keyframe_interpolation as module

    model_dir = tmp_path / "model"
    model_dir.mkdir()
    (model_dir / "transformer-dev.safetensors").touch()
    pipe = module.KeyframeInterpolationPipeline(
        model_dir=str(model_dir),
        low_memory=False,
        dev_transformer="transformer-dev.safetensors",
    )
    pipe.image_conditioner = _FakeKeyframeConditioner()
    pipe.dit = object()
    pipe.upsampler = object()
    monkeypatch.setattr(pipe, "_encode_text_with_negative", lambda _prompt: _text_embeddings())

    observed = {}

    def probe_audio_token_count(num_frames, frame_rate=24.0):
        observed.update(num_frames=num_frames, frame_rate=frame_rate)
        raise _StopAfterProbeError

    monkeypatch.setattr(module, "compute_audio_token_count", probe_audio_token_count)

    with pytest.raises(_StopAfterProbeError):
        pipe.interpolate(
            prompt="test",
            keyframe_images=["unused.png"],
            keyframe_indices=[0],
            height=64,
            width=64,
            num_frames=121,
            frame_rate=30.0,
            cfg_scale=2.0,
        )

    assert observed == {"num_frames": 121, "frame_rate": 30.0}


def test_a2v_video_positions_use_requested_frame_rate_in_both_stages(tmp_path, monkeypatch):
    """Both A2V RoPE grids must use the output fps, not the 24fps default."""
    import ltx_pipelines_mlx.a2vid_two_stage as module

    model_dir = tmp_path / "model"
    model_dir.mkdir()
    (model_dir / "transformer-dev.safetensors").touch()
    pipe = module.A2VidPipelineTwoStage(model_dir=str(model_dir), low_memory=False)
    pipe.audio_encoder = object()
    pipe.audio_processor = object()
    pipe.dit = object()
    pipe.upsampler = object()
    monkeypatch.setattr(pipe, "_load_audio_encoder", lambda: None)
    monkeypatch.setattr(pipe, "_encode_text_with_negative", lambda _prompt: _text_embeddings())
    monkeypatch.setattr(pipe, "_fuse_distilled_lora", lambda _dit: None)
    monkeypatch.setattr(
        pipe,
        "_denoise_stage1",
        lambda **kwargs: SimpleNamespace(
            video_latent=kwargs["video_state"].latent,
            audio_latent=kwargs["audio_state"].latent,
        ),
    )

    audio_data = SimpleNamespace(
        waveform=mx.zeros((1, 2, 16000), dtype=mx.float32),
        sample_rate=16000,
    )
    monkeypatch.setattr(module, "load_audio", lambda *_args, **_kwargs: audio_data)
    monkeypatch.setattr(
        module,
        "encode_audio",
        lambda *_args, **_kwargs: mx.zeros((1, 8, 32, 16), dtype=mx.bfloat16),
    )

    # num_frames=9 at 64x64 gives an F=2, H_half=W_half=1 latent.
    pipe.image_conditioner = _FakeStage2ImageConditioner(mx.zeros((1, 128, 2, 2, 2), dtype=mx.bfloat16))

    real_compute_video_positions = module.compute_video_positions
    observed_frame_rates = []

    def probe_video_positions(num_frames, height, width, frame_rate=24.0):
        observed_frame_rates.append(frame_rate)
        if len(observed_frame_rates) == 2:
            raise _StopAfterProbeError
        return real_compute_video_positions(num_frames, height, width, frame_rate=frame_rate)

    monkeypatch.setattr(module, "compute_video_positions", probe_video_positions)

    with pytest.raises(_StopAfterProbeError):
        pipe.generate_and_save(
            prompt="test",
            output_path="unused.mp4",
            audio_path="unused.wav",
            height=64,
            width=64,
            num_frames=9,
            frame_rate=30.0,
            stage1_steps=1,
        )

    assert observed_frame_rates == [30.0, 30.0]
