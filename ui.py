import pygame
from constants import *




def update(event, screen):
    ui_font = pygame.font.SysFont(None, UI_TEXT_SIZE)
    pygame.draw.line(screen, WHITE, (MAP_SIZE[0], 0), (MAP_SIZE[0], SCREEN_SIZE[1]), UI_LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (0, MAP_SIZE[1]), (SCREEN_SIZE[0], MAP_SIZE[1]), UI_LINE_WIDTH)

    render_label(LABEL_PLAYER_ONE_CONTENT, LABEL_PLAYER_ONE_POSITION, screen, ui_font)
    render_label(LABEL_POSX_CONTENT, LABEL_POSX_POSITION, screen, ui_font)
    render_label(LABEL_POSY_CONTENT, LABEL_POSY_POSITION, screen, ui_font)
    render_label(LABEL_GOLD_CONTENT, LABEL_GOLD_POSITION, screen, ui_font)
    render_label(LABEL_WOOD_CONTENT, LABEL_WOOD_POSITION, screen, ui_font)
    render_label(LABEL_BRICK_CONTENT, LABEL_BRICK_POSITION, screen, ui_font)
    render_label(LABEL_IRON_CONTENT, LABEL_IRON_POSITION, screen, ui_font)
    render_label(LABEL_SCORE_CONTENT, LABEL_SCORE_POSITION, screen, ui_font)


def render_label(text, position, screen, font):
    screen_text = font.render(text, True, WHITE)
    screen.blit(screen_text, position)

