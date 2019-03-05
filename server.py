import time
import asyncio


from sanic import Sanic
from sanic.response import json
from sanic.websocket import WebSocketProtocol
from game import Game, Player
from request import Request, Response


def create_app(game: Game, player_class, request_class, response_class) -> Sanic:
    app = Sanic()

    connections = set()

    @app.websocket("/game")
    async def feed(request, ws):
        ws = SanicWebSocket(ws)
        connections.add(ws)
        player = None

        try:
            while True:
                data = await ws.recv()
                request = request_class(data)
                if data is not None:
                    if player:
                        data = game.process_request(player, request)
                    else:
                        data, player = game.process_request(None, request)

                    response = response_class(data)
                    await ws.send(response())
        finally:
            game.remove_player(player)

    async def update():
        while True:
            now = time.time()
            info = game.get_info()
            response = response_class(info)
            for connection in connections:
                await connection.send(response())
            print("sent in %s time", time.time() - now)
            asyncio.sleep(0.1)

    async def garbage_collector_task():
        while True:
            asyncio.sleep(60)
            game.run_garbage_collector()

    app.add_task(update())
    app.add_task(garbage_collector_task())
    return app


if __name__ == "__main__":
    game = Game(1000, 1000)

    create_app(game, Player, Request, Response).run(host="0.0.0.0", port=8000, protocol=WebSocketProtocol)
