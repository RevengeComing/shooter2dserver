
class Stone:
    def __init__(self, owner, owner_speed_x, owner_speed_y, game_map,stone_type="normal"):
        self.owner = owner
        self.game_map = game_map
        self.type = type
        self.__speed_x = owner_speed_x * 1.5
        self.__speed_y = owner_speed_y * 1.5

    def hit_wall(self):
        pass
