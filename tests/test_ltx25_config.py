import mlx.core as mx

from ltx_core_mlx.model.transformer.model import LTXModel, LTXModelConfig


def _tiny_config(**kwargs) -> LTXModelConfig:
    return LTXModelConfig(
        num_layers=1,
        video_dim=16,
        audio_dim=8,
        video_num_heads=2,
        audio_num_heads=2,
        video_head_dim=8,
        audio_head_dim=4,
        av_cross_num_heads=2,
        av_cross_head_dim=4,
        video_patch_channels=4,
        audio_patch_channels=4,
        ff_mult=2.0,
        **kwargs,
    )


def test_ltx25_config_reads_bias_and_keyframe_flags():
    config = LTXModelConfig.from_checkpoint_config(
        {
            "transformer": {
                "ff_bias": False,
                "audio_ff_bias": True,
                "use_keyframes_abs_pos_embedding": True,
            }
        }
    )

    assert config.ff_bias is False
    assert config.audio_ff_bias is True
    assert config.use_keyframes_abs_pos_embedding is True


def test_ltx25_video_ff_has_no_bias_but_audio_ff_does():
    model = LTXModel(_tiny_config(ff_bias=False, audio_ff_bias=True))
    block = model.transformer_blocks[0]

    assert "bias" not in block.ff.proj_in
    assert "bias" not in block.ff.proj_out
    assert "bias" in block.audio_ff.proj_in
    assert "bias" in block.audio_ff.proj_out


def test_keyframe_embedding_only_changes_marked_tokens():
    model = LTXModel(_tiny_config(use_keyframes_abs_pos_embedding=True))
    model.keyframes_abs_pos_embedding = mx.ones((1, 16)) * 3
    hidden = mx.zeros((1, 3, 16))
    mask = mx.array([[[0], [1], [0]]])

    result = model._apply_keyframes_abs_pos_embedding(hidden, mask)
    mx.eval(result)

    assert mx.array_equal(result[:, 0], hidden[:, 0])
    assert mx.array_equal(result[:, 1], mx.ones((1, 16)) * 3)
    assert mx.array_equal(result[:, 2], hidden[:, 2])


def test_ltx23_defaults_keep_biases_and_no_keyframe_parameter():
    model = LTXModel(_tiny_config())
    block = model.transformer_blocks[0]

    assert "bias" in block.ff.proj_in
    assert "bias" in block.ff.proj_out
    assert not hasattr(model, "keyframes_abs_pos_embedding")
