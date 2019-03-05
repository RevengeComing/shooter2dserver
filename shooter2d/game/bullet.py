from shooter2d.cmd.config import Config


class Bullet():
    def __init__(self, player, direction):
        self.player = player
        self.direction = direction
        self.speed = Config.Game.BULLET_SPEED

    def shoot_task(self):
        pass
