import pygame
import world
from constants import *
import math


class IRender:
    screen = pygame.display.get_surface()
    ui_font = pygame.font.SysFont('Calibri', UI_TEXT_SIZE)

    """
    obj interface
    all obj inherit Irender
    include grid land player
    """
    def on_render(self, screen):
        pass


def init(grids, lands):
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_mode(SCREEN_SIZE)
    # render_grids(grids)
    #render_ui()

