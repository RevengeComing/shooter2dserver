
class Player:
    def __init__(self, x, y, name=""):
        self.x = x
        self.y = y
        self.name = name
        self.speed_x = 0
        self.speed_y = 0
        self.health = 100

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
