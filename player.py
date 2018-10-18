from constants import *
import render
import world
import pygame

class Player(render.IRender):
    id = 0

    def __init__(self):
        self.pos_col, self.pos_row = BORN_POINT
        self.money = INIT_GOLD
        self.id = Player.id
        Player.id += 1

    def get_pos(self):
        return self.pos_col, self.pos_row

    def move(self, x, y):
        self.pos_col = self.pos_col + x if 1 <= self.pos_col + x <= GAME_SIZE[0] else self.pos_col
        self.pos_row = self.pos_row + y if 1 <= self.pos_row + y <= GAME_SIZE[1] else self.pos_row

    def recruit(self):
        max_num = int(self.money / RECRUIT_PRICE)
        num = min()

    def build_city(self):
        pass

    def on_render(self, screen):
        player_coordinate = world.get_grid_middle_point(self.pos_col, self.pos_row)
        player_width = 20
        pygame.draw.rect(screen, BLACK, [player_coordinate[0] - int(player_width / 2),
                                         player_coordinate[1] - int(player_width / 2),
                                         20, 20])
