import orjson as json
from .player import Player
from .actions import actions


class Game:
    def __init__(self, height, width):
        self.players = set()
        self.connections = set()
        self.height = height
        self.width = width
        self.map = _create_empty_map(height, width)

    def add_player(self, player: Player):
        self.players.add(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def process_request(self, player: Player, request):
        return actions[request.action](self, request.action_data, player)

    def get_info(self):
        map_info = dict()

        for player in self.players:
            map_info[player.name] = {"hp": player.health,
                                     "position_x": player.x,
                                     "position_y": player.y,
                                     "speed_x": player.speed_x,
                                     "speed_y": player.speed_y}
        return json.dumps(map_info)

    def clock(self):
        pass


def _create_empty_map(height, width):
    return []
