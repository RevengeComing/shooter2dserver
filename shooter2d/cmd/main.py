
import click

from shooter2d.constants import GAME_MAP_HEIGHT, GAME_MAP_WIDTH
from shooter2d.server import create_app
from shooter2d.game import Game, Player
from shooter2d.request import Request, Response

from sanic.websocket import WebSocketProtocol


@click.group()
def cli():
    print("Command Line")


@cli.command()
def dev():
    game = Game(GAME_MAP_HEIGHT, GAME_MAP_WIDTH)
    create_app(game, Player, Request, Response).run(host="0.0.0.0", port=8000, protocol=WebSocketProtocol)


if __name__ == "__main__":
    cli()
