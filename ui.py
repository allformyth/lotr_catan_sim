import pygame

font = 0
screen = pygame.display.get_surface()

def init():

def render_label(text, position):

    screen_text = font.render(text, True, WHITE)
    screen.blit(screen_text, position)


def render_ui(players):
    screen = pygame.display.get_surface()
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

    render_player_position_ui(players[0])


def render_player_position_ui(player):
    render_label(str(player.pos[1]), [1000, 20])
    render_label(str(player.pos[0]), [1000, 40])


