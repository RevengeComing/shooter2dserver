try:
    import orjson as json
except:
    try:
        import ujson as json
    except:
        import json


class Request:
    __slots__ = ["body", "action", "payload"]

    def __init__(self, body):
        self.body = body
        self._decode()

    def _decode(self):
        print(self.body)
        try:
            data = json.loads(self.body)
            self.action = data["action"]
            self.payload = data["payload"]
        except:
            print("koskesh ridi ba in datat")


class Response:
    def __init__(self, data):
        self.data = data

    def __call__(self):
        return json.dumps(self.data)
