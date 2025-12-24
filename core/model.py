from smolagents import LiteLLMModel

_model = None

def get_model():
    global _model
    if _model is None:
        _model = LiteLLMModel(
            model_id="ollama/krith/qwen2.5-7b-instruct:IQ4_XS"
        )
    return _model
