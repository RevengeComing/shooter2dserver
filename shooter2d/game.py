from random import randint


def process_join_game(player, data, game):
    player = player_class.create_player()
    game.add_player(player)
    return {"request": "join_game", "status": "done", "current_position": player.position}


def process_get_map(player, data, game):
    return {"request": "get_map", "map": game.map}


def process_move(player, data, game):
    player.move(data["direction"])
    return {"request": "process_move", "status": "done", "current_position": player.position}


def process_set_name(player, data, game):
    player.set_name(data["name"])
    return {"request": "set_name", "status": "done", "player_name": player.name}


actions = {"move": process_move, "get_map": process_get_map, "set_name": process_set_name, "join_game": process_join_game}



class Player:
    @staticmethod
    def create_player(game):
        p = Player()
        p.x = x
        p.y = y
        return p

    def set_name(self):
        self.name = name

    def move(self, direction, undo=False):
        pass


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
        return actions[request.action](player, request.action_data, self)

    def get_info(self):
        return {}

    def json_map(self):
        return []


def _create_empty_map(height, width):
    return []
