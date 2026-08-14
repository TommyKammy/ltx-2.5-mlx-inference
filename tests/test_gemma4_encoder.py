import json
from types import SimpleNamespace

import mlx.core as mx

from ltx_core_mlx.text_encoders.gemma.encoders.base_encoder import GemmaLanguageModel
from ltx_pipelines_mlx.utils.blocks import PromptEncoder


def test_load_maps_unified_config_to_mlx_lm_gemma4(tmp_path, monkeypatch):
    (tmp_path / "config.json").write_text(json.dumps({"model_type": "gemma4_unified"}))
    captured = {}

    def fake_load(path, model_config=None):
        captured["path"] = path
        captured["model_config"] = model_config
        return object(), object()

    monkeypatch.setattr("mlx_lm.load", fake_load)
    encoder = GemmaLanguageModel()
    encoder.load(str(tmp_path))

    assert captured == {"path": str(tmp_path), "model_config": {"model_type": "gemma4"}}


class _FakeEmbedding:
    def __call__(self, token_ids):
        return mx.zeros((*token_ids.shape, 4))


class _FakeGemma4Layer:
    def __init__(self, index, layer_type="full_attention"):
        self.index = index
        self.layer_type = layer_type
        self.received_shared_kv = None

    def __call__(self, h, mask, cache, per_layer_input=None, shared_kv=None, offset=None):
        self.received_shared_kv = shared_kv
        return h + (self.index + 1), f"kv-{self.index}", self.index


class _FakeGemma4Inner:
    def __init__(self):
        self.embed_tokens = _FakeEmbedding()
        self.embed_scale = 2.0
        self.layers = [_FakeGemma4Layer(0), _FakeGemma4Layer(1), _FakeGemma4Layer(2)]
        self.previous_kvs = [0, 1, 0]
        self.window_size = 4096


def test_gemma4_hidden_states_preserve_shared_kv_dependencies():
    inner = _FakeGemma4Inner()
    encoder = GemmaLanguageModel()
    encoder._model = SimpleNamespace(language_model=SimpleNamespace(model=inner))
    token_ids = mx.array([[1, 2]])
    attention_mask = mx.ones_like(token_ids)

    states = encoder.get_all_hidden_states(token_ids, attention_mask)
    mx.eval(*states)

    assert len(states) == 4
    assert mx.array_equal(states[0], mx.zeros((1, 2, 4)))
    assert mx.array_equal(states[1], mx.ones((1, 2, 4)))
    assert mx.array_equal(states[2], mx.ones((1, 2, 4)) * 3)
    assert mx.array_equal(states[3], mx.ones((1, 2, 4)) * 6)
    assert inner.layers[2].received_shared_kv == "kv-0"


def test_prompt_encoder_autodetects_bundled_ltx25_gemma(tmp_path):
    bundled = tmp_path / "gemma4-12b-ltx-v1"
    bundled.mkdir()
    (bundled / "config.json").write_text("{}")

    encoder = PromptEncoder(tmp_path)

    assert encoder.gemma_model_id == str(bundled)


def test_prompt_encoder_preserves_explicit_gemma_path(tmp_path):
    bundled = tmp_path / "gemma4-12b-ltx-v1"
    bundled.mkdir()
    (bundled / "config.json").write_text("{}")

    encoder = PromptEncoder(tmp_path, gemma_model_id="custom/gemma")

    assert encoder.gemma_model_id == "custom/gemma"
