import territory
import city
import random
import math
import player
from constants import *

tiles = []
token_numbers = []
corners = []
players = []

def init(game_size):
    max_cols, max_rows = game_size[0], game_size[1]
    tmp_list = [2] + [3] * 2 + [4] * 2 + [5] * 2 + [6] * 2 + [7] * 2 + [8] * 2 + [9] * 2 + [10] * 2 + [11] * 2 + [12]
    tmp_list = tmp_list * 3
    token_numbers.extend(tmp_list)

    # 生成Grids - 最外圈为地图边界
    for x in range(max_cols + 2):
        tiles.append([])
        # 边界地块也要生成出来
        for y in range(max_rows + 2):
            random_resource = 0
            tmp_token_number = -1
            if x != 0 and x != max_cols + 1 and y != 0 and y != max_rows + 1:
                random_resource = random.randint(1, 4)
                random_index = random.randint(0, len(token_numbers) - 1)
                tmp_token_number = token_numbers.pop(random_index)
            tiles[x].append(territory.Territory(x, y, random_resource, tmp_token_number))


    # 生成 Corners
    for x in range(max_cols):
        for y in range(max_rows):
            self_grid = get_grid(x + 1, y + 1)
            adjcents = get_territories_of_adjacents(self_grid)

            try_add_to_list(city.City([adjcents[0], adjcents[1], self_grid]))
            try_add_to_list(city.City([adjcents[1], adjcents[2], self_grid]))
            try_add_to_list(city.City([adjcents[2], adjcents[3], self_grid]))
            try_add_to_list(city.City([adjcents[3], adjcents[4], self_grid]))
            try_add_to_list(city.City([adjcents[4], adjcents[5], self_grid]))
            try_add_to_list(city.City([adjcents[5], adjcents[0], self_grid]))
    # 生成 Player
    players.append(player.Player())
    return True


def update(screen):
    for tile_col in tiles:
        for tile in tile_col:
            tile.on_render(screen)
    for land in corners:
        land.on_render(screen)
    for player in players:
        player.on_render(screen)


def get_lands_by_player_id(id):
    result = []
    for ld in corners:
        if ld.owner == id:
            result.append(ld)
    return result

def try_add_to_list(land):
    if corners:
        for ld in corners:
            if ld.guid == land.guid:
                break
        else:
            corners.append(land)
    else:
        corners.append(land)


def get_land_by_three_territory(territory1_pos, territory2_pos, territory3_pos):
    result = None
    return result


def get_lands_of_one_territory(territory_pos):
    result = []
    return result


def get_grid(pos_col, pos_row):
    return tiles[pos_col][pos_row]


def get_territory_index_of_adjacents(territory):
    # left_down,left_up,up,right_up,right_down,down
    adjacents = get_territories_of_adjacents(territory)
    for i in range(len(adjacents)):
        adjacents[i] = (adjacents[i].col_index, adjacents[i].row_index)
    return adjacents


def get_territories_of_adjacents(territory):
    # oder left_down,left_up,up,right_up,right_down,down
    # 顺序 左下，左上，上，右上，右下，下
    adjacents = [0, 0, 0, 0, 0, 0]
    # even_col
    if territory.col_index % 2 == 0:
        adjacents[0] = get_grid(territory.col_index - 1, territory.row_index)
        adjacents[1] = get_grid(territory.col_index - 1, territory.row_index - 1)
        adjacents[2] = get_grid(territory.col_index, territory.row_index - 1)
        adjacents[3] = get_grid(territory.col_index + 1, territory.row_index - 1)
        adjacents[4] = get_grid(territory.col_index + 1, territory.row_index)
        adjacents[5] = get_grid(territory.col_index, territory.row_index + 1)
    # odd_col
    else:
        adjacents[0] = get_grid(territory.col_index - 1, territory.row_index + 1)
        adjacents[1] = get_grid(territory.col_index - 1, territory.row_index)
        adjacents[2] = get_grid(territory.col_index, territory.row_index - 1)
        adjacents[3] = get_grid(territory.col_index + 1, territory.row_index)
        adjacents[4] = get_grid(territory.col_index + 1, territory.row_index + 1)
        adjacents[5] = get_grid(territory.col_index, territory.row_index + 1)
    return adjacents

def roll_dice():
    result = 0
    for i in range(2):
        result = result + random.randint(1, 6)
    return result

def get_grid_middle_point(grid_pos_col, grid_pos_row):
    middle_point = [0, 0]
    if grid_pos_col % 2 == 0:
        middle_point[0] = MIDDLE_POINT_OF_FIRST_GRID[0] + (grid_pos_col * HEX_SIZE * 3 / 2) * HEX_SPACING_RATE
        middle_point[1] = MIDDLE_POINT_OF_FIRST_GRID[1] + (grid_pos_row * math.sqrt(3) * HEX_SIZE ) * HEX_SPACING_RATE
    else:
        middle_point[0] = MIDDLE_POINT_OF_FIRST_GRID[0] + (HEX_SIZE * 3 / 2 + (grid_pos_col - 1) * HEX_SIZE * 3/2) * HEX_SPACING_RATE
        middle_point[1] = MIDDLE_POINT_OF_FIRST_GRID[1] + (math.sqrt(3) * HEX_SIZE / 2 + grid_pos_row * math.sqrt(3) * HEX_SIZE) * HEX_SPACING_RATE
        #
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