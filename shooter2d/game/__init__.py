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
        return actions[request.action](self, request.action_data, player_instance)

    def get_info(self):
        map_info = dict()

        for player_instance in self.players:
            map_info["player" + player_instance.name] = {"hp": player_instance.health,
                                                         "position_x": player_instance.x,
                                                         "position_y": player_instance.y,
                                                         "speed_x": player_instance.speed_x,
                                                         "speed_y": player_instance.speed_y}
        return json.dumps(map_info)

    def clock(self):
        pass


def _create_empty_map(height, width):
    return []


def _create_walls(max_width, max_height):
    numbers = randint(30, 50)
    positions = set()
    for i in range(numbers):
        positions.add((randint(max_width), randint(max_height)))

    return positions
