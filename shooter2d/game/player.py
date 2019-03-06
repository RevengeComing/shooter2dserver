from math import sqrt
import time

from .clock import clocked_function

from ..cmd.config import Config


class Player:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.velocity_x = 0
        self.velocity_y = 0
        self.health = 100
        self.ammo_count = 5
        self.has_blink = True
        self.direction = 0
        self.radius = Config.Game.PLAYER_RADIUS
        self.last_update = time.time()

    def set_name(self, name):
        self.name = name

    def move(self, velocity_x, velocity_y):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def add_ammo(self, count):
        self.ammo_count += count

    def has_ammo(self):
        return self.ammo_count > 0

    def shoot_ammo(self):
        self.ammo_count -= 1

    def add_hp(self, hp_amount: int):
        self.health = max(100, self.health + hp_amount)

    def update(self):
        now = time.time()
        dt = now - self.last_update

        self.x += self.velocity_x * dt * 1000 * Config.Game.PLAYER_SPEED
        if self.x > Config.Game.MAP_WIDTH:
            self.x = Config.Game.MAP_WIDTH
        elif self.x < 0:
            self.x = 0

        self.y += self.velocity_y * dt * 1000 * Config.Game.PLAYER_SPEED
        if self.y > Config.Game.MAP_HEIGHT:
            self.y = Config.Game.MAP_HEIGHT
        elif self.y < 0:
            self.y = 0

        self.last_update = now


def calc_line_size(first_x, first_y, second_x, second_y):
    return sqrt(pow(first_x - second_x, 2) + pow(first_y - second_y, 2))


def calc_nearest_position(first_x, first_y, second_x, second_y):
    pass
