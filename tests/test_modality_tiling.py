"""Unit tests for VideoModalityTiler."""

from __future__ import annotations

import mlx.core as mx

from ltx_core_mlx.components.modality_tiling import VideoModalityTiler
from ltx_core_mlx.model.transformer.modality import Modality
from ltx_core_mlx.model.video_vae.tiling import DimensionTilingConfig, TileCountConfig


def _make_modality(latent: mx.array, positions: mx.array, attention_mask: mx.array | None = None) -> Modality:
    """Build a minimal Modality for tiler tests (timesteps, sigma, context filled with zeros)."""
    B, T = latent.shape[0], latent.shape[1]
    return Modality(
        latent=latent,
        sigma=mx.zeros((B,)),
        timesteps=mx.zeros((B, T)),
        positions=positions,
        context=mx.zeros((B, 0, 0), dtype=latent.dtype),
        enabled=True,
        context_mask=None,
        attention_mask=attention_mask,
    )


def _make_positions(F: int, H: int, W: int) -> mx.array:  # noqa: N803
    """(1, F*H*W, 3) point coords matching the (f, h, w) grid."""
    f_idx = mx.arange(F)[:, None, None].astype(mx.float32) * mx.ones((F, H, W), dtype=mx.float32)
    h_idx = mx.arange(H)[None, :, None].astype(mx.float32) * mx.ones((F, H, W), dtype=mx.float32)
    w_idx = mx.arange(W)[None, None, :].astype(mx.float32) * mx.ones((F, H, W), dtype=mx.float32)
    pos = mx.stack([f_idx, h_idx, w_idx], axis=-1).reshape(1, F * H * W, 3)
    return pos


class TestVideoModalityTiler:
    def test_tile_count_with_overlap(self):
        tiling = TileCountConfig(
            frames=DimensionTilingConfig(num_tiles=2, overlap=1),
            height=DimensionTilingConfig(num_tiles=2, overlap=2),
            width=DimensionTilingConfig(num_tiles=1),
        )
        tiler = VideoModalityTiler(tiling, latent_shape=(4, 8, 8))
        # 2 (frames) * 2 (height) * 1 (width) = 4 tiles
        assert len(tiler.tiles) == 4

    def test_single_tile_round_trip(self):
        """1x1x1 tile: blend(tile(latent)) must equal latent itself."""
        F, H, W, D = 4, 6, 8, 16
        T = F * H * W
        tiling = TileCountConfig()  # 1 tile per dim
        tiler = VideoModalityTiler(tiling, latent_shape=(F, H, W))
        assert len(tiler.tiles) == 1

        latent = mx.random.normal((1, T, D))
        positions = _make_positions(F, H, W)
        modality = _make_modality(latent, positions)
        tile = tiler.tiles[0]

        tiled, ctx = tiler.tile_modality(modality, tile, normalize_positions=False)
        assert tiled.latent.shape == latent.shape

        out = tiler.blend(tiled.latent, tile, ctx)
        mx.eval(latent, out)
        assert mx.allclose(latent, out, atol=1e-6).item()

    def test_multi_tile_no_overlap_round_trip(self):
        """Tiling with no overlap and trapezoidal mask = 1.0 everywhere
        should reconstruct identity when blend masks are uniform."""
        F, H, W, D = 4, 8, 8, 8
        T = F * H * W
        tiling = TileCountConfig(
            frames=DimensionTilingConfig(num_tiles=2, overlap=0),
            height=DimensionTilingConfig(num_tiles=2, overlap=0),
        )
        tiler = VideoModalityTiler(tiling, latent_shape=(F, H, W))
        assert len(tiler.tiles) == 4

        latent = mx.random.normal((1, T, D))
        positions = _make_positions(F, H, W)
        modality = _make_modality(latent, positions)

        output = mx.zeros_like(latent)
        for t in tiler.tiles:
            tiled, ctx = tiler.tile_modality(modality, t, normalize_positions=False)
            output = tiler.blend(tiled.latent, t, ctx, output=output)
        mx.eval(latent, output)
        # No overlap → blend masks are all 1.0, sum gives back identity.
        assert mx.allclose(latent, output, atol=1e-6).item()

    def test_multi_tile_with_overlap_blend_weights_sum_to_one(self):
        """With overlap, blended output must equal the original where
        per-pixel blend weights across all tiles sum to 1."""
        F, H, W, D = 4, 8, 8, 4
        T = F * H * W
        tiling = TileCountConfig(
            frames=DimensionTilingConfig(num_tiles=1),
            height=DimensionTilingConfig(num_tiles=2, overlap=2),
        )
        tiler = VideoModalityTiler(tiling, latent_shape=(F, H, W))

        latent = mx.random.normal((1, T, D))
        positions = _make_positions(F, H, W)
        modality = _make_modality(latent, positions)

        output = mx.zeros_like(latent)
        for t in tiler.tiles:
            tiled, ctx = tiler.tile_modality(modality, t, normalize_positions=False)
            output = tiler.blend(tiled.latent, t, ctx, output=output)
        mx.eval(latent, output)
        # Trapezoidal masks sum to 1 across the overlap → identity.
        assert mx.allclose(latent, output, atol=1e-5).item()

    def test_position_normalization(self):
        """When normalize_positions=True, the tile's generated tokens
        should start at coord zero on every axis."""
        F, H, W = 4, 8, 8
        tiling = TileCountConfig(
            frames=DimensionTilingConfig(num_tiles=2, overlap=0),
            height=DimensionTilingConfig(num_tiles=2, overlap=0),
        )
        tiler = VideoModalityTiler(tiling, latent_shape=(F, H, W))

        latent = mx.zeros((1, F * H * W, 4))
        positions = _make_positions(F, H, W)
        modality = _make_modality(latent, positions)

        for t in tiler.tiles:
            tiled, _ = tiler.tile_modality(modality, t, normalize_positions=True)
            tiled_pos = tiled.positions
            num_tile_gen = (
                (t.in_coords[0].stop - t.in_coords[0].start)
                * (t.in_coords[1].stop - t.in_coords[1].start)
                * (t.in_coords[2].stop - t.in_coords[2].start)
            )
            mx.eval(tiled_pos)
            gen_pos = tiled_pos[:, :num_tile_gen, :]
            assert float(gen_pos.min().item()) == 0.0

    def test_attention_mask_subset(self):
        """When attention_mask is given, the tiled mask is the kept
        rows x kept cols submatrix."""
        F, H, W = 2, 4, 4
        T = F * H * W
        tiling = TileCountConfig(height=DimensionTilingConfig(num_tiles=2, overlap=0))
        tiler = VideoModalityTiler(tiling, latent_shape=(F, H, W))

        latent = mx.zeros((1, T, 4))
        positions = _make_positions(F, H, W)
        full_mask = mx.random.normal((1, T, T))
        modality = _make_modality(latent, positions, attention_mask=full_mask)

        tile = tiler.tiles[0]
        tiled, _ = tiler.tile_modality(modality, tile)
        assert tiled.attention_mask is not None
        assert tiled.attention_mask.shape == (1, tiled.latent.shape[1], tiled.latent.shape[1])

    def test_cond_tokens_kept_by_overlap(self):
        """Conditioning tokens whose point coords fall in the tile range
        are kept; others are dropped."""
        F, H, W, D = 2, 4, 4, 4
        T_gen = F * H * W
        # Two cond tokens: one in each height-half of the grid.
        cond_pos = mx.array([[[0.0, 0.0, 0.0], [0.0, 3.0, 0.0]]])  # (1, 2, 3)
        positions = mx.concatenate([_make_positions(F, H, W), cond_pos], axis=1)
        latent = mx.random.normal((1, T_gen + 2, D))

        tiling = TileCountConfig(height=DimensionTilingConfig(num_tiles=2, overlap=0))
        tiler = VideoModalityTiler(tiling, latent_shape=(F, H, W))
        modality = _make_modality(latent, positions)

        # First tile covers h=[0,2): only the first cond (h=0) is kept.
        # Second tile covers h=[2,4): only the second cond (h=3) is kept.
        for t in tiler.tiles:
            _, ctx = tiler.tile_modality(modality, t)
            cond_keep = ctx.keep_mask[T_gen:]
            mx.eval(cond_keep)
            assert int(cond_keep.sum().item()) == 1


class TestTiledLTXModel:
    @staticmethod
    def _tiny_model_config():
        from ltx_core_mlx.model.transformer.model import LTXModelConfig

        return LTXModelConfig(
            num_layers=2,
            video_dim=32,
            audio_dim=16,
            video_num_heads=4,
            audio_num_heads=4,
            video_head_dim=8,
            audio_head_dim=4,
            av_cross_num_heads=4,
            av_cross_head_dim=4,
            video_patch_channels=8,
            audio_patch_channels=8,
            ff_mult=2.0,
            timestep_embedding_dim=32,
        )

    def test_single_tile_matches_baseline(self):
        """Wrapping a model in TiledLTXModel with a 1x1x1 tiler must
        produce the same output as the bare model (single tile == identity)."""
        from ltx_core_mlx.components.modality_tiling import TiledLTXModel
        from ltx_core_mlx.model.transformer.model import LTXModel

        cfg = self._tiny_model_config()
        mx.random.seed(7)
        model = LTXModel(cfg)
        mx.eval(model.parameters())

        # Pixel-space: F=1, H=1, W=16 → 16 tokens (single time/height row).
        F, H, W = 1, 1, 16
        Nv, Na, Nt = F * H * W, 4, 4
        common = dict(
            video_latent=mx.random.normal((1, Nv, cfg.video_patch_channels)).astype(mx.bfloat16),
            audio_latent=mx.random.normal((1, Na, cfg.audio_patch_channels)).astype(mx.bfloat16),
            timestep=mx.array([0.5]),
            video_text_embeds=mx.random.normal((1, Nt, cfg.video_dim)).astype(mx.bfloat16),
            audio_text_embeds=mx.random.normal((1, Nt, cfg.audio_dim)).astype(mx.bfloat16),
            video_positions=_make_positions(F, H, W),
            audio_positions=mx.zeros((1, Na, 1)),
        )

        baseline_v, baseline_a = model(**common)

        tiler = VideoModalityTiler(TileCountConfig(), latent_shape=(F, H, W))
        wrapped = TiledLTXModel(model, tiler)
        wrapped_v, wrapped_a = wrapped(**common)

        mx.eval(baseline_v, baseline_a, wrapped_v, wrapped_a)
        assert mx.allclose(baseline_v, wrapped_v, atol=1e-5, rtol=1e-5).item()
        assert mx.allclose(baseline_a, wrapped_a, atol=1e-5, rtol=1e-5).item()

    def test_multi_tile_slices_video_keyframes_mask(self):
        """The LTX-2.5 keyframe marker must follow the tile token subset.

        Regression: the full ``(B, Nv, 1)`` mask was forwarded with a tiled
        ``(B, tile_Nv, D)`` latent, causing a broadcast error inside
        ``LTXModel._apply_keyframes_abs_pos_embedding``.
        """
        from ltx_core_mlx.components.modality_tiling import TiledLTXModel
        from ltx_core_mlx.model.transformer.model import LTXModel

        cfg = self._tiny_model_config()
        cfg.use_keyframes_abs_pos_embedding = True
        mx.random.seed(11)
        model = LTXModel(cfg)
        mx.eval(model.parameters())

        F, H, W = 1, 1, 4
        Nv, Na, Nt = F * H * W, 2, 2
        common = dict(
            video_latent=mx.random.normal((1, Nv, cfg.video_patch_channels)).astype(mx.bfloat16),
            audio_latent=mx.random.normal((1, Na, cfg.audio_patch_channels)).astype(mx.bfloat16),
            timestep=mx.array([0.5]),
            video_text_embeds=mx.random.normal((1, Nt, cfg.video_dim)).astype(mx.bfloat16),
            audio_text_embeds=mx.random.normal((1, Nt, cfg.audio_dim)).astype(mx.bfloat16),
            video_positions=_make_positions(F, H, W),
            audio_positions=mx.zeros((1, Na, 1)),
            video_keyframes_mask=mx.array([[[1.0], [0.0], [0.0], [1.0]]]),
        )

        tiler = VideoModalityTiler(
            TileCountConfig(width=DimensionTilingConfig(num_tiles=2, overlap=0)),
            latent_shape=(F, H, W),
        )
        wrapped = TiledLTXModel(model, tiler)

        video_out, audio_out = wrapped(**common)
        mx.eval(video_out, audio_out)
        assert video_out.shape == common["video_latent"].shape
        assert audio_out.shape == common["audio_latent"].shape
