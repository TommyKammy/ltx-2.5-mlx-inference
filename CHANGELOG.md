# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

While the project is pre-1.0 (`0.x.y`), the `0.y` segment serves as the major
version: breaking changes bump `y`, additive changes bump `z`. See
[`docs/PIPELINE_MATURITY.md`](docs/PIPELINE_MATURITY.md) for per-pipeline
stability guarantees.

## [0.15.0](https://github.com/TommyKammy/ltx-2.5-mlx-inference/compare/v0.14.19...v0.15.0) (2026-08-14)


### ⚠ BREAKING CHANGES

* ultra-strict iso on frame_rate kwarg — mandatory everywhere → 0.14.0 ([#15](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/15))
* remove standalone upscale pipeline (no upstream counterpart) → 0.13.0 ([#12](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/12))
* rename pipeline classes to match upstream verbatim (BREAKING)
* remove ImageToVideoPipeline (legacy, no upstream equivalent) (BREAKING)
* ti2vid_one_stage.py now hosts TI2VidOneStagePipeline (file iso)
* **retake:** fold extend into RetakePipeline (file iso with upstream)
* **cli:** rename --hq → --two-stages-hq (matches upstream class name)
* **a2v:** remove a2v --hq (not in upstream) (BREAKING)
* **cli:** require explicit pipeline mode for generate (BREAKING)

### Features

* add --enable-teacache / --teacache-thresh to generate CLI ([10fed63](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/10fed6382a2d576d033faaac0fbf0d1214924eda))
* add --hq flag to calibrate_teacache for res_2s calibration ([ae3cb4b](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ae3cb4b51c55e1db6067ce8f71fdcbf07a88295e))
* add bump_version.py for monorepo version bumps ([5da18ee](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/5da18ee8cb6e61ae2315f0f0a1b19928deae2238))
* add compute_video_normed_sa helper for TeaCache gate signal ([63853a3](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/63853a3e2fbbf9bffbfd1acc3b19e4bcf57744c7))
* add enable_teacache flag to TwoStagePipeline.generate_two_stage ([39012b2](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/39012b2239f1eeb0bda3b162e46e290c9c8ea3de))
* add generate_changelog.py for release notes from git log ([5e3f1d6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/5e3f1d6350f86319b7d4d315ff5c6092e7253163))
* add GitHub Actions release workflow (tag-driven) ([132e253](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/132e253a1d51a42313aa53ad26edea7950a854d5))
* add HQ mode (res_2s sampler) to a2v pipeline ([95290cd](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/95290cd780f689f31d320dbced9ce499452f6f8c))
* add I2V conditioning support to a2v pipeline ([f7d9a45](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f7d9a45fc81c87287f969dc25e489936067daf05))
* add IC-LoRA pipeline with CLI support for official Lightricks LoRAs ([e7d4b05](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/e7d4b05250262d3ee35b81341bfe8124b2e41d44))
* add keyframe divergence test matrix runner ([3c7d55f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3c7d55f3b4861eea003982cd2adc6e801a1c3cb5))
* add keyframe test fixture generator (5 diverse pairs) ([49a642d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/49a642d0bd4b6b5e5d1aa85a93c6ae9dcf1c549a))
* add LTX-2.5 MLX inference support ([aa86e81](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/aa86e819fa5ad497151c64286b2e8fbdb4e5a624))
* add LTXModel.compute_gate_signal for TeaCache decisions ([018bea2](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/018bea2462f60bc39c8ed6e7bef2826c27687cbb))
* add robust polyfit analysis script for TeaCache calibration ([fa3338d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/fa3338d755b6795c9909218f217b4a2cdf1edd97))
* add tap and block_stack_override hooks to LTXModel and X0Model ([360e696](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/360e6960af06ac9cf0f86debefa669249b22a8ce))
* add tap kwarg to guided_denoise_loop for TeaCache calibration ([28ad6e6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/28ad6e64b1e563eb12033284920e139bd3046366))
* add TeaCache calibration script for LTX-2 stage 1 ([ab53c97](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ab53c97bb1a8f5d7d1e650a626c0eeb7b7dda08f))
* add teacache kwarg to guided_denoise_loop with per-pass dict cache ([a2efc9c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/a2efc9c581469532d2574c9b199ff6f33380e963))
* add training pipeline (preprocess, train, LoRA generation) ([c2e0ea7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/c2e0ea7ee807ca1014022cd9a5a87d61f40e68c5))
* add validate_versions.py for release-time coherence check ([0c63d2f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/0c63d2ffff82896529f314efad559428fa84a0e5))
* audio LoRA training — preprocessing, slicer, and gradient checkpointing ([#43](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/43)) ([89dd935](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/89dd935ec3fc7fa411ff927c9765a577ea3f67e4))
* **blocks:** add AudioConditioner block, fully delegate loaders ([5560fb3](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/5560fb3471489e4ba0b59846312b3d136af62dbf))
* **blocks:** add composition API in utils/blocks.py (mirrors upstream) ([0cdd8ca](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/0cdd8caa3de90e070c1506b436ebb6e51f03bf6a))
* **cli:** phase markers on silent pipeline stages (closes [#5](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/5)) → 0.13.1 ([#13](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/13)) ([c04eee7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/c04eee72a3b0ab7093d47cdcc448ea1bb95bc0a5))
* **cli:** require explicit pipeline mode for generate (BREAKING) ([715a82c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/715a82cd453593106dcb88275c0dc369d1e3738b))
* complete MLX port of LTX-2 for Apple Silicon ([dcd639e](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/dcd639e77b25a46c2b562463ed4c6f9cf16dccf5))
* dev model + distilled LoRA keyframe interpolation matching reference ([86f37a9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/86f37a95f2ff43145413c4b2fcf56c8165438b92))
* **dev-one-stage:** port DevOneStagePipeline + generate --dev flag (v0.7.0) ([5a26b4c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/5a26b4c83265fe16886e5a3e9024b9f1135c535c))
* **distilled:** port DistilledPipeline + generate --distilled flag (v0.6.0) ([a019365](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/a019365308d553378c47518c2da47f2e80adedf1))
* drop calibrated LTX-2 TeaCache coefficients (deg 1, thresh 0.5) ([245fd5f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/245fd5f8eea99d08c3b8fcdd0f6a27fddb3cf04a))
* drop calibrated TeaCache coefficients for LTX-2 stage 1 ([3b830a7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3b830a7e6733e1e977e1922199f1c7b9d1aec38f))
* drop res_2s-specific TeaCache coefficients for HQ pipeline ([6a6b5cd](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/6a6b5cd0b349939511c200c4abd28dd8348c07f0))
* enable --lora on --low-ram flow ([#30](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/30)) ([7e053b9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/7e053b98d17e04eb566504fae7589681047fef53))
* **hdr:** port LogC3 utilities for HDR IC-LoRA pipeline (phase 1) ([603fe44](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/603fe4427a519fd925c3e7ab15cb50d6654402a4))
* **hdr:** wire HDR LoRA detection + linear-HDR output into ICLoraPipeline (phase 2) ([1df766d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1df766d345bdfe9cd8277798ca9f8d69af72057b))
* **i2v:** multi-image conditioning + fix HQ stage1_steps default ([e9e0e8a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/e9e0e8aad95615b56223d4566a6403ca60f91310))
* **i2v:** propagate multi-image conditioning to all I2V pipelines ([f96bb59](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f96bb595ed305924643dd018868a6d3cdf1e97e9))
* ic-lora --upsample-only + control-aware --refine-steps ([#68](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/68)) ([16580db](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/16580db376888316803505d5e163048cc902ec93))
* **image:** apply H.264 CRF round-trip in prepare_image_for_encoding (upstream-iso) ([30152ed](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/30152ed035965daf714b182aaaaccfc9413186b6))
* **keyframe:** expose --start-strength / --end-strength on CLI ([10cc221](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/10cc221df128d15bd76a8b37e699eb8129df549f))
* **lipdub:** LipDub experimental pipeline from PR [#212](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/212) → 0.12.1 ([#10](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/10)) ([f9f9bcd](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f9f9bcd86d54b07c7380af9e487d68fce917025e))
* **loader:** add BlockStreamer + block_provider hook for low-RAM inference ([be93037](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/be93037f325de0a5095d8f11a12439aff0469594))
* **loader:** add eviction + auto-reload to BlockStreamer for constant-RAM streaming ([38000f4](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/38000f4e4bc39c37efd41b625d00cb0283813760))
* **media_io:** port ltx_pipelines.utils.media_io 1:1 upstream-iso ([16b9b6a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/16b9b6ab3349c2f93160897e09b502da8629e50a))
* **modality-tiling:** pipeline integration via --tile-frames / --tile-spatial (phase 3) ([1d4f116](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1d4f1160ee0160f64f2bff99f144538cc5933e29))
* **modality-tiling:** VideoModalityTiler helper (phase 2) ([f1952d7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f1952d7a81a145b4dc457b1c5818c3c21e5d3b5e))
* multi-anchor I2V for --one-stage and --distilled ([#45](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/45)) ([bd2217a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/bd2217a420aaf2aaa2fc6f97ebad2842ee1c3fb0))
* **pipeline:** wire block streaming into one-stage T2V/I2V via --low-ram ([b1e4cd9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b1e4cd9786acc446f63109a8740e6f6b69244006))
* Prompt Relay temporal prompt gating ([#61](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/61)) ([b9aa475](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b9aa475ac90ebc2bbfe1dffd97ee6bdee5a823f5))
* remove standalone upscale pipeline (no upstream counterpart) → 0.13.0 ([#12](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/12)) ([e17c2af](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/e17c2af9a63bebb3d0675d1f786667a543539255))
* save raw deltas in calibration JSON for offline re-fit ([7cb2ccd](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/7cb2ccd8e52e57171fed95d111b0694667ffd3e7))
* **streaming:** bind-time LoRA fusion → ic-lora --low-ram + custom distilled LoRA strength ([c1e2a1c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/c1e2a1c48b8066a1a121194ff72d2193f46eeadd))
* **streaming:** extend --low-ram to --two-stage / --hq / a2v / keyframe ([e3ff713](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/e3ff713a3bb7bcc99738c1c75ef0a18749b86a4c))
* **streaming:** mx.compile + per-block sync — actual ~75% transformer RAM savings ([3643fbd](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3643fbdb955cdb8ee807a0ef281fcf25b59a092a))
* **streaming:** set Metal cache_limit=0 to enable real eviction in --low-ram ([33b6f5b](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/33b6f5bd7761c4b0e1d8607bc8dda68582c3c5aa))
* **tiling:** token-grid primitives for modality tiling ([faf5f14](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/faf5f149ffab4927487969c3d9fface8612f51ca))
* ultra-strict iso on frame_rate kwarg — mandatory everywhere → 0.14.0 ([#15](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/15)) ([b35254a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b35254a9288e838afc574e8002432815a04f16f4))
* **upscale:** add standalone video upscale pipeline + CLI ([d175548](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/d17554885b3cc09b2c14e23c8a6d781ed21ee31e))
* **upstream-sync:** additive PR [#212](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/212) sync (iclora_utils + diffusion_steps + ic_lora refactor) → 0.11.1 ([#8](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/8)) ([30322b9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/30322b9292766dcbc0c9999b87691ad875be5d76))
* versioned safetensors loading ([#32](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/32)) ([3a3b28d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3a3b28d3b09621276261a54d04e838fece3510f1))
* warn on output dimension snapping via shared helper ([#72](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/72)) ([42ea2bb](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/42ea2bb6dc29e9ff974def828d95de192ef11393))
* wire TeaCache on res2s_denoise_loop (HQ path) ([c2f975f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/c2f975f58421c392e0b370ae04cf604791b8d505))


### Bug Fixes

* accurate transformer load time via mx.eval ([4fca24a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/4fca24a121c229a10cb9da71ccbf04446738952f)), closes [#18](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/18)
* add cleanup between Gemma encodes + disable STG pending shape fix ([cde7f1c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/cde7f1c3d741d072247e7ca86d2ac206af7c6c15))
* add phase timing for distilled text encoding ([#28](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/28)) ([668c657](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/668c657ec2789095da824caab1c433a1f083719d))
* align a2v pipeline with reference (dev model + CFG + denorm/renorm) ([272420a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/272420aade7e1bd733c10b37129621e6c04acc6d))
* align guidance defaults with Lightricks reference ([3311240](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/331124031e88954a7ab4cac45aa2212be0abb7de))
* align keyframe pipeline with reference — 4 divergences from audit ([40becda](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/40becda83bc2c6024d612e553e2840bede52d5c0))
* align MLX port with PyTorch reference — 11 bug fixes + two-stage keyframe ([570cce8](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/570cce8789631a089fb68bcf5661ab92a4de95bf))
* align retake/extend with reference (dev model + CFG guidance) ([1b7127d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1b7127d0abd9ec5683128ed9ad4ad4c2305f324b))
* align two-stage pipelines with reference (dev model + CFG + distilled LoRA) ([eaefa40](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/eaefa40b24b3ac7fc9e8449892182940c384d69e))
* apply streaming LoRA deltas under the correct block prefix ([#52](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/52)) ([#53](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/53)) ([b68459f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b68459f8c284a87da18eedc518237ff16e73c47d))
* audio-video sync in a2v pipeline ([2a2f5d7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/2a2f5d7b7e8760c4ddd1296f0d1dc2e28e9692a0))
* audit and fix CLI parameter issues ([98c24be](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/98c24bee8d03ca2ca662a013fa865e7dc85edf04))
* auto-encode DEFAULT_NEGATIVE_PROMPT for CFG in keyframe pipeline ([f59245f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f59245f29696d0a1dfa616503ccb5fa82250c01c))
* av_ca_timestep_scale_multiplier 1.0 → 1000.0 matching model config ([6a856f6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/6a856f6318ea90eeadcc38e57471c28b6888a3e0))
* cast bf16 waveform to fp32 in MLX before numpy conversion ([3962bfc](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3962bfce47b91030cf4dab811049f9b825db64e0))
* complete LoRA key remapping — 236 keys were silently ignored ([5c60cb9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/5c60cb9eeca47adcfc944fe2e7fb9f00c4ca10a1))
* **decode:** use frame_rate kwarg in VideoDecoder wrapper ([89071ba](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/89071ba04376fbe0e39924d1c50d7530fbf0e113)), closes [#17](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/17)
* default stg_scale=0.0 for 32GB Mac compatibility ([199f243](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/199f243bbedda7e147576b8764b1bb1f86db59c0))
* default to simple denoising for keyframe interpolation ([699529e](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/699529e9afa2b1c9621be133087e9c8545d67419))
* **defaults:** restore upstream stg_scale=1.0 on standard pipelines (was 0.0 for 32GB compat) ([61255ef](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/61255ef60540f955960fc61cc0bb9758be0ab261))
* defer VAE encoder + upsampler loading in a2v for memory ([ee6e910](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ee6e910b56ade6bf327b8152ca28ce32d82b5812))
* denormalize/renormalize latent around upsampler in IC-LoRA Stage 2 ([14c94a3](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/14c94a35e8eb2eede51bdd97ee5bccc7fc1e47bb))
* denormalize/renormalize latent around upsampler in two-stage pipelines ([703f1cf](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/703f1cf4bc800a2d7e055ea64b2331cf54e6124d))
* **deps:** update vulnerable locked dependencies ([2ded0c1](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/2ded0c19cbfcb054cdb8a3ca9d87d7d216dc21fc))
* disable STG/modality in keyframe guider params (attention shape bug) ([ecd8910](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ecd89109607e85b2e6de1de5c11b9c5e480aa6d8))
* disable upsampler normalization wrapping — causes grid artifacts ([9903c86](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/9903c86f0e026170756e6820f0ab753079b807d4))
* do not truncate muxed video to shortest stream in VAE decode ([#58](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/58)) ([d9f566a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/d9f566a641294a8562e9776ba343263771c26f70))
* dodge mlx 0.31.2 Metal scatter bug in audio upsampling ([#34](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/34)) ([#38](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/38)) ([7a26987](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/7a26987ac25138375454efbd04620b6d913e8506))
* enable pytorch_compatible GroupNorm in audio VAE ([ca784dd](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ca784ddf45c413b5f7fb178af330c4f59f5a1559))
* enable pytorch_compatible GroupNorm in upsampler ([133e1c1](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/133e1c194a68765576fb0543b45d0ea872d5faf1))
* explain macOS GPU-watchdog kills instead of dying cryptically ([#75](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/75)) ([#78](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/78)) ([8f43c23](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/8f43c23e1cba9ad586afeccde07d9e851903c0cf))
* extend Metal watchdog eval guards to all Apple Silicon Macs ([#3](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/3)) ([0897e7d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/0897e7d547ea4349f3dceb2c797bc2fef7b217bf))
* fail loud when spatial upsampler weights are missing ([#42](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/42)) ([251709f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/251709f45d9cee3a9813b06bc2c66113a4f82c1e))
* free decoders at end of generate_and_save (low_memory mode) ([3a79e52](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3a79e5273ed1b04720bde71b9c08089822073288))
* free the DiT before VAE decode in low-memory mode ([#74](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/74)) ([#76](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/76)) ([89d5400](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/89d54005a06c7d35d8557b46fd30c354252c8d7a))
* harden LTX-2.5 inference and release flow ([91239b3](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/91239b3620df0572dc8225b83c1725725852b48c))
* I2V pipeline staged loading for low_memory mode ([04b0ad7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/04b0ad7cdfc9c98e0f28bca43c76f91760fbdd42))
* **i2v:** strip appended keyframe tokens before unpatchify across all pipelines ([0e753b6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/0e753b609113f896a582f680f4d6ded2c1fdf883))
* **ic_lora:** align reference-video frame count to (1 + 8k) before VAE encode ([b0c5819](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b0c58194bc9d3e12a4240f61b9a64aae4c234019))
* **ic_lora:** align reference-video frame count to (1 + 8k) before VAE encode ([#29](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/29)) ([b0c5819](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b0c58194bc9d3e12a4240f61b9a64aae4c234019))
* **ic_lora:** tighter upstream-iso (UnboundLocalError + 4 API alignments) ([23127d6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/23127d65dd269fa4794df1b3bef5b9ff681e3b64))
* ic-lora dev-mode fuses distilled lora in the main pass; add --single-stage ([#63](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/63)) ([dcaf982](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/dcaf982be68dd2e893eca4d5851a4ab31f71ca55))
* keyframe conditioning must be applied BEFORE noising ([9c089ff](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/9c089ff33fe20b3cd23034e8b267d547cd7f2b16))
* **keyframe:** port num_pixel_frames from upstream PR [#192](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/192) ([b7a24e9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b7a24e9df1cdd5af2c68fcc0f0e2b962f5eb95be))
* load decoders on-demand in _decode_and_save for retake/extend ([53008b3](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/53008b35fc2e200305b86007feee316814d58594))
* **loaders:** honor _pending_loras across all pipeline load() overrides → 0.14.2 ([1f59643](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1f596435080c2f4c4ac1c1d1cad08c060d38c8b8))
* match reference output resolution (704x448 not 640x384) ([12a2ec4](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/12a2ec4972d3de64d0ceb311c65cdaa453345ae4))
* modality_scale=1.0 to disable (0.0 still triggers perturbation path) ([668d4b0](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/668d4b0907937010bf60d63887bdb2ed70d09857))
* move calibrate_teacache into src tree so -m import works ([d2f9206](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/d2f9206e11f2265ef23dc294622cfd084230d009))
* **pipelines:** drop wasteful Gemma re-load in load() — fixes Metal heap thrash ([1a30f74](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1a30f74f81e7780cac753fb99ca63c182c425d5b))
* **pipelines:** extend _pre_denoise_flush coverage to all denoise call sites ([#23](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/23)) ([81c8934](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/81c8934c1e17ffc074bf6378413ff1d10a7de057))
* **pipelines:** flush noised states before denoise loop on all pipelines ([#22](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/22)) ([3d466ed](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3d466ed7f83602677b950104639351f5b70c0532))
* pixel_shuffle channel ordering for MLX-converted conv weights ([1eb2c53](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1eb2c538d56021d86637625d271075fcd70cd259))
* port upstream bugfixes from Lightricks/LTX-2 PR [#179](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/179) ([22adef1](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/22adef112b8855360b47c16308781b35769c2a4a))
* propagate full guider params (STG, rescale, modality) to keyframe pipeline ([899ae78](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/899ae78e5a9557462b226ffde1763187232f332e))
* read av_ca_timestep_scale_multiplier from checkpoint config ([#39](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/39)) ([59a42d7](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/59a42d7f0eafd397c5c421868877c1b6d5324910)), closes [#37](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/37)
* remove dead code, fix CLI naming and help text inconsistencies ([6cd7beb](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/6cd7bebb6c5441b1959bb7b76cbbfcc46c9794ca))
* replace deprecated mx.metal.* with mx.* API ([4c733f6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/4c733f61c51f51fce428e9e1c9df6979494f250d))
* require dev model for keyframe interpolation ([667b0e2](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/667b0e2cff06a2a204f87fda836656781d07c494))
* round source video frames to VAE-compatible count (1+8k) in retake/extend ([504c399](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/504c399c16e498f9f75cfcb67844f68a702f88a1))
* staged model loading in keyframe pipeline for low-memory devices ([71f8e9c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/71f8e9c9434408f847de43fa482fd79856af7363))
* STG attention shape bug — 4D mask on 3D cross-attention output ([591a3d8](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/591a3d863e1d4076a5c4eaf99cd3fb7d9b13bd63))
* stop the Gemma encoder from widening a stricter cache limit ([#79](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/79)) ([#80](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/80)) ([aed35d6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/aed35d63714e71a6b8ed56b54aba3b9aac207648))
* **streaming:** fallback to eager block when guidance perturbations are active ([2fcdc97](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/2fcdc97da24f63a84f65a720bf5c9b65a5779b89))
* **streaming:** remove per-block mx.eval to avoid Metal watchdog at production token counts ([c67e547](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/c67e547b66a45568aa99a1f9efe265c64983bdaf))
* support indented version keys in bump_version.py ([ca8d4d9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ca8d4d9a631cca25e17aaedc930abb728660ba16))
* support quantized transformers at any group_size (not just 64) ([#60](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/60)) ([9af01c8](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/9af01c8fe318089abf042d33443fb815877e56d7))
* suppress divide-by-zero warning in mel filterbank ([f0cfe1c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f0cfe1c2433fa5db076a9b606e3d9e688ecf2b9e))
* suppress divide-by-zero warnings in ltx2_schedule ([e495563](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/e4955631e778349aa5dc3ec64389706d49808b33))
* synchronous VAE eval prevents Metal watchdog crash ([110a8e5](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/110a8e5649f4eaa735749a4c07fd2b5864cab30d))
* **text-encoder:** auto-split Gemma + connector forwards on &lt;=48 GB Macs ([3431205](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3431205d60ec38ed55027ef2463c283396476866))
* **text-encoder:** default Gemma forward to lazy graph (LTX2_GEMMA_EVAL_EVERY=0) ([8b2a29f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/8b2a29fb41596779f424d14e67a6188d77f0906f))
* **text-encoder:** materialize positive and negative prompts separately ([edda6b6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/edda6b69a0e518e2e9c6d1569b4118147602ca2b))
* **text-encoder:** mx.synchronize between Gemma layers + connector forward ([26e80a1](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/26e80a1185070b3b897164015c97cfa9835cf317))
* **text-encoder:** per-block sync in connector + LTX2_GEMMA_MAX_LENGTH override ([7d09201](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/7d09201f8cbeda3e7ab662c51d66293465a759ed))
* transpose latent layout for encoder normalize/denormalize ([82e01af](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/82e01afb41097952c9fcd30df946082121a19b5b))
* update tests to use transformer-distilled.safetensors filename ([160118f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/160118f3ecd9d7723ad294acfc03e6eaea9cb341))
* upsampler tests use mid_channels=32 (GroupNorm requires channels &gt;= 32) ([749d015](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/749d0151167bca73ee5ce87859b9dc8250ddcc64))
* use actual token count for ltx2_schedule sigma computation ([a0e49d0](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/a0e49d03ede5ee9e58a7f195e2870cb334fce51b))
* use correct half-resolution rounding for keyframe interpolation ([6e71b71](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/6e71b7195cbc9243d44d41700ae16f026037a0b2))
* use floor division for VAE frame rounding to avoid exceeding source length ([de4a12d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/de4a12d3cd14f345b2ec680eb63f4114b927b435))
* use LTX2Scheduler for dev model stage 1 instead of distilled sigmas ([e3f4467](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/e3f4467f7ddb7a168f52243445c8c02c8f958117))
* use relative path for local mlx-arsenal source in pyproject ([f74e753](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f74e753571149320e1fe9843a8f3bbcf78fee129))
* **vae:** port VideoDecoder dtype guard from upstream PR [#179](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/179) ([25e903e](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/25e903e6b7b269176a08de28d8f03d2f09f5a024))
* **vae:** VideoDecoder spatial_padding_mode hardcoded to "reflect", model uses "zeros" ([6c38f1e](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/6c38f1ed73a204c9ad0a1bf6630b206300b78cf6))
* wrap upsampler with encoder normalize/denormalize in keyframe pipeline ([50df81c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/50df81cfb5fe0092f8c26119d69883aa1cbcedc8))


### Performance Improvements

* use Flash Attention + compiled RoPE for faster inference ([5e75d27](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/5e75d278910b91c0f6d29dbd44908a2fe952bfab))
* **vae:** auto-tile VAE decode to cap peak Metal memory on HD/long runs ([15be202](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/15be202b73e671f6a91cf10b80610f81df8223a7))
* **vae:** auto-tile VAE decode to cap peak Metal memory on HD/long runs ([#25](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/25)) ([15be202](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/15be202b73e671f6a91cf10b80610f81df8223a7))


### Reverts

* av_ca_timestep_scale_multiplier back to 1.0 ([01da05c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/01da05c9171c551b83e7919347031a7949aa693e))
* restore keyframe pipeline to test-transition-7 state ([1db1401](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1db14014913061bbaa41b44f2fb10b4754dd29ed))


### Documentation

* --low-ram now covers generate / two-stage / hq / a2v / keyframe ([40bbe3d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/40bbe3d4c0a44873cdfdca56f6499c32b9ba2fd3))
* --low-ram now covers ic-lora + custom distilled-lora-strength via bind-time fusion ([b41217a](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b41217a3b10d8828ce7f0b463c1b0d5938c8e56f))
* add Block Streaming section + --low-ram CLI examples ([f38816d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f38816dacfac5c93fc5549ddb66536ecfa19fb8b))
* add IC-LoRA pipeline documentation to CLAUDE.md ([94154b0](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/94154b003fa179d46b0598805c34b0153821f1fd))
* add Modality Tiling section + v0.4.0 update across CLAUDE.md / README.md ([a1277e9](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/a1277e93ec2d9c14932034bb4ed7407661de7e39))
* add pipelines + options matrix at docs/PIPELINES.md ([9439d36](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/9439d36421daa3c98e9ae9b45a6f724e057af958))
* add TeaCache calibration & integration design for stage 1 ([1e0dd4b](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/1e0dd4b8af9209c0f85de4b6d27c30221362fe02))
* add TeaCache implementation plan ([4b87b3f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/4b87b3f7f1d9a81e0a757d27199bcace924ee208))
* add TeaCache section to CLAUDE.md ([f8c0d70](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f8c0d700751a467450d47594655d89f01a3b2f45))
* add two-stage pipeline documentation to CLAUDE.md ([4b1a95f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/4b1a95fb934ee1de86a91a2d831dff012c67e1cb))
* bootstrap ltx-mlx — pure MLX port of ltx-core for Apple Silicon ([90fd769](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/90fd769da7f1af8944cb0bb0ffee53515b47fe79))
* bring CLAUDE.md / README / PIPELINES.md into coherence ([#11](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/11)) ([4d46f61](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/4d46f619363e926c03d53cd2d81b10048400537a))
* cleanup stale docs, remove legacy scripts, update CLAUDE.md ([3a50fff](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3a50fff5418817f2fcec797913ae6c4eb2b16964))
* consolidate documentation hierarchy ([28415eb](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/28415eb399a8187612cd2acce568611c5310c12b))
* document 0.14.16 features in CLAUDE.md ([#65](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/65)) ([b283144](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/b283144a5207c97a10b3cc8df2bb6491f7f14285))
* document ic-lora --upsample-only / --refine-steps in CLAUDE.md ([#70](https://github.com/TommyKammy/ltx-2.5-mlx-inference/issues/70)) ([8e1526d](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/8e1526d3147086d8981b30f1e03496012c059125))
* HDR IC-LoRA section + Metal watchdog guard env vars (v0.5.0) ([2c40b80](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/2c40b80fb6bad30ae93be2e1b6acc7b744909046))
* HQ TeaCache empirical 1.78x speedup with res_2s-specific coefs ([ae8f095](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ae8f095f4c245de72f6a74b90021c827ffef8ff1))
* HQ TeaCache empirical limit — no speedup with Euler coefs ([0ebb84c](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/0ebb84c935613bfcbc6feafadd042f3ca9d39441))
* production-quality regression results (Q1-Q8 + fix history) ([ac262ea](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/ac262eaae6d66e502f2ef8e3dc89a34d89213dd0))
* scrub stale LTX2_METAL_WATCHDOG_GUARD refs after 8877f88 removal ([9601ee6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/9601ee6faae172ee0b05ac4fe36c3c0c644ed7e8))
* static-scene I2V recipe (ic-lora + canny control video) — validated Phoenix Q15 ([09c4526](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/09c4526ec704f4c4f02073a4c6f38f96309bb728))
* **streaming:** update --low-ram help to reflect shipped 75% RAM reduction ([f2ec151](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/f2ec1515efa7176b7a1e65ac9412b0f4a1689c10))
* **text-encoder:** clean up stale comment from earlier 'lazy by default' iteration ([364f909](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/364f9096adfe1feadbc687ffc986606e90b44941))
* update CLAUDE.md and README with current pipeline defaults ([51ed849](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/51ed849754b66a84ecd1798f209e5215ac2bece2))
* update CLAUDE.md TeaCache section to cover --hq path ([464a32b](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/464a32b7587087e017dd5759cae52e5abde42d04))
* update HuggingFace repo names after rename ([d02ef3f](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/d02ef3fae4298ecd0258a875cbe9e3d2c653f523))
* update keyframe divergence report with test matrix results ([45b00e6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/45b00e69dcfc38428ac5c92170392a057e55ba15))


### Code Refactoring

* **a2v:** remove a2v --hq (not in upstream) (BREAKING) ([d593c5b](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/d593c5b648f635e9576e307b447ca64847032c88))
* **cli:** rename --hq → --two-stages-hq (matches upstream class name) ([3f25f64](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/3f25f64fe07b2c08275292c5a4eb7b464a68e969))
* remove ImageToVideoPipeline (legacy, no upstream equivalent) (BREAKING) ([493aec2](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/493aec2b38d902370d55d19faa24e7971bcd9791))
* rename pipeline classes to match upstream verbatim (BREAKING) ([d6cc3d1](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/d6cc3d1d4a335a60169f70eaa5ad59279e59cedd))
* **retake:** fold extend into RetakePipeline (file iso with upstream) ([c2f3126](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/c2f31265bde5caf591c1fc92fb33b58f69968dc9))
* ti2vid_one_stage.py now hosts TI2VidOneStagePipeline (file iso) ([202a8b6](https://github.com/TommyKammy/ltx-2.5-mlx-inference/commit/202a8b6f393471135e06aa8aa25e999c55aed8f8))

## [0.14.19](https://github.com/dgrauet/ltx-2-mlx/compare/v0.14.18...v0.14.19) (2026-07-19)


### Bug Fixes

* explain macOS GPU-watchdog kills instead of dying cryptically ([#75](https://github.com/dgrauet/ltx-2-mlx/issues/75)) ([#78](https://github.com/dgrauet/ltx-2-mlx/issues/78)) ([8f43c23](https://github.com/dgrauet/ltx-2-mlx/commit/8f43c23e1cba9ad586afeccde07d9e851903c0cf))
* free the DiT before VAE decode in low-memory mode ([#74](https://github.com/dgrauet/ltx-2-mlx/issues/74)) ([#76](https://github.com/dgrauet/ltx-2-mlx/issues/76)) ([89d5400](https://github.com/dgrauet/ltx-2-mlx/commit/89d54005a06c7d35d8557b46fd30c354252c8d7a))
* stop the Gemma encoder from widening a stricter cache limit ([#79](https://github.com/dgrauet/ltx-2-mlx/issues/79)) ([#80](https://github.com/dgrauet/ltx-2-mlx/issues/80)) ([aed35d6](https://github.com/dgrauet/ltx-2-mlx/commit/aed35d63714e71a6b8ed56b54aba3b9aac207648))

## [0.14.18](https://github.com/dgrauet/ltx-2-mlx/compare/v0.14.17...v0.14.18) (2026-07-11)


### Features

* warn on output dimension snapping via shared helper ([#72](https://github.com/dgrauet/ltx-2-mlx/issues/72)) ([42ea2bb](https://github.com/dgrauet/ltx-2-mlx/commit/42ea2bb6dc29e9ff974def828d95de192ef11393))


### Documentation

* document ic-lora --upsample-only / --refine-steps in CLAUDE.md ([#70](https://github.com/dgrauet/ltx-2-mlx/issues/70)) ([8e1526d](https://github.com/dgrauet/ltx-2-mlx/commit/8e1526d3147086d8981b30f1e03496012c059125))

## [0.14.17](https://github.com/dgrauet/ltx-2-mlx/compare/v0.14.16...v0.14.17) (2026-07-10)


### Features

* ic-lora --upsample-only + control-aware --refine-steps ([#68](https://github.com/dgrauet/ltx-2-mlx/issues/68)) ([16580db](https://github.com/dgrauet/ltx-2-mlx/commit/16580db376888316803505d5e163048cc902ec93))


### Documentation

* document 0.14.16 features in CLAUDE.md ([#65](https://github.com/dgrauet/ltx-2-mlx/issues/65)) ([b283144](https://github.com/dgrauet/ltx-2-mlx/commit/b283144a5207c97a10b3cc8df2bb6491f7f14285))

## [0.14.16](https://github.com/dgrauet/ltx-2-mlx/compare/v0.14.15...v0.14.16) (2026-07-09)


### Features

* Prompt Relay temporal prompt gating ([#61](https://github.com/dgrauet/ltx-2-mlx/issues/61)) ([b9aa475](https://github.com/dgrauet/ltx-2-mlx/commit/b9aa475ac90ebc2bbfe1dffd97ee6bdee5a823f5))


### Bug Fixes

* ic-lora dev-mode fuses distilled lora in the main pass; add --single-stage ([#63](https://github.com/dgrauet/ltx-2-mlx/issues/63)) ([dcaf982](https://github.com/dgrauet/ltx-2-mlx/commit/dcaf982be68dd2e893eca4d5851a4ab31f71ca55))
* support quantized transformers at any group_size (not just 64) ([#60](https://github.com/dgrauet/ltx-2-mlx/issues/60)) ([9af01c8](https://github.com/dgrauet/ltx-2-mlx/commit/9af01c8fe318089abf042d33443fb815877e56d7))

## [0.14.15](https://github.com/dgrauet/ltx-2-mlx/compare/v0.14.14...v0.14.15) (2026-07-01)


### Bug Fixes

* add missing frame_rate to combined_image_conditionings, fixing a2v/lipdub with image conditioning ([#56](https://github.com/dgrauet/ltx-2-mlx/issues/56)) ([cc0cacc](https://github.com/dgrauet/ltx-2-mlx/commit/cc0caccc4287855c56ba56628b5346b55f192c37))
* do not truncate muxed video to shortest stream in VAE decode ([#58](https://github.com/dgrauet/ltx-2-mlx/issues/58)) ([d9f566a](https://github.com/dgrauet/ltx-2-mlx/commit/d9f566a641294a8562e9776ba343263771c26f70))

## [0.14.14](https://github.com/dgrauet/ltx-2-mlx/compare/v0.14.13...v0.14.14) (2026-06-29)


### Bug Fixes

* apply streaming LoRA deltas under the correct block prefix ([#52](https://github.com/dgrauet/ltx-2-mlx/issues/52)) ([#53](https://github.com/dgrauet/ltx-2-mlx/issues/53)) ([b68459f](https://github.com/dgrauet/ltx-2-mlx/commit/b68459f8c284a87da18eedc518237ff16e73c47d))

## [Unreleased]

## [0.14.13] - 2026-06-22

Makes multi-anchor I2V reachable on the `--one-stage` and `--distilled`
generate modes. Both pipelines already accepted the upstream-iso `images=`
list and routed it through `combined_image_conditionings`; a leftover CLI
guard (`_legacy_single_image`) was the only thing rejecting more than one
`--image` anchor or a non-trivial `frame_idx`/`strength` on these modes,
artificially restricting multi-anchor I2V to `--two-stage` / `--two-stages-hq`.
Removing the guard brings the CLI in line with upstream, where `--image` is
repeatable across all modes. Purely additive — only previously-erroring paths
are affected; `--two-stage` / `--two-stages-hq` behavior is unchanged.
Validated with start+end anchor smoke tests at 512×512×25 on both
`--distilled` and `--one-stage`. Thanks to
[@plz12345](https://github.com/plz12345) (#45).

### Added

- Multi-anchor I2V on `--one-stage` and `--distilled`: the repeatable
  `--image PATH FRAME_IDX STRENGTH` form now works on every `generate` mode.
  `frame_idx=0` hard-replaces the first latent frame
  (`VideoConditionByLatentIndex`); `frame_idx>0` appends a soft keyframe anchor
  (`VideoConditionByKeyframeIndex`). New "Multi-Anchor I2V" section in
  `CLAUDE.md` documents the form and the `(num_frames - 1) % 8 == 0`
  frame-count constraint.

### Fixed

- `VideoConditionByKeyframeIndex.frame_idx` docstring corrected from "latent
  frame index" to "pixel frame index (0-based)", matching the math in
  `_compute_keyframe_positions` and the `--image` help text.
- `uv.lock` resynced to the released package versions (the 0.14.12 release
  bumped the workspace `pyproject` files but left the lockfile at 0.14.11).

## [0.14.12] - 2026-06-15

Enables end-to-end joint audio-video LoRA training on Apple Silicon, closing
the gap between what the trainer config accepted and what it could actually
execute. Adds an audio preprocessing path, a video slicer for preparing
training clips, and gradient checkpointing so the dev model can backprop on a
64 GB machine. Also fixes four latent crashers in the existing trainer that
would have broken any audio training run — three of them (`fps=` →
`frame_rate=` at trainer call sites) are regressions from the v0.14.0
iso-strict rename that missed the trainer package, the same class of miss as
the v0.14.1 decode-wrapper fix. Validated with a real 2000-step audio-style
LoRA run on an M5 Pro 64 GB (74 clips, 192×192, rank 32). Thanks to
[@plz12345](https://github.com/plz12345) (#43).

### Added

- `ltx-2-mlx slice` command — cuts long source videos into normalized,
  resolution-aligned training clips with audio retained: fixed-interval or
  timecode-list slicing, aspect-safe crop/pad, `--max-clips` with even or
  sequential sampling, and per-source output subfolders
  (`ltx_trainer_mlx/slice_clips.py`).
- `preprocess --with-audio` — encodes each clip's audio track through the
  audio VAE encoder into `audio_latents/` alongside the video latents, sized
  to `compute_audio_token_count()` so the two modalities are aligned by
  construction. Adds `load_audio_vae_encoder` to the trainer model loader and
  recursive clip discovery so per-source subfolders from `slice` work.
- Gradient checkpointing on `LTXModel` (`gradient_checkpointing` flag, default
  off, no inference effect), wired to the trainer via
  `OptimizationConfig.enable_gradient_checkpointing` and the `train --low-ram`
  CLI flag. Recomputes each transformer block in the backward pass to cap
  activation memory at ~1 block (vs storing all 48), letting the dev model
  backprop fit on 64 GB. LoRA params are passed as explicit `mx.checkpoint`
  inputs so their gradients are tracked (a naive wrap would silently zero
  them). Covered by a grad-equivalence test.
- `transformer_file` config field to pin an explicit transformer safetensors
  filename (e.g. `transformer-dev.safetensors`) instead of relying on
  auto-detection.
- Example training config `configs/lora_av_whisper.yaml` (whisper/ASMR
  audio-style LoRA).

### Changed

- `preprocess` no longer downloads the full model snapshot when given a
  HuggingFace repo ID. It now does a partial download of only the encoder
  files preprocessing actually loads (connector + video/audio VAE), skipping
  the ~20 GB transformer (~80 GB total saved). **Impact:** anyone who relied
  on `preprocess` to populate the full HF cache must now run
  `huggingface-cli download <repo>` separately or pass an already-cached local
  path. `~` is now expanded in `model_path` config validation.

### Fixed

- Trainer audio training was broken by `fps=` keyword arguments at three call
  sites (`trainer.py`, `training_strategies/base_strategy.py`,
  `validation_sampler.py`) — the parameter was renamed to `frame_rate=` in
  v0.14.0 but the trainer package was not covered by that audit.
- Validation sampler called the video and audio decoders directly
  (`decoder(latent)`) instead of `decoder.decode(latent)`.
- `bfloat16` arrays were passed to numpy without a cast in `video_utils.py`
  (numpy has no bfloat16 buffer dtype); now cast to `float32` in MLX first.

## [0.14.11] - 2026-06-08

Fixes audio cross-modal gating (speech / lip-sync) by reading the
transformer config from the checkpoint instead of relying on hardcoded
dataclass defaults. Every LTX-2.3 checkpoint ships
`av_ca_timestep_scale_multiplier = 1000.0` (in both `config.json` and
`embedded_config.json`), but the MLX `LTXModelConfig` dataclass default was
`1.0` and the loaders never read the checkpoint — so the audio↔video
cross-attention gate AdaLN received `sigma * 1` instead of `sigma * 1000`,
mis-weighting the cross-modal information that carries voice/dialog. The
root cause was copying upstream's *dataclass* default (`1`) without wiring
upstream's *configurator*, which reads the value from the checkpoint
(`config.get("av_ca_timestep_scale_multiplier", 1)` → `1000`). The fix
mirrors upstream `LTXModelConfigurator.from_config`: hyperparameters are now
read from the checkpoint at load time across all pipelines and the trainer.
Audio output changes for every generation (toward upstream parity);
validated end-to-end (config-driven output is bit-identical to manually
setting the multiplier to 1000, and materially different — waveform
correlation 0.31 — from the previous behaviour). See issue #37; independent
confirmation in Acelogic/LTX-2-MLX `AUDIO_ISSUES.md`.

### Fixed

- AV cross-attention gate was attenuated by reading
  `av_ca_timestep_scale_multiplier = 1.0` (dataclass default) instead of the
  checkpoint's `1000.0`. `load_transformer` (`utils/_orchestration.py`), the
  LoRA-fused path (`_base.py`) and the trainer loader
  (`ltx_trainer_mlx/model_loader.py`) now build the model config from the
  checkpoint via `LTXModelConfig.from_checkpoint_dir()` (#37).

### Added

- `LTXModelConfig.from_checkpoint_config(dict)` and
  `LTXModelConfig.from_checkpoint_dir(path)` — read transformer
  hyperparameters from a checkpoint's `embedded_config.json` (preferred) or
  `config.json`, mirroring upstream `LTXModelConfigurator.from_config`. The
  dataclass defaults are the per-key fallback, so direct `LTXModel()`
  construction is unchanged.
- `tests/test_av_ca_timestep_config.py` — pins the checkpoint-read behaviour,
  guards against architecture drift (only `av_ca_timestep_scale_multiplier`
  may differ from defaults on the shipped config), and asserts the gate
  timestep embedding is load-bearing.

## [0.14.10] - 2026-06-07

Fixes near-silent audio (mean ≈ −52 dB instead of ≈ −13 dB) in generated
videos on **mlx 0.31.2**. mlx 0.31.2 shipped a Metal scatter-kernel
regression (ml-explore/mlx#3266, reported as #3477, fixed upstream by
#3483 but not yet in any release) where `mx.array.at[<strided slice>].add()`
mis-indexes its *source* on the Metal backend. The audio path used that
op twice for zero-insert upsampling — in the BigVGAN vocoder
(`UpSample1d`) and the BWE resampler (`HannSincResampler`) — so the
corrupted zero-insert fed every SnakeBeta activation and collapsed the
waveform to noise. Video was unaffected. Both call sites now use plain
strided assignment, which is equivalent (the destination is freshly
zeroed) and correct on mlx 0.31.1, 0.31.2 and main. No version pin is
added: 0.31.1 is itself unsafe on some setups (Metal watchdog crashes at
text-encode) and `mlx-lm>=0.31.3` requires `mlx>=0.31.2`. See issue #34.

### Fixed

- `audio_vae/vocoder.py` (`UpSample1d`) and `audio_vae/bwe.py`
  (`HannSincResampler`): replace `at[<strided>].add()` zero-insert with
  strided assignment to dodge the mlx 0.31.2 Metal scatter bug (#34).

### Added

- `tests/test_audio_scatter_regression.py` — NumPy-reference tests for the
  two real call sites (`UpSample1d`, `HannSincResampler`) plus a framework
  canary that skips with a diagnostic on an affected mlx backend.

## [0.14.9] - 2026-06-02

Handles LTX-2.3 model directories that ship versioned safetensors
filenames (e.g. `transformer-distilled-1.1.safetensors`). Previously the
loader hardcoded unversioned names, so it silently ignored LTX's newer
file revisions — and failed hard if a user kept only the newer file to
save disk. Resolution is now dynamic: the alphabetically-latest versioned
file wins over the unversioned exact name when both are present. After an
upstream sync + re-forge, the code picks up the newer weights with no
changes. Thanks to [@plz12345](https://github.com/plz12345) for the
contribution (PR #32).

### Added

- `BasePipeline._resolve_safetensors(model_dir, stem)` — resolves a
  (possibly versioned) safetensors path, preferring `{stem}-*.safetensors`
  over `{stem}.safetensors` and returning the canonical exact path when
  nothing exists (clear `FileNotFoundError`). Wired into transformer,
  distilled-LoRA, and upscaler resolution across `_base`, `distilled`,
  `ic_lora`, and `ti2vid_two_stages`.
- `_load_weights` fallback in `loader/sft_loader.py` — loads extensionless
  HuggingFace cache blobs via `mx.load(path, format="safetensors")`, which
  `mx.load` cannot infer by suffix. Reachable when a model dir resolves
  through a `snapshots/` symlink to the real GUID blob name (custom or
  refined models).
- Trainer `model_loader.load_transformer` auto-detect extended to
  versioned transformer names.

### Fixed

- Upscaler file naming and key-prefix handling: supports both the new
  v1.1+ bare-key layout and the legacy stem-prefixed layout.

## [0.14.8] - 2026-05-22

Enables `generate --lora` on the `--low-ram` block-streaming path.
Previously, combining the two raised `NotImplementedError` because
LoRA fusion required a fully-materialised weight dict before
block-stream eviction started. The streaming path now attaches each
pending LoRA as a `BlockLoraSource` on the `StreamingLTXModel`
wrapper — fusion happens per-block at each `bind()`, mirroring the
pattern already used by `ICLoraPipeline._fuse_loras` for control
LoRAs. Works for community LoRAs at strength 1.0 and at custom
strengths. Thanks to [@plz12345](https://github.com/plz12345) for the
contribution (PR #30, follow-up to #20).

### Added

- `resolve_lora_path` helper in `ltx_pipelines_mlx.utils._orchestration`
  shared by the streaming and non-streaming LoRA paths. Accepts local
  `.safetensors` paths and HuggingFace repo IDs. Raises `ValueError`
  on ambiguous multi-safetensors repos (lists the candidate file
  names) and `FileNotFoundError` on empty repos.
- Audio / joint-block LoRA key remappings (`.linear_1.` → `.linear1.`,
  `.linear_2.` → `.linear2.`, `audio_ff.net.0.proj.` →
  `audio_ff.proj_in.`, `audio_ff.net.2.` → `audio_ff.proj_out.`)
  consolidated into the shared `LTXV_LORA_COMFY_RENAMING_MAP` in
  `ltx_core_mlx.loader.sd_ops` so the streaming path picks them up
  automatically (it goes through the map directly, no longer through
  `ti2vid_two_stages._remap_lora_keys`).
- Tests: streaming dispatch now pins `BlockLoraSource` ctor args and
  exercises a parametrized two-LoRA case; new `test_resolve_lora_path`
  covers the 4 resolution branches (local-exists, HF single, HF
  multi-raises, HF zero-raises); new `test_lora_renaming_map` locks
  the contract for the 4 audio/joint-block patterns.

### Changed

- CLAUDE.md "Limitations" + CLI `--low-ram` help text updated: the
  `generate --lora` flag is now compatible with `--low-ram` via
  per-block bind-time fusion.
- `_remap_lora_keys` in `ti2vid_two_stages.py` simplified to a single
  dict comprehension; `or k` fallback removed (verified dead — the
  shared map's `apply_to_key` always returns a string given
  `with_matching()` + no `allowed_keys`).
- `resolve_lora_path` writes its "Downloading LoRA from HuggingFace"
  notice to stderr via `print(..., file=sys.stderr)` instead of
  `logging.info` (which was swallowed by the absent logger config).

## [0.14.7] - 2026-05-20

Hotfix for a long-standing IC-LoRA reference-video crash. Any caller
passing an 8k-frame source file (the format LTX itself produces — its
``_decode_and_save_video`` drops the leading frame on write) into
``ICLoraPipeline.generate_and_save(video_conditioning=...)`` hit a
``space_to_depth`` reshape error at ``ltx_core_mlx/model/video_vae/sampling.py:121``
because the encoder's first temporal-stride-2 block requires a
``(1 + 8k)``-frame input. Failure was input-content-independent: a raw
RGB driving video and a canny-edges control map produced byte-identical
error numbers at the same reshape site.

### Fixed

- ``append_ic_lora_reference_video_conditionings`` in ``iclora_utils.py``
  now probes the source with ``probe_video_info``, clamps to the
  caller's target ``num_frames``, and rounds down to the nearest
  ``(1 + 8k)`` before invoking ``load_video_frames_normalized``.
  Mirrors ``RetakePipeline._encode_source_video``. Applies to every
  ``ICLoraPipeline`` subclass — including ``HDRICLoraPipeline`` (where
  the reporter observed the same crash at a different spatial scale,
  ``reference_downscale_factor=1``) and ``LipDubPipeline``'s
  video-reference path.

### Changed

- Lifted the local ``from ltx_core_mlx.components.patchifiers import
  compute_video_latent_shape`` inside ``append_ic_lora_reference_video_conditionings``
  to module scope. Same scoping anti-pattern that caused the
  ``UnboundLocalError`` previously fixed in ``ic_lora.py`` (commit
  ``23127d6``); not load-bearing here, but matches the cleanup precedent.

### Credit

Bug surfaced and diagnosed by [@R0drig0Diaz](https://github.com/R0drig0Diaz)
in [#27](https://github.com/dgrauet/ltx-2-mlx/issues/27) — with
byte-identical reproductions across two input modalities (RGB +
canny-edges) and two LoRA variants (Union Control with
``reference_downscale_factor=2``, HDR with ``reference_downscale_factor=1``),
plus the ``RetakePipeline._encode_source_video`` precedent and a 3-fix
proposal. The two scoping-trap items called out in #27 (``ic_lora.py:261``
+ ``ic_lora.py:501``) were already resolved on ``main`` since
``23127d6``; the reporter was on stale HEAD ``0e753b6``.

## [0.14.6] - 2026-05-20

Automatic temporal tiling for the video VAE decoder. The block-3
DepthToSpaceUpsample intermediate (``(B, 512, 4F, 4H, 4W)`` in bf16)
dominates peak Metal activation memory at HD or long durations and
pushed 32 GB Macs into swap on 720p+ runs beyond ~20s — even when the
rest of the pipeline (transformer streamed, decoders loaded on demand)
fit comfortably.

### Added

- ``_compute_decode_tiling(latent_shape, frame_rate)`` in
  ``ltx_core_mlx.model.video_vae.video_vae``: pure-arithmetic helper
  that derives a ``TilingConfig`` from the latent shape and the
  ``LTX2_VAE_DECODE_BUDGET_GB`` budget (default ``8.0``). Returns
  ``None`` when the full video already fits, so the no-tiling path
  has zero overhead at common resolutions. Tile size and overlap
  scale with frame rate (~1 second of pixel frames of overlap).
- ``VideoDecoder.decode_and_stream`` (pipelines wrapper) now prints
  ``[vae-decode tiled: tile_frames=N overlap=K]`` to stderr when tiling
  kicks in, gated on the pipeline's ``verbose`` flag.

### Changed

- ``VideoDecoder.tiled_decode`` (core) inserts ``mx.eval`` +
  ``aggressive_cleanup`` after each tile decode and after each
  accumulation step so prior-tile activations are freed before the
  next tile begins.
- ``VideoDecoder.decode`` gains an opt-in ``_materialize_stages``
  keyword-only flag (default ``False``) that forces ``mx.eval`` between
  the four upsample stages. Only set ``True`` by ``tiled_decode`` —
  the no-tiling fast path keeps full kernel fusion across upsample
  stages.
- ``A2VidPipelineTwoStage._upscale_and_optionally_encode`` was
  reaching into ``self.vae_decoder.decode_and_stream`` directly;
  routed through ``self.video_decoder_block.decode_and_stream`` like
  every other pipeline. Removes a stale ``assert self.vae_decoder
  is not None`` (the block's ``load()`` is idempotent) and gives a2v
  the same stderr marker as the rest.

### Note on numerical equivalence

Tiled decode is **not** bit-equivalent to a non-tiled decode at the
same configuration. The video VAE's causal ``Conv3dBlock``
(``convolution.py:62-66``) replicates each tile's first frame for
temporal padding, so isolated tiles diverge from the full-decode
context at boundaries. The trapezoidal blend mask smooths the seam
visually but does not reconstruct the exact signal. This is intrinsic
to any tiled-VAE-decode and matches the upstream behaviour — users
switching into tiled mode at 1080p+ should expect minor boundary
drift vs. the same config with enough RAM to skip tiling.

### Benchmarks (one run each, ``--distilled`` 8/3 at 480p × 15s × 25fps)

| stage | no-tile | tiled (opt-in via large input) | Δ |
|---|---|---|---|
| decode | 124.1s | 131.4s | +5.9% |
| total | 841.0s | 881.9s | +4.9% |

No-tiling fast path is unchanged.

### Credit

End-to-end PR by [@plz12345](https://github.com/plz12345) in
[#25](https://github.com/dgrauet/ltx-2-mlx/pull/25), iterated through
two rounds of review covering env-var budget gating, scoped
``BrokenPipeError`` handling, fp32→bf16 budget correction, stderr
marker plumbing, a2v consistency cleanup, and the multi-tile
integration test. Production-validated on plz12345's M5 MacBook Air
32 GB for a week prior to submission.

## [0.14.5] - 2026-05-19

CLI phase-marker coverage gap on the distilled two-stage path. The
``[Encoding prompt] ... done in X.Xs`` marker introduced in v0.13.1
was emitted by every pipeline that goes through ``BasePipeline``'s
text-encoding helper, but ``DistilledPipeline.generate_two_stage``
encodes the (positive-only) prompt inline and was missed in the v0.13.1
audit. ``[Loading text encoder]`` was emitted, then silence until
``[Loading DiT]``.

### Fixed

- Wrap ``_encode_text`` + ``_materialize`` in ``DistilledPipeline.generate_two_stage``
  with the ``phase("Encoding prompt", ...)`` context manager so the
  encoding duration is reported on stderr like every other pipeline.
  Caught by external contributor [@plz12345](https://github.com/plz12345)
  in PR #28.

## [0.14.4] - 2026-05-14

Apple Silicon Metal watchdog hardening for the denoise loop. On
M2 Max 64 GB (and any Apple Silicon under load), the macOS GPU
watchdog could fire with ``MTLCommandBufferErrorInternal`` (code 14)
at the start of a denoise loop when the accumulated pre-denoise lazy
graph — VAE encoding, conditioning blend, and noise addition — was
submitted as a single oversized Metal command buffer exceeding the
~10s watchdog window.

### Fixed

- Add ``BasePipeline._pre_denoise_flush(video_state, audio_state)``
  that calls ``mx.eval`` on the noised latent states to force-materialise
  the accumulated graph in its own command buffer before the denoise
  loop begins. Each subsequent denoise-step buffer is then within the
  watchdog window.
- Wire the flush at every denoise call site across all pipelines
  (18 sites total): ``BasePipeline.generate`` (one-stage distilled),
  ``TI2VidOneStagePipeline`` (dev one-stage + CFG), ``DistilledPipeline``
  (two-stage), ``TI2VidTwoStagesPipeline`` and ``TI2VidTwoStagesHQPipeline``
  (both stages), ``A2VidPipelineTwoStage`` (both stages),
  ``ICLoraPipeline`` and ``HDRICLoraPipeline`` (both stages, via
  inheritance), ``RetakePipeline`` (retake + extend), ``KeyframeInterpolationPipeline``
  (stage 1 dev/distilled branches + stage 2), and ``LipDubPipeline``
  (both stages).

### Credit

Initial fix and validation on M2 Max 64 GB by
[@colinbdesign](https://github.com/colinbdesign) in
[#22](https://github.com/dgrauet/ltx-2-mlx/pull/22) — covered
``BasePipeline.generate`` plus the two two-stage variants. Coverage
extended to the remaining 14 call sites in
[#23](https://github.com/dgrauet/ltx-2-mlx/pull/23).

## [0.14.3] - 2026-05-14

Accurate transformer-load phase timing. Before this patch, the
``[Loading transformer (...)] done in 0.1s`` marker reported ~0.1s for
a 10+ GB load — MLX is lazy, so ``apply_quantization`` + ``load_weights``
build a graph but defer the real work. The marker measured graph
construction, not loading.

### Fixed

- Force MLX graph materialisation immediately after ``load_weights`` in
  both the orchestration helper (``utils._orchestration.load_transformer``)
  and the LoRA-fusion path (``_base.py``). Both branches now report
  real load time (~1.8s empirically observed by the reporter on a
  typical run).

### Credit

Bug surfaced by [@plz12345](https://github.com/plz12345) in
[#18](https://github.com/dgrauet/ltx-2-mlx/pull/18). Release PR
adds the symmetric guard to the LoRA-fusion path for consistency.

## [0.14.2] - 2026-05-14

Hotfix for a long-standing latent bug: setting ``pipe._pending_loras = [...]``
from the CLI was silently dropped by every pipeline whose ``load()`` method
overrides :meth:`BasePipeline.load` — that is, ``--distilled``, ``--one-stage``,
``--two-stage``, and ``--two-stages-hq``. Only the ``BasePipeline.load()``
path (no longer reached by any T2V/I2V CLI mode) honored the flag, so T2V
generation with ``--lora`` produced output indistinguishable from a
base-model run.

### Fixed

- ``BasePipeline._load_transformer_with_optional_streaming`` now honors
  ``_pending_loras`` directly. Every pipeline whose ``load()`` routes
  through this wrapper (or through ``_load_dev_transformer``, which
  transitively calls the wrapper) automatically picks up LoRA fusion —
  no subclass-level boilerplate required. Pre-existing pipelines fixed:
  ``DistilledPipeline``, ``TI2VidOneStagePipeline``, ``TI2VidTwoStagesPipeline``,
  ``TI2VidTwoStagesHQPipeline``.
- New regression test (``tests/test_pending_loras_dispatch.py``) locks the
  contract: every pipeline ``load()`` override must route DiT construction
  through the wrapper. Catches future overrides that would silently
  reintroduce the bug.

### Credit

Bug surfaced by [@colinbdesign](https://github.com/colinbdesign) in
[#16](https://github.com/dgrauet/ltx-2-mlx/pull/16) (closed in favor of
this PR's wrapper-level fix, which is upstream-iso friendly and covers
all four affected pipelines instead of just ``DistilledPipeline``).

## [0.14.1] - 2026-05-14

Hotfix for a regression introduced by the v0.14.0 `fps` → `frame_rate`
rename. The `VideoDecoder.decode_and_stream` wrapper in
`ltx_pipelines_mlx/utils/blocks.py` was missed during the audit and
kept the old `fps=` kwarg, while the inner `ltx_core_mlx`
`VAE.decode_and_stream` now requires `frame_rate=` mandatory
keyword-only. Every decode path raised `TypeError: ... got an
unexpected keyword argument 'frame_rate'` at mux time.

### Fixed

- `VideoDecoder.decode_and_stream` wrapper accepts and forwards
  `frame_rate=` (was still `fps=`). Affects every pipeline that goes
  through the orchestration helper: `--two-stage`, `--two-stages-hq`,
  `a2v`, `keyframe`, `ic-lora`, `hdr-ic-lora`. One-stage was
  unaffected — bug was isolated to the decode hop.
  Closes [#17](https://github.com/dgrauet/ltx-2-mlx/pull/17).
  Thanks to [@plz12345](https://github.com/plz12345) for the catch +
  patch.

## [0.14.0] - 2026-05-13

Ultra-strict upstream-iso pass on the `frame_rate` parameter. Mirrors
`Lightricks/LTX-2`'s pipeline signatures byte-for-byte: every public
pipeline method now takes `frame_rate: float` as a **mandatory
keyword-only** parameter (no default, matches upstream's required
`frame_rate=` kwarg). The legacy `fps=` kwarg is renamed throughout the
pipelines layer + immediate core helpers. Closes the audit gap
identified on [issue #6](https://github.com/dgrauet/ltx-2-mlx/issues/6).

### Changed

- **Breaking**: every pipeline public method (`generate*`,
  `generate_and_save`, `interpolate`, `retake`, `extend`,
  `generate_lipdub`) renames `fps: float = 24.0` →
  `frame_rate: float` (mandatory keyword-only). 8 pipelines affected:
  `TI2VidOneStagePipeline`, `TI2VidTwoStagesPipeline`,
  `TI2VidTwoStagesHQPipeline`, `DistilledPipeline`,
  `A2VidPipelineTwoStage`, `KeyframeInterpolationPipeline`,
  `ICLoraPipeline`, `HDRICLoraPipeline`. The 2 pipelines that derive
  `frame_rate` from the source video metadata (`RetakePipeline`,
  `LipDubPipeline`) still don't expose a public kwarg, but their
  internal `extend(...)` accepts `frame_rate` keyword-only too.

- **Breaking**: every CLI subcommand that previously accepted `--fps`
  now accepts `--frame-rate` and makes it **required**. Coverage
  changes: `--frame-rate` is now also required on `generate`
  (all four modes), `ic-lora`, and `hdr-ic-lora` — fixing the silent
  24fps default that was unintentionally baked into the temporal RoPE
  on those pipelines. `retake`, `extend`, and `lipdub` derive
  `frame_rate` from the source video and need no flag.

- **Breaking** (core helpers): `compute_video_positions`,
  `compute_audio_token_count`, `decode_and_stream`,
  `VideoConditionByKeyframeIndex` constructor, `_decode_and_save_video`,
  `combined_image_conditionings` all rename `fps` → `frame_rate`. The
  `fps` field on `RetakePipeline._SourceMeta` is renamed to
  `frame_rate`. `VideoInfo.fps` (ffprobe metadata carrier) **keeps
  its `fps` name** — it describes a source video file's metadata, not
  a pipeline parameter, and aligns with how ffprobe and upstream's
  `VideoPixelShape(fps=...)` data class label the concept.

### Migration

Python API callers:

```python
# 0.13.x
pipe.generate_and_save(prompt="...", num_frames=97, fps=24.0)
# 0.14.0
pipe.generate_and_save(prompt="...", num_frames=97, frame_rate=24.0)
```

`frame_rate` is mandatory and keyword-only — positional callers and
callers relying on the implicit 24.0 default will hit a `TypeError`.

CLI users:

```bash
# 0.13.x
ltx-2-mlx a2v --audio music.wav --fps 24 ...
# 0.14.0
ltx-2-mlx a2v --audio music.wav --frame-rate 24 ...

# 0.13.x silently assumed 24
ltx-2-mlx generate --two-stage -p "..." -o out.mp4
# 0.14.0 requires it explicitly
ltx-2-mlx generate --two-stage --frame-rate 24 -p "..." -o out.mp4
```

LTX-2.3 was trained at 24 fps. Values far from 24 drift out of the
temporal RoPE training distribution — quality risk. ComfyUI exposes
the same knob with the same caveat.

## [0.13.1] - 2026-05-13

Adds CLI phase markers around previously silent long-running stages
(Gemma load + prompt encode, transformer load, decoder load, video
decode). Addresses [issue #5](https://github.com/dgrauet/ltx-2-mlx/issues/5)
— a UX-only change with no impact on math, performance, or output.

### Added

- **CLI phase markers**. Each pipeline now prints `[phase] ...` /
  `[phase] done in X.Ys` lines to **stderr** around the five silent
  stages: loading the text encoder, encoding the prompt, loading the
  transformer, loading the decoders, and decoding video + audio +
  muxing. Output goes to stderr so stdout stays clean for callers that
  pipe pipeline output. Suppressed by `--quiet`.
- `BasePipeline.verbose` constructor parameter (default `True`)
  controlling the phase markers. CLI maps `verbose=not args.quiet` after
  pipeline construction. Programmatic users can set it either via the
  constructor or by assigning `pipe.verbose = False` after the fact.
- New `ltx_pipelines_mlx.utils.progress.phase()` context manager. Small
  helper used internally by `BasePipeline` to wrap silent stages; no-op
  when `verbose=False`. Public-ish utility, but mainly an internal
  building block.

## [0.13.0] - 2026-05-13

Removes the standalone `upscale` pipeline and its `upscale` CLI subcommand.
The pipeline was a local experimental addition with no upstream counterpart
in `Lightricks/LTX-2`, kept out of scope for this MLX port.

### Removed

- **`UpscalePipeline`** class and `upscale` CLI subcommand. The pipeline
  exposed the LTX neural latent upsampler (`spatial_upscaler_x2_v1_1` /
  `spatial_upscaler_x1_5_v1_0`) as a standalone VAE-encode → upsampler →
  VAE-decode tool with no DiT. It has no upstream equivalent and was only
  ever a local experiment. Removed from `ltx_pipelines_mlx.__all__`,
  `ltx-2-mlx --help`, and the maturity matrix.

  **What still works.** The neural latent upsampler module
  (`ltx_core_mlx/model/upsampler/`) is unchanged — it's a load-bearing
  component of every two-stage pipeline (`generate --two-stage` /
  `--two-stages-hq` / `--distilled`, `keyframe`, `ic-lora`, `hdr-ic-lora`,
  `a2v`, `lipdub`). Only the standalone CLI wrapper is gone.

  **Migration.** No upstream-iso replacement exists. If you relied on
  standalone latent upscaling, pin `ltx-2-mlx==0.12.1` or re-implement
  externally on top of `ltx_core_mlx.model.upsampler.LatentUpsampler`.

## [0.12.1] - 2026-05-13

Adds `LipDubPipeline` from upstream PR #212 as a new
**[experimental tier](docs/PIPELINE_MATURITY.md) pipeline**.

### Added

- **`LipDubPipeline`** + `lipdub` CLI subcommand. Two-stage lip-dubbing
  pipeline that takes a reference video providing both visual structure
  (via IC-LoRA reference latent appends) and target audio (via the audio
  VAE encoded as `AudioConditionByReferenceLatent`). Frame count is
  auto-derived from the reference video metadata (snapped to `8k+1`).
  Stage 2 keeps the stage-1 audio latent unchanged (`frozen=True`
  semantics) and only refines the video. Exported from
  `ltx_pipelines_mlx` as `LipDubPipeline`.

  **Known limitations** (model-level, not a port bug):
  - Output audio is a **VAE+vocoder reconstruction** of the reference
    audio, perceptually similar but not bit-identical to the input.
    Spectral artifacts can be audible on rich musical content. To
    preserve the original audio bit-exact, remux the source audio over
    the output mp4 via ffmpeg post-pipeline (loses fine lip-sync but
    preserves source music).
  - Lip-sync quality depends on prompt-audio alignment. Generic prompts
    produce visually plausible but loosely-synced output.
  - Uses `Lightricks/LTX-2.3-22b-IC-LoRA-LipDub` (currently `v0.9`).
    Pin a specific app version if depending on the current behaviour.

  Classified as **Experimental** in `docs/PIPELINE_MATURITY.md`. The
  CLI `--help` output marks it as `[experimental]`.

## [0.12.0] - 2026-05-13

Upstream sync from Lightricks/LTX-2 PR #212 — surfaces two **default value
changes**. No public API additions or removals; existing callers that pass
explicit values are unaffected, but consumers that relied on the previous
defaults should retest before upgrading.

### Changed (potentially breaking for callers relying on defaults)

- **`TilingConfig.default()`** spatial config bumped from `512×512` /
  `64` overlap to **`768×768` / `64` overlap**; temporal config from
  `64` frames / `24` overlap to **`80` frames / `24` overlap**. Matches
  upstream's tradeoff (fewer tile boundaries at production resolutions).
  Our internal pipelines do not call `TilingConfig.default()` directly,
  but external consumers using this helper will get the new defaults.
- **`precompute_rope_freqs` default `rope_type`** switched from
  `"interleaved"` to `"split"`. All in-repo call sites pass `rope_type=`
  explicitly so this is a no-op for our pipelines, but external consumers
  that called `precompute_rope_freqs` without specifying `rope_type` will
  see different output (the LTX-2.3 checkpoints all use SPLIT — upstream
  switched the default to match reality).

### Added

- `AudioConditionByReferenceLatent` now exported from
  `ltx_core_mlx.conditioning` and `ltx_core_mlx.conditioning.types`
  (was previously importable only from the leaf module).

## [0.11.1] - 2026-05-13

Additive upstream sync from Lightricks/LTX-2 PR #212 (merged upstream 2026-05-11),
plus a low-risk internal refactor. No public default values change in this
release.

### Added

- `iclora_utils.py` module exposing the shared IC-LoRA helpers from upstream
  PR #212: `read_lora_reference_downscale_factor`,
  `downsample_mask_video_to_latent`, `append_ic_lora_reference_video_conditionings`.
  Used by ic-lora and the upcoming lip-dub pipeline.
- `AudioConditionByReferenceLatent` conditioning type for appending
  reference audio tokens with negative-shifted RoPE positions. Audio-side
  mirror of `VideoConditionByReferenceLatent`.
- `ltx_core_mlx.components.diffusion_steps` — `EulerDiffusionStep`,
  `Res2sDiffusionStep`, `EulerCfgPpDiffusionStep` primitives + protocol +
  `_get_ancestral_step` helper. Available as standalone primitives;
  existing samplers still inline this math (no behaviour change for
  current pipelines).
- `ltx_core_mlx.utils.diffusion` — `to_velocity` / `to_denoised` helpers
  matching upstream.

### Changed

- `ic_lora.py` refactored to delegate the IC-LoRA reference video
  conditioning to `iclora_utils.append_ic_lora_reference_video_conditionings`.
  -151 LOC net. Public API unchanged. Bit-exact regression validated
  against the pre-refactor Q20 baseline (SHA256 match).

## [0.11.0] - 2026-05-11

### Added
- `--start-strength` / `--end-strength` flags on `keyframe` CLI to expose
  per-keyframe conditioning strength (upstream-iso surface, default `1.0`).
- Static-scene I2V recipe documentation (ic-lora + canny control video),
  validated end-to-end on Phoenix Q15.
- Standalone `upscale` pipeline + CLI subcommand (VAE encode → neural
  upsampler → VAE decode, no DiT).
- Modality tiling (`--tile-frames N --tile-spatial M`) on `generate` (one-stage /
  --two-stage / --two-stages-hq), `a2v`, `keyframe`.

### Fixed
- `ic_lora` upstream-iso tightening: fix `UnboundLocalError` introduced by an
  earlier edit, 4 API alignments with upstream `ICLoraPipeline._create_conditionings`.
- Default `stg_scale=1.0` restored on standard pipelines (matches upstream
  `LTX_2_3_PARAMS`). Was hardcoded `0.0` for 32 GB Mac compat — that's now
  the user's choice, not the default.
- Strip appended keyframe tokens before unpatchify across all pipelines (fix
  for multi-anchor I2V at `frame_idx > 0`).
- Multi-image conditioning propagated to all I2V pipelines; upstream-iso
  `combined_image_conditionings` helper used end-to-end.
- Metal watchdog: drop wasteful Gemma re-load in `load()` methods (Gemma was
  being loaded twice — once before forward, once before DiT — causing 7.5 GB
  heap thrash). Production-quality generation on M2 Pro 32 GB now passes
  under sustained system contention.

### Changed
- `media_io.py` ported 1:1 upstream-iso (replaces the previous divergent
  shim).
- `prepare_image_for_encoding` applies H.264 CRF round-trip (matches
  upstream's training-distribution pre-processing).
- `metal_watchdog.py` removed; auto eval gating (per-layer Gemma /
  per-block connector) supersedes the opt-in `LTX2_METAL_WATCHDOG_GUARD` env var.

## [0.10.0] - 2026-05-08

### Removed (BREAKING)
- `ImageToVideoPipeline` removed — no upstream equivalent. I2V is now
  supported on every public pipeline via `image=` kwarg / `--image` CLI flag
  (consistent with upstream's `combined_image_conditionings` pattern).

## [0.9.x] - 2026-05 (pre-isomorphism patch series)

Series of bit-exact iso-tightening patches across pipelines (T2V, I2V, A2V,
keyframe, ic-lora, hdr-ic-lora). Detailed per-commit history in `git log v0.9.0..v0.9.8`.

## [0.x] - earlier (foundations)

Initial MLX port of LTX-2.3 from Lightricks/LTX-2 reference. Bring-up of
video VAE, audio VAE + vocoder + BWE, DiT transformer, Gemma 3 12B text
encoder, conditioning system, two-stage pipelines, distilled mode.
