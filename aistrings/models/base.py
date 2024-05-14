from typing import List, Literal


class BaseModel:
    @staticmethod
    def request_price(response):
        raise NotImplemented

    def __call__(self, messages: List[dict], response_type: Literal["text", "json_object"]):
        raise NotImplemented
