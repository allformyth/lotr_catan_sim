import render
import pygame
from constants import *


class City():
    def __init__(self, adjcent_territories):
        assert len(adjcent_territories) == 3
        self.adjcent_territories = sorted(adjcent_territories, key=lambda x: x.guid)
        self.guid = self.adjcent_territories[0].guid * 10000 * 10000 + \
                    self.adjcent_territories[1].guid * 10000 + \
                    self.adjcent_territories[2].guid
        self._coordinate = []
        self.rect = 0
        self.level = 0
        self.owner = 0

    def get_coordinate(self):
        if not self._coordinate:
            p1 = self.adjcent_territories[0].middle_point
            p2 = self.adjcent_territories[1].middle_point
            p3 = self.adjcent_territories[2].middle_point
            self._coordinate = [int((p1[0] + p2[0] + p3[0])/3), int((p1[1] + p2[1] + p3[1])/3)]
        return self._coordinate

    def render(self, screen):
        vertex_coordinate = self.get_coordinate()
        pygame.draw.circle(screen, WHITE, vertex_coordinate, VERTEX_SIZE)

    def update(self, event):
        pass