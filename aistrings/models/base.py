from typing import List


class BaseModel:
    @staticmethod
    def request_price(response):
        raise NotImplemented

    def __call__(self, messages: List[dict], response_type: str):
        raise NotImplemented
