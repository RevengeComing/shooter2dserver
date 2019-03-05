try:
    import orjson as json
except:
    try:
        import ujson as json
    except:
        import json


class Request:
    __slots__ = ["body", "action", "action_data"]

    def __init__(self, body):
        self.body = body
        self._decode()

    def _decode(self):
        data = json.loads(self.body)
        self.action = data["action"]
        self.action_data = data["action_data"]


class Response:
    def __init__(self, data):
        self.data = data

    def __call__(self):
        return json.dumps(self.data)
