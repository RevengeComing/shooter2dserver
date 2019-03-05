from random import randint
from .player import Player
import jwt
from shooter2d.cmd.config import Config
from shooter2d.math import nearly_equal


def process_join(game, payload=None, player=None):
    username = jwt.decode(payload['token'].encode(), Config.Server.SECRET_KEY, algorithms=[
                          'HS256'])['username']
    new_player_x, new_player_y = get_new_player_position(game)
    player = Player(new_player_x, new_player_y, username)
    game.add_player(player)
    return {"request": "join_game", "status": "done", "current_position_x": player.x, "current_position_y": player.y}, player


def process_get_map(game, payload=None, player=None):
    return {"request": "get_map", "map": game.map}


def process_move(game, payload, player):
    if nearly_equal(payload['speed_x'] ** 2 + payload['speed_y'] ** 2, 1):
        player.move(payload["speed_x"], payload["speed_y"])
    return {"request": "process_move", "status": "done"}


def process_set_name(game, payload, player):
    player.set_name(payload["name"])
    return {"request": "set_name", "status": "done", "player_name": player.name}


def get_new_player_position(game):
    new_player_position_x = randint(0, game.height)
    new_player_position_y = randint(0, game.width)
    for player in game.players:
        if player.x == new_player_position_x and player.y == new_player_position_y:
            return get_new_player_position(game)

    return new_player_position_x, new_player_position_y


actions = {"move": process_move, "get_map": process_get_map,
           "join": process_join}
