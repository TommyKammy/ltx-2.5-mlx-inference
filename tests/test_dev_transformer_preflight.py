"""Capability preflight tests for pipelines that require dev weights."""

from __future__ import annotations

from collections.abc import Callable

import mlx.core as mx
import pytest

from ltx_pipelines_mlx.a2vid_two_stage import A2VidPipelineTwoStage
from ltx_pipelines_mlx.distilled import DistilledPipeline
from ltx_pipelines_mlx.keyframe_interpolation import KeyframeInterpolationPipeline
from ltx_pipelines_mlx.retake import RetakePipeline
from ltx_pipelines_mlx.ti2vid_one_stage import TI2VidOneStagePipeline
from ltx_pipelines_mlx.ti2vid_two_stages import TI2VidTwoStagesPipeline
from ltx_pipelines_mlx.ti2vid_two_stages_hq import TI2VidTwoStagesHQPipeline

PipelineFactory = Callable[[str], object]
PipelineCall = Callable[[object], object]


def _default_factory(cls):
    return lambda model_dir: cls(model_dir=model_dir, low_memory=True)


def _keyframe_factory(model_dir: str):
    return KeyframeInterpolationPipeline(
        model_dir=model_dir,
        low_memory=True,
        dev_transformer="transformer-dev.safetensors",
    )


_SOURCE_VIDEO = mx.zeros((1, 128, 1, 1, 1), dtype=mx.bfloat16)
_SOURCE_AUDIO = mx.zeros((1, 8, 1, 16), dtype=mx.bfloat16)


@pytest.mark.parametrize(
    ("factory", "invoke"),
    [
        (
            _default_factory(TI2VidOneStagePipeline),
            lambda pipe: pipe.generate_one_stage_dev(prompt="test", frame_rate=24.0),
        ),
        (
            _default_factory(TI2VidTwoStagesPipeline),
            lambda pipe: pipe.generate_two_stage(prompt="test", frame_rate=24.0),
        ),
        (
            _default_factory(TI2VidTwoStagesHQPipeline),
            lambda pipe: pipe.generate_two_stage(prompt="test", frame_rate=24.0),
        ),
        (
            _default_factory(A2VidPipelineTwoStage),
            lambda pipe: pipe.generate_and_save(prompt="test", output_path="out.mp4", frame_rate=24.0),
        ),
        (
            _keyframe_factory,
            lambda pipe: pipe.interpolate(
                prompt="test",
                keyframe_images=[],
                keyframe_indices=[],
                frame_rate=24.0,
            ),
        ),
        (
            _default_factory(RetakePipeline),
            lambda pipe: pipe.retake_from_video(
                prompt="test",
                video_path="missing.mp4",
                start_frame=0,
                end_frame=1,
            ),
        ),
        (
            _default_factory(RetakePipeline),
            lambda pipe: pipe.extend_from_video(
                prompt="test",
                video_path="missing.mp4",
                extend_frames=1,
            ),
        ),
        (
            _default_factory(RetakePipeline),
            lambda pipe: pipe.retake(
                prompt="test",
                source_video_latent=_SOURCE_VIDEO,
                source_audio_latent=_SOURCE_AUDIO,
                start_frame=0,
                end_frame=1,
                frame_rate=24.0,
            ),
        ),
        (
            _default_factory(RetakePipeline),
            lambda pipe: pipe.extend(
                prompt="test",
                source_video_latent=_SOURCE_VIDEO,
                source_audio_latent=_SOURCE_AUDIO,
                extend_frames=1,
                frame_rate=24.0,
            ),
        ),
    ],
    ids=[
        "one-stage",
        "two-stage",
        "hq-two-stage",
        "a2v",
        "keyframe",
        "retake-from-video",
        "extend-from-video",
        "retake-latents",
        "extend-latents",
    ],
)
def test_distilled_only_model_fails_before_preprocessing(tmp_path, factory: PipelineFactory, invoke: PipelineCall):
    """Every dev-only public entry must reject distilled-only weights immediately."""
    model_dir = tmp_path / "distilled-only"
    model_dir.mkdir()
    (model_dir / "transformer-distilled.safetensors").touch()
    pipe = factory(str(model_dir))

    with pytest.raises(FileNotFoundError) as exc_info:
        invoke(pipe)

    message = str(exc_info.value)
    assert "requires a dev (non-distilled) transformer" in message
    assert "Detected distilled-only weights" in message
    assert "generate --distilled" in message


def test_dev_preflight_accepts_existing_configured_weight(tmp_path):
    """The capability check must preserve dev-capable LTX-2.3 directories."""
    model_dir = tmp_path / "dev-model"
    model_dir.mkdir()
    expected = model_dir / "transformer-dev.safetensors"
    expected.touch()
    pipe = TI2VidTwoStagesPipeline(model_dir=str(model_dir), low_memory=True)

    assert pipe._require_dev_transformer() == expected


def test_dev_preflight_rejects_directory_with_checkpoint_name(tmp_path):
    """Only a regular checkpoint file may satisfy the dev capability check."""
    model_dir = tmp_path / "invalid-dev-model"
    model_dir.mkdir()
    (model_dir / "transformer-dev.safetensors").mkdir()
    pipe = TI2VidTwoStagesPipeline(model_dir=str(model_dir), low_memory=True)

    with pytest.raises(FileNotFoundError, match="Dev transformer not found"):
        pipe._require_dev_transformer()


def test_distilled_pipeline_does_not_require_dev_weights(tmp_path, monkeypatch):
    """The supported ``generate --distilled`` path must bypass the dev preflight."""
    model_dir = tmp_path / "distilled-only"
    model_dir.mkdir()
    (model_dir / "transformer-distilled.safetensors").touch()
    pipe = DistilledPipeline(model_dir=str(model_dir), low_memory=True)

    class _ReachedDistilledPathError(RuntimeError):
        pass

    def fail_if_dev_preflight_runs():
        raise AssertionError("distilled path invoked dev preflight")

    def stop_at_distilled_text_encoder():
        raise _ReachedDistilledPathError

    monkeypatch.setattr(pipe, "_require_dev_transformer", fail_if_dev_preflight_runs)
    monkeypatch.setattr(pipe, "_load_text_encoder", stop_at_distilled_text_encoder)

    with pytest.raises(_ReachedDistilledPathError):
        pipe.generate_two_stage(prompt="test", frame_rate=24.0)
