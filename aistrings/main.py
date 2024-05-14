import datetime
from typing import TypedDict, List

from models.base import BaseModel
from models.openai import OpenAIModel

MODEL_PROVIDERS = {
    'openai': OpenAIModel
}


class AiStrings:
    def __init__(self, provider_name: str, model_name: str):
        assert provider_name in MODEL_PROVIDERS.keys()
        self.model: BaseModel = MODEL_PROVIDERS[provider_name](model_name=model_name)
        self.cumulative_cost = 0
        self.history: List[HistoryItem] = []

    def reset_cost(self):
        self.cumulative_cost = 0

    def log(self, action_type: str, input_str: str, output_str: str, cost: float):
        self.history.append(
            {
                "action_type": action_type,
                "input_str": input_str,
                "output_str": output_str,
                "cost": cost,
                "timestamp": datetime.datetime.now()
            }
        )
        self.cumulative_cost += cost

    def log_history(self):
        print("History")
        print(f"----------------------")
        for h in self.history:
            print(
                f"  Action: {h['action_type']}\n"
                f"  Input: {h['input_str']}\n"
                f"  Output: {h['output_str']}\n"
                f"  Cost: {h['cost']}\n"
                f"  Time: {h['timestamp']}\n"
            )
        print(f"Total Cost: {self.cumulative_cost}")
        print(f"----------------------\n")

    def summarize(self, text: str):
        messages = [
            {
                "role": "user",
                "content": f"Summarize the the text, be brief, don't repeat yourself and return the summary only. Text: {text} "
            },
        ]
        response, cost = self.model(messages=messages, response_type="text")
        self.log(action_type='summarize', input_str=text, output_str=response, cost=cost)
        return response

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


class HistoryItem(TypedDict):
    action_type: str
    input_str: str
    output_str: str
    cost: float
    timestamp: datetime.datetime
