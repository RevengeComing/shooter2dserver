
import click

from shooter2d.server import create_app
from shooter2d.game import Game, Player
from shooter2d.request import Request, Response

from sanic.websocket import WebSocketProtocol

from .config import Config


@click.group()
def cli():
    print("Command Line")


@cli.command()
def dev():
    game = Game(Config.Game.MAP_HEIGHT, Config.Game.MAP_WIDTH)
    create_app(game, Player, Request, Response, Config.Server).run(
        host="localhost", port=8000)


if __name__ == "__main__":
    cli()
