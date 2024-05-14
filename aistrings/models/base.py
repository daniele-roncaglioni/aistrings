class BaseModel:
    @staticmethod
    def request_price(response):
        raise NotImplemented

    def __call__(self, *args, **kwargs):
        raise NotImplemented
