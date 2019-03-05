from math import sqrt

from shooter2d.game.stone import Stone

from ..cmd.config import Config


class Player:
    def __init__(self, x, y, game_map, name=""):
        self.game_map = game_map
        self.x = x
        self.y = y
        self.name = name
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100
        self.stone_numbers = 5
        self.has_blink = True

    def set_name(self, name):
        self.name = name

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def set_speed(self, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

    def add_hp(self, hp_amount: int):
        self.health = max(100, self.health + hp_amount)

    def shoot_stein(self):
        Stone(owner=self.name, owner_speed_x=self.speed_x, owner_speed_y=self.speed_y, game_map=self.game_map)
        self.stone_numbers -= 1

    def take_stones(self, number_of_stones):
        self.stone_numbers += number_of_stones

    def blink(self, blink_position_x, blink_position_y):
        if self.has_blink:
            self.has_blink = False
            self.x = blink_position_x if calc_line_size(first_x=self.x,
                                                        first_y=self.y,
                                                        second_x=blink_position_x,
                                                        second_y=blink_position_y) < Config.BLINK_RANGE \
                else calc_nearest_position(first_x=self.x,
                                           first_y=self.y,
                                           second_x=blink_position_x,
                                           second_y=blink_position_y)
        else:
            return


def calc_line_size(first_x, first_y, second_x, second_y):
    return sqrt(pow(first_x - second_x, 2) + pow(first_y - second_y, 2))


def calc_nearest_position(first_x, first_y, second_x, second_y):
    pass
