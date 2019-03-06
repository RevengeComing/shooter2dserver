import asyncio
import websockets
import requests
import orjson as json


class Shooter2DClinet():
    def __init__(self, address, username):
        self.address = address
        self.username = username
        data = self._get_token_and_ws_address()
        self.token, self.ws_address = data['token'], data['websocket']
        self.player = None
        self._connect(self.token, self.ws_address)

    async def connect(self):
        self.websocket = await websockets.connect(self.ws_address)

    async def login(self):
        await self.websocket.send(json.dumps(
            {"action": "login", "payload": {"token": self.token}}))

    async def move(self, velocity):
        pass

    async def shoot(self, direction):
        pass

    async def direction(self, direction):
        pass

    async def data_recieved(self):
        while self.websocket.open:
            data = await self.websocket.recv()
            data = json.loads(data)
            data_type = data.get('type')
            if data_type:  # confirm, update, config
                if data_type == "update":
                    await self.on_update(data.get("payload"))
                elif data_type == "confirm":
                    await self.on_confirm(data.get("payload"))
                elif data_type == "config":
                    await self.on_config(data.get('payload'))

        print("Connection closed ... try again ...")

    async def on_confirm(self, payload):
        print("on_confirm event triggered")

    async def on_update(self, payload):
        print("on_update event triggered")

    async def on_config(self, payload):
        print("on_config event triggered")

    def _get_token_and_ws_address(self):
        resp = requests.post(self.address, json={"username": self.username})
        return resp.json()

    def _connect(self, token, ws_address):
        asyncio.get_event_loop().run_until_complete(self.connect())
        asyncio.get_event_loop().run_until_complete(self.data_recieved())
