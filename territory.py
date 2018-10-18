import render
import pygame
import world
from constants import *


class Territory(render.IRender):
    def __init__(self, col_index, row_index, resource, number):
        self.col_index = col_index
        self.row_index = row_index
        self.guid = col_index * 100 + row_index
        self.resource = resource
        self.number = number
        self.is_mining = False

        self.middle_point = world.get_grid_middle_point(self.col_index, self.row_index)
        self.grid_vertexes = world.get_grid_vertex(self.middle_point)

    def get_pos(self):
        return self.col_index, self.row_index

    def __repr__(self):
        return "grid_index: ({one.col_index}, {one.row_index})".format(one=self)

    def on_render(self, screen):
        assert (0 <= self.resource <= 4)
        pygame.draw.polygon(screen, RESOURCE_COLOR[self.resource], self.grid_vertexes)

        map_num_font = pygame.font.SysFont('Calibri', MAP_NUM_FONT_SIZE)
        text = map_num_font.render(str(self.number), True, BLACK)
        text_point = (self.middle_point[0] - int(MAP_NUM_FONT_SIZE / 2), self.middle_point[1] - int(MAP_NUM_FONT_SIZE / 2))
        if self.number not in [-1, 7]:
            screen.blit(text, text_point)





