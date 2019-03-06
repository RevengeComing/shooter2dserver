import orjson as json
import time
from random import randint

from .player import Player
from .actions import actions
from .bullet import Bullet


class Game:
    def __init__(self, config):
        self.players = set()
        self.connections = set()
        self.bullets = set()
        self.height = config.MAP_HEIGHT
        self.width = config.MAP_WIDTH
        self.bullet_pain = config.BULLET_PAIN
        self.map = _create_empty_map(config.MAP_HEIGHT, config.MAP_WIDTH)
        self.l_shape_walls = _create_walls(self.width, self.height)
        self.circle_shape_walls = _create_walls(self.width, self.height)
        self.single_point_walls = _create_walls(self.width, self.height)
        self.app = None

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
                "type": "player",
                "hp": player.health,
                "position": {"x": player.x, "y": player.y},
                "velocity": {"x": player.velocity_x, "y": player.velocity_y},
                "direction": player.direction,
                "name": player.name,
            }
            map_info.append(player_info)

        for bullet in self.bullets:
            bullet_info = {
                'type': "bullet",
                "position": {"x": bullet.x, "y": bullet.y},
                "direction": bullet.direction,
                "speed": bullet.speed,
            }
        return map_info

    def shoot(self, player, direction):
        bullet = Bullet(player, direction)
        self.bullets.add(bullet)

    def update(self):
        now = time.time()
        for player in self.players:
            player.update()

        for bullet in self.bullets:
            bullet.update()

            for player in self.players:
                if bullet.is_collide_with(player):
                    self.bullets.remove(bullet)
                    player.hp -= self.bullet_pain
                    break

                if bullet.expired_at < now:
                    self.bullets.remove(bullet)


def _create_empty_map(height, width):
    return []


def _create_walls(max_width, max_height):
    numbers = randint(30, 50)
    positions = set()
    for i in range(numbers):
        positions.add((randint(0, max_width), randint(0, max_height)))

    return positions
