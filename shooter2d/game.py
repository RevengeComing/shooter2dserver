from random import randint

from shooter2d.constants import GAME_MAP_WIDTH, GAME_MAP_HEIGHT


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
    new_player_position_x = randint(GAME_MAP_WIDTH)
    new_player_position_y = randint(GAME_MAP_HEIGHT)
    for player in game.players:
        if player.x == new_player_position_x and player.y == new_player_position_y:
            return get_new_player_position(game)

    return new_player_position_x, new_player_position_y


actions = {"move": process_move, "get_map": process_get_map, "set_name": process_set_name,
           "join_game": process_join_game}


class Player:
    def __init__(self, x, y, name=""):
        self.x = x
        self.y = y
        self.name = name
        self.speed_x = 0
        self.speed_y = 0

    def set_name(self, name):
        self.name = name

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def set_speed(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y


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
        return {}

    def json_map(self):
        return []

    def clock(self):
        pass


def _create_empty_map(height, width):
    return []
