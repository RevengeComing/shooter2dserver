import math
from unittest import TestCase
from shooter2d.game.player import Player


class PlayerTestCase(TestCase):
    def setUp(self):
        self.player = Player(0, 0, "Sepehr")

    def test_asd(self):
        self.player.update()
        self.player.move(
            1*math.sin(45*math.pi/180),
            1*math.cos(45*math.pi/180),
        )
        self.player.update()
        print(self.player.x)
        print(self.player.y)
