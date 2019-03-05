import orjson as json
from random import randint

from .player import Player
from .actions import actions


class Game:
    def __init__(self, height, width):
        self.players = set()
        self.connections = set()
        self.height = height
        self.width = width
        self.map = _create_empty_map(height, width)
        self.l_shape_walls = _create_walls(self.width, self.height)
        self.circle_shape_walls = _create_walls(self.width, self.height)
        self.single_point_walls = _create_walls(self.width, self.height)

    def add_player(self, player_instance: Player):
        self.players.add(player_instance)

    def remove_player(self, player_instance: Player):
        self.players.remove(player_instance)

    def process_request(self, player_instance: Player, request):
        return actions[request.action](self, request.payload, player_instance)

    def get_info(self):
        map_info = []
        for player in self.players:
            player_info = {
                "hp": player.health,
                "position_x": player.x,
                "position_y": player.y,
                "speed_x": player.speed_x,
                "speed_y": player.speed_y,
                "name": player.name,
            }
            map_info.append(player)
        return map_info

    def clock(self):
        pass


def _create_empty_map(height, width):
    return []


def _create_walls(max_width, max_height):
    numbers = randint(30, 50)
    positions = set()
    for i in range(numbers):
        positions.add((randint(0, max_width), randint(0, max_height)))

    return positions
