import pygame
from locals.ui import *
import math

points = []


def init(grids, lands):
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_mode(SCREEN_SIZE)
    render_grids(grids)
    render_lands(lands)
    #render_ui()


def render_grids(grids):
    for cols in grids:
        for grid in cols:
            render_grid(grid.col_index, grid.row_index, grid.resource, grid.number)


def render_grid(col, row, resource, number):
    screen = pygame.display.get_surface()
    map_num_font = pygame.font.SysFont('Calibri', MAP_NUM_FONT_SIZE)
    text = map_num_font.render(str(number), True, BLACK)
    middle_point = get_grid_middle_point(col, row)
    text_point = (middle_point[0]-int(MAP_NUM_FONT_SIZE/2), middle_point[1]-int(MAP_NUM_FONT_SIZE/2))

    if resource == -1:
        pygame.draw.polygon(screen, BLUE, get_grid_vertex(middle_point))
    elif resource == 1:
        pygame.draw.polygon(screen, WHITE, get_grid_vertex(middle_point))
    elif resource == 2:
        pygame.draw.polygon(screen, RED, get_grid_vertex(middle_point))
    elif resource == 3:
        pygame.draw.polygon(screen, YELLOW, get_grid_vertex(middle_point))
    else:
        pygame.draw.polygon(screen, GREEN, get_grid_vertex(middle_point))

    if number != 7 and number != -1:
        screen.blit(text, text_point)


def render_lands(lands):
    for land in lands:
        render_land(land)


def render_land(land):
    screen = pygame.display.get_surface()
    vertex_coordinate = get_vertex_point(land)
    pygame.draw.circle(screen, WHITE, vertex_coordinate, VERTEX_SIZE)


def render_players(players):
    for player in players:
        render_player(player)


def render_player(player):
    screen = pygame.display.get_surface()
    player_coordinate = get_grid_middle_point(player.pos[0], player.pos[1])
    player_width = 20
    pygame.draw.rect(screen, BLACK, [player_coordinate[0] - int(player_width / 2),player_coordinate[1]-int(player_width / 2),20,20])


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


def render_label(text, position):
    font = pygame.font.SysFont('Calibri', UI_TEXT_SIZE)
    screen = pygame.display.get_surface()
    screen_text = font.render(text, True, WHITE)
    screen.blit(screen_text, position)


def get_grid_middle_point(grid_pos_col, grid_pos_row):
    middle_point = [0, 0]
    if grid_pos_col % 2 == 0:
        middle_point[0] = MIDDLE_POINT_OF_FIRST_GRID[0] + (grid_pos_col * HEX_SIZE * 3 / 2) * HEX_SPACING_RATE
        middle_point[1] = MIDDLE_POINT_OF_FIRST_GRID[1] + (grid_pos_row * math.sqrt(3) * HEX_SIZE ) * HEX_SPACING_RATE
    else:
        middle_point[0] = MIDDLE_POINT_OF_FIRST_GRID[0] + (HEX_SIZE * 3 / 2 + (grid_pos_col - 1) * HEX_SIZE * 3/2) * HEX_SPACING_RATE
        middle_point[1] = MIDDLE_POINT_OF_FIRST_GRID[1] + (math.sqrt(3) * HEX_SIZE / 2 + grid_pos_row * math.sqrt(3) * HEX_SIZE) * HEX_SPACING_RATE
    return middle_point


def get_grid_vertex(middle_point=(100, 100)):
    vertex_coordinates = []
    left_point = (middle_point[0] - HEX_SIZE, middle_point[1])
    left_bottom_point = (middle_point[0] - HEX_SIZE / 2, middle_point[1] + math.sqrt(3) / 2 * HEX_SIZE)
    right_bottom_point = (middle_point[0] + HEX_SIZE / 2, middle_point[1] + math.sqrt(3) / 2 * HEX_SIZE)
    right_point = (middle_point[0] + HEX_SIZE, middle_point[1])
    right_up_point = (middle_point[0] + HEX_SIZE / 2, middle_point[1] - math.sqrt(3) / 2 * HEX_SIZE)
    left_up_point = (middle_point[0] - HEX_SIZE / 2, middle_point[1] - math.sqrt(3) / 2 * HEX_SIZE)
    vertex_coordinates.append(left_point)
    vertex_coordinates.append(left_bottom_point)
    vertex_coordinates.append(right_bottom_point)
    vertex_coordinates.append(right_point)
    vertex_coordinates.append(right_up_point)
    vertex_coordinates.append(left_up_point)
    return vertex_coordinates


def get_vertex_point(land):
    vertex_coordinate = [0,0]

    t1 = land.adjcents_territory[0]
    t2 = land.adjcents_territory[1]
    t3 = land.adjcents_territory[2]

    p1 = get_grid_middle_point(t1.col_index, t1.row_index)
    p2 = get_grid_middle_point(t2.col_index, t2.row_index)
    p3 = get_grid_middle_point(t3.col_index, t3.row_index)

    vertex_coordinate[0] = int((p1[0] + p2[0] + p3[0])/3)
    vertex_coordinate[1] = int((p1[1] + p2[1] + p3[1])/3)

    return vertex_coordinate


