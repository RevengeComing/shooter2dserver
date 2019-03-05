from random import randint
from .player import Player


def process_join_game(game, data=None, player=None):
    new_player_x, new_player_y = get_new_player_position(game)
    player = Player(new_player_x, new_player_y)
    game.add_player(player)
    return {"request": "join_game", "status": "done", "current_position_x": player.x, "current_position_y": player.y}


def process_get_map(game, data=None, player=None):
    return {"request": "get_map", "map": game.map}


def process_move(game, data, player):
    player.move(data["speed_x"], data["speed_y"])
    return {"request": "process_move", "status": "done", "current_position_x": player.x, "current_position_y": player.y}


def process_set_name(game, data, player):
    player.set_name(data["name"])
    return {"request": "set_name", "status": "done", "player_name": player.name}


def get_new_player_position(game):
    new_player_position_x = randint(0, game.height)
    new_player_position_y = randint(0, game.width)
    for player in game.players:
        if player.x == new_player_position_x and player.y == new_player_position_y:
            return get_new_player_position(game)

    return new_player_position_x, new_player_position_y


actions = {"move": process_move, "get_map": process_get_map, "set_name": process_set_name,
           "join_game": process_join_game}
