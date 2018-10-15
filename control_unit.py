from locals.game_logic_constants import *


class Player:
    def __init__(self):
        self.pos = BORN_POINT
        self.money = INIT_GOLD
        self.army = 0
        self.resources = [INIT_WOOD, INIT_BRICK, INIT_WHEAT, INIT_SHEEP, INIT_IRON]
        self.status = REST

    def move(self, x , y):
        self.status = MOVING
        self.pos[0] += x
        self.pos[1] += y
