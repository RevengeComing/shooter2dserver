import asyncio
import time

import jwt

from sanic import Sanic
from sanic.response import json

from .game import Game


def create_app(game: Game, player_class, request_class, response_class, config) -> Sanic:
    app = Sanic()

    connections = set()

    @app.websocket("/game")
    async def feed(request, ws):
        connections.add(ws)
        player = None

        try:
            while True:
                data = await ws.recv()
                if data is not None:
                    request = request_class(data)
                    if player:
                        data = game.process_request(player, request)
                    else:
                        data, player = game.process_request(player, request)

                    response = response_class(data)
                    await ws.send(response())
        finally:
            game.remove_player(player)

    @app.route("/join", methods=["POST"])
    async def join(request):
        username = request.json.get("username") or request.form.get("username")
        return jwt.encode({'username': username, "server_address": "localhost:8000/game"},
                          config.SECRET_KEY, algorithm='HS256')

    async def clock():
        while True:
            now = time.time()
            info = game.get_info()
            response = response_class(info)
            for connection in connections:
                try:
                    await connection.send(response())
                except ConnectionError:
                    connections.remove(connection)
            print("Clock in %f" % (time.time() - now))
            await asyncio.sleep(0.1)

    app.add_task(clock())
    return app
