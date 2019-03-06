import math
import time

from shooter2d.cmd.config import Config


class Bullet():
    def __init__(self, player, direction):
        self.x = player.x
        self.y = player.y
        self.radius = Config.Game.BULLET_RADIUS
        self.owner = player
        self.direction = direction
        self.speed = Config.Game.BULLET_SPEED
        self.expire_at = time.time() + Config.Game.BULLET_DURATION
        self.last_update = time.time()

    def update(self):
        now = time.time()
        dt = now - self.last_update
        self.x += self.speed * math.cos(self.direction) * dt
        self.y += self.speed * math.sin(self.direction) * dt
        self.last_update = now

    def is_collide_with(self, player):
        radius_sum = self.radius + player.radius
        if (((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 1/2) < radius_sum:
            return True
        return False
