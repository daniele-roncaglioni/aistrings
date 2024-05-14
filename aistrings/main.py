from models.openai import OpenAIModel

MODEL_PROVIDERS = {
    'openai': OpenAIModel
}


class AiStrings:
    def __init__(self, provider_name: str, model_name: str):
        assert provider_name in MODEL_PROVIDERS.keys()
        self.model = MODEL_PROVIDERS[provider_name](model_name=model_name)
        self.cumulative_cost = 0
        self.history = []

    def reset_cost(self):
        self.cumulative_cost = 0

    def log_cost(self):
        print(
            "------------\n"
            "hello"
        )

    def summarize(self):
        pass

    def answer(self):
        pass

    def is_factual(self):
        pass

    def make_verbose(self):
        pass

    def expand(self):
        pass

    def correct_grammar(self):
        pass

    def detect_lang(self):
        pass

    def split(self):
        pass

    def replace(self):
        pass
