import mlx.core as mx

from ltx_pipelines_mlx.utils.helpers import create_noised_state


def test_create_noised_video_state_marks_only_causal_first_frame():
    state = create_noised_state(
        base_shape=(1, 8, 4),
        conditionings=[],
        spatial_dims=(4, 1, 2),
        positions=mx.zeros((1, 8, 3)),
        seed=42,
        mark_first_frame=True,
    )

    assert state.keyframes_mask is not None
    assert state.keyframes_mask.shape == (1, 8, 1)
    assert mx.all(state.keyframes_mask[:, :2] == 1).item()
    assert mx.all(state.keyframes_mask[:, 2:] == 0).item()


def test_create_noised_audio_state_does_not_create_keyframes_mask():
    state = create_noised_state(
        base_shape=(1, 6, 4),
        conditionings=[],
        spatial_dims=(4, 1, 2),
        positions=mx.zeros((1, 6, 1)),
        seed=42,
    )

    assert state.keyframes_mask is None
