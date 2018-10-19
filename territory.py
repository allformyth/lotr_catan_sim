import render
import pygame
import world
import math
import map_
from constants import *


class Territory:
    def __init__(self, col_index, row_index, resource, number):
        self.col_index = col_index
        self.row_index = row_index
        self.guid = col_index * 100 + row_index
        self.resource = resource
        self.number = number
        self.is_mining = False

        self.middle_point = map_.calc_grid_middle_point_coordinate(self.col_index, self.row_index)
        self.grid_vertexes = map_.calc_vertexes_coordinate_of_grid(self.middle_point)

        self.monster_level = self.col_index + self.row_index
        self.monster_power = self.monster_level * 10

    def get_pos(self):
        return self.col_index, self.row_index

    def __repr__(self):
        return "grid_index: ({one.col_index}, {one.row_index})".format(one=self)

    def render(self, screen):
        assert (0 <= self.resource <= 4)
        pygame.draw.polygon(screen, RESOURCE_COLOR[self.resource], self.grid_vertexes)

        map_num_font = pygame.font.SysFont('Calibri', MAP_NUM_FONT_SIZE)
        text = map_num_font.render(str(self.number), True, BLACK)
        text_point = (self.middle_point[0] - int(MAP_NUM_FONT_SIZE / 2), self.middle_point[1] - int(MAP_NUM_FONT_SIZE / 2))
        if self.number not in [-1, 7]:
            screen.blit(text, text_point)

    def update(self, event):
        pass