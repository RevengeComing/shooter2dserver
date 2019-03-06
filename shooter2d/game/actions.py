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
    return {
        "type": "config",
        "payload": {
            "configs": {
                "bullet_speed": Config.Game.BULLET_SPEED,
                "bullet_ttl": Config.Game.BULLET_TTL,
                "map_height": Config.Game.MAP_HEIGHT,
                "map_width": Config.Game.MAP_WIDTH,
                "player_speed": Config.Game.PLAYER_SPEED,
                "max_blind_range": Config.Game.MAX_BLINK_RANGE,
            },
        },
    }, player


def process_get_map(game, payload=None, player=None):
    return {"type": "get_map", "payload": {"map": game.map}}


def process_move(game, payload, player):
    if (nearly_equal(payload['velocity']['x'] ** 2 + payload['velocity']['y'] ** 2, 1) or
            (payload['velocity']['x'] == 0 and payload['velocity']['y'] == 0)):
        player.move(payload["velocity"]["x"], payload["velocity"]["y"])
        return {"type": "confirm", "payload": {"move": "done"}}
    return {"type": "confirm", "payload": {"move": "failed"}}


def process_direction(game, payload, player):
    player.direction = payload['direction']
    return {"type": "confirm", "playload": {"direction": "done"}}


def process_shoot(game, payload, player):
    direction = payload['direction']
    if player.has_ammo():
        game.shoot(player, direction)
        return {"type": "confirm", "payload": {"shoot": "done"}}
    return {"type": "confirm", "payload": {"shoot": "failed"}}


def get_new_player_position(game):
    new_player_position_x = randint(0, game.height)
    new_player_position_y = randint(0, game.width)
    for player in game.players:
        if player.x == new_player_position_x and player.y == new_player_position_y:
            return get_new_player_position(game)

    return new_player_position_x, new_player_position_y


actions = {"move": process_move, "get_map": process_get_map,
           "join": process_join, "shoot": process_shoot, "direction": process_direction}
