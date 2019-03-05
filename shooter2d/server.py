import asyncio
import time

import jwt

import websockets
from sanic import Sanic
from sanic.response import json

from .game import Game


async def send_data(connection, data, connections):
    try:
        await connection.send(data)
    except websockets.exceptions.ConnectionClosed:
        connections.remove(connection)


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
            if player:
                game.remove_player(player)

        return json({"status": "end"})

    @app.route("/login", methods=["POST"])
    async def login(request):
        username = request.json.get("username") or request.form.get("username")
        server_address = config.SCHEMA + "://" + \
            config.DOMAIN + ":" + str(config.PORT) + "/game"
        return json({"token": jwt.encode({'username': username},
                                         config.SECRET_KEY, algorithm='HS256'), "websocket": server_address})

    @app.middleware('response')
    async def add_response_header(request, response):
        response.headers['Access-Control-Allow-Origin'] = "*"

    async def update():
        while True:
            now = time.time()
            game.update()
            info = game.get_info()
            response = response_class(info)
            data = response()

            for connection in connections:
                app.add_task(send_data(connection, data, connections))
            print("update in %f" % (time.time() - now))
            await asyncio.sleep(0.1)

    app.add_task(update())
    return app
