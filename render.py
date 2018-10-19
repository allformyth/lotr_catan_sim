import pygame
from constants import *

screen = 0
ui_font = 0


def init():
    global screen
    global ui_font
    screen = pygame.display.get_surface()
    ui_font = pygame.font.SysFont(None, UI_TEXT_SIZE)
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_mode(SCREEN_SIZE)


def render_label(text, position):
    screen_text = ui_font.render(text, True, WHITE)
    screen.blit(screen_text, position)

def render_ui():
    pygame.draw.line(screen, WHITE, (MAP_SIZE[0], 0), (MAP_SIZE[0], SCREEN_SIZE[1]), UI_LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, MAP_SIZE[1]), (SCREEN_SIZE[0], MAP_SIZE[1]), UI_LINE_WIDTH)

    render_label(LABEL_PLAYER_ONE_CONTENT, LABEL_PLAYER_ONE_POSITION)
    render_label(LABEL_POSX_CONTENT, LABEL_POSX_POSITION)
    render_label(LABEL_POSY_CONTENT, LABEL_POSY_POSITION)
    render_label(LABEL_GOLD_CONTENT, LABEL_GOLD_POSITION)
    render_label(LABEL_WOOD_CONTENT, LABEL_WOOD_POSITION)
    render_label(LABEL_BRICK_CONTENT, LABEL_BRICK_POSITION)
    render_label(LABEL_IRON_CONTENT, LABEL_IRON_POSITION)
    render_label(LABEL_SCORE_CONTENT, LABEL_SCORE_POSITION)