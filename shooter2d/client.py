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

    def act_login(self):
        asyncio.ensure_future(self.login(), loop=asyncio.get_event_loop())

    async def login(self):
        await self.websocket.send(json.dumps(
            {"action": "join", "payload": {"token": self.token}}))

    def act_move(self, velocity):
        asyncio.ensure_future(self.move(velocity),
                              loop=asyncio.get_event_loop())

    async def move(self, velocity):
        data = {
            "action": "move",
            "payload": {
                "velocity": {"x": velocity[0], "y": velocity[1]}
            }
        }
        await self.websocket.send(json.dumps(data))

    def act_shoot(self, direction):
        asyncio.ensure_future(self.shoot(direction),
                              loop=asyncio.get_event_loop())

    async def shoot(self, direction):
        await self.websocket.send(json.dumps({
            {"action": "shoot", "payload": {
                "direction": direction}}
        }))

    def act_direction(self, direction):
        asyncio.ensure_future(self.move(direction),
                              loop=asyncio.get_event_loop())

    async def direction(self, direction):
        await self.websocket.send(json.dumps({
            {"action": "direction", "payload": {
                "direction": direction}}
        }))

    async def data_recieved(self):
        while self.websocket.open:
            try:
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
            except asyncio.streams.IncompleteReadError:
                print("WTF")

        print("Connection closed ... try again ...")

    async def on_confirm(self, payload):
        print("on_confirm event triggered")

    async def on_update(self, payload):
        print("on_update event triggered %s payload" % payload)

    async def on_config(self, payload):
        print("on_config event triggered")

    def _get_token_and_ws_address(self):
        resp = requests.post(self.address, json={"username": self.username})
        return resp.json()

    def _connect(self, token, ws_address):
        asyncio.get_event_loop().run_until_complete(self.connect())
        asyncio.ensure_future(self.data_recieved(),
                              loop=asyncio.get_event_loop())
