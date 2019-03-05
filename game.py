from random import randint


def process_join_game(player, data, game):
    player = player_class.create_player()
    game.add_player(player)
    return {"request": "join_game", "status": "done", "current_position": player.position}


def process_get_map(player, data, game):
    return {"request": "get_map", "map": game.map}


def process_move(player, data, game):
    player.move(data["direction"])
    if Cell.has_location_owner(player.x, player.y, game) and not game.safe_mode:
        player.move(data["direction"], undo=True)
        return {"request": "process_move", "status": "failed", "current_position": player.position}
    return {"request": "process_move", "status": "done", "current_position": player.position}


def process_set_name(player, data, game):
    player.set_name(data["name"])
    return {"request": "set_name", "status": "done", "player_name": player.name}


actions = {"move": process_move, "get_map": process_get_map, "set_name": process_set_name, "join_game": process_join_game}


class Cell:
    def __init__(self, x, y):
        self.owner = None

    def change_owner(self, owner):
        self.owner = owner

    def has_owner(self):
        return self.owner is not None

    @staticmethod
    def get_free_cell(game, retries=3):
        rand_width = randint(0, game.width)
        rand_height = randint(0, game.height)
        cell = game.map[rand_height][rand_width]

        if cell.has_owner():
            cell.change_owner(p)
        else:
            if retries == 0:
                raise Exception("Retries for getting empty cell exceeded")

            cell = Cell.get_free_cell()

        return cell, rand_width, rand_height

    @staticmethod
    def has_location_owner(x, y, game):
        cell = game.map[x][y]
        return cell.has_owner()


class Player:
    @staticmethod
    def create_player(game):
        p = Player()
        cell, x, y = get_free_cell(game)
        p.x = x
        p.y = y
        return p

    def set_name(self):
        self.name = name

    def move(self, direction, undo=False):
        multiplier = 1
        if undo:
            multiplier = -1

        if direction == "left":
            self.x -= 1 * multiplier
        elif direction == "right":
            self.x += 1 * multiplier
        elif direction == "top":
            self.y -= 1 * multiplier
        elif direction == "down":
            self.y += 1 * multiplier


class Game:
    def __init__(self, height, width):
        self.players = set()
        self.connections = set()
        self.height = height
        self.width = width
        self.map = _create_empty_map(height, width)
        self.safe_mode = True

    def add_player(self, player: Player):
        self.players.add(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def process_request(self, player: Player, request):
        return actions[request.action](player, request.action_data, self)

    def get_info(self):
        return {
            "players": [{"x": player.x, "y": player.y, "name": player.name} for player in self.players],
            "map": self.json_map(),
            "garbage_collected": False,
        }

    def json_map(self):
        _map = []
        for row in self.map:
            row = []
            for cell in row:
                row.append({"owner": cell.owner})
            _map.append(row)
        return _map

    def run_garbage_collector(self):
        pass


def _create_empty_map(height, width):
    map = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(Cell(j, i))
        map.append(row)
    return map
