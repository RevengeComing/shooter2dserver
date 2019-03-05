import asyncio
import time

import jwt

from sanic import Sanic
from sanic.response import json

from .game import Game


async def send_data(connection, data):
    await connection.send(data)


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

    @app.route("/login", methods=["POST"])
    async def login(request):
        username = request.json.get("username") or request.form.get("username")
        server_address = config.SCHEMA + "://" + \
            config.DOMAIN + ":" + config.PORT + "/game"
        return json({"token": jwt.encode({'username': username},
                                         config.SECRET_KEY, algorithm='HS256'), "websocket": server_address})

    @app.middleware('response')
    async def add_response_header(request, response):
        response.headers['Access-Control-Allow-Origin'] = "*"

    async def clock():
        while True:
            now = time.time()
            info = game.get_info()
            response = response_class(info)
            data = response()

            for connection in connections:
                app.add_task(send_data(connection, data))
            print("Clock in %f" % (time.time() - now))
            await asyncio.sleep(0.1)

    app.add_task(clock())
    return app
