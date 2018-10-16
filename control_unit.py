from constants import *

players = []


class Player:
    def __init__(self):
        self.pos = list(BORN_POINT)
        self.money = INIT_GOLD
        #self.army = 0
        #self.resources = [INIT_WOOD, INIT_BRICK, INIT_WHEAT, INIT_SHEEP, INIT_IRON]
        #self.status = REST

    def move(self, x, y):
        self.pos[0] = self.pos[0] + x if 1 <= self.pos[0] + x <= GAME_SIZE[0] else self.pos[0]
        self.pos[1] = self.pos[1] + y if 1 <= self.pos[1] + y <= GAME_SIZE[1] else self.pos[1]

    def recruit(self, pos):
        max_num = int(self.money / RECRUIT_PRICE)
        num = min()

def init_player():
    players.append(Player())

