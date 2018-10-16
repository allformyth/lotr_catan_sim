import world_unit
import random

tiles = []
token_numbers = []
corners = []


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
            random_resource = -1
            tmp_token_number = -1
            if x != 0 and x != max_cols + 1 and y != 0 and y != max_rows + 1:
                random_resource = random.randint(1, 4)
                random_index = random.randint(0, len(token_numbers) - 1)
                tmp_token_number = token_numbers.pop(random_index)
            tiles[x].append(world_unit.Territory(x, y, random_resource, tmp_token_number))

    # 生成 Corners
    for x in range(max_cols):
        for y in range(max_rows):
            adjcents = get_territories_of_adjacents(tiles[x + 1][y + 1])
            land1 = world_unit.Land([adjcents[0], adjcents[1], tiles[x + 1][y + 1]])
            land2 = world_unit.Land([adjcents[1], adjcents[2], tiles[x + 1][y + 1]])
            land3 = world_unit.Land([adjcents[2], adjcents[3], tiles[x + 1][y + 1]])
            land4 = world_unit.Land([adjcents[3], adjcents[4], tiles[x + 1][y + 1]])
            land5 = world_unit.Land([adjcents[4], adjcents[5], tiles[x + 1][y + 1]])
            land6 = world_unit.Land([adjcents[5], adjcents[0], tiles[x + 1][y + 1]])

            try_add_to_list(land1)
            try_add_to_list(land2)
            try_add_to_list(land3)
            try_add_to_list(land4)
            try_add_to_list(land5)
            try_add_to_list(land6)


def try_add_to_list(land):
    if not is_in_list(land):
        corners.append(land)


def is_in_list(land):

    result = False
    for ld in corners:
        if is_the_same_territory(ld, land):
            result = True
    return result


def is_the_same_territory(ld:world_unit.Land, land:world_unit.Land):
    result = False
    if ld.adjcents_territory[0].cpm_num == land.adjcents_territory[0].cpm_num:
        if ld.adjcents_territory[1].cpm_num == land.adjcents_territory[1].cpm_num:
            if ld.adjcents_territory[2].cpm_num == land.adjcents_territory[2].cpm_num:
                result = True
    return result


def get_land_by_three_territory(territory1_pos, territory2_pos, territory3_pos):
    result = None
    return result


def get_lands_of_one_territory(territory_pos):
    result = []
    return result


def get_gird(pos_col, pos_row):
    return tiles[pos_col, pos_row]


def get_territory_index_of_adjacents(territory):
    # left_down,left_up,up,right_up,right_down,down
    adjacents = get_territories_of_adjacents(territory)
    for i in range(len(adjacents)):
        adjacents[i] = (adjacents[i].col_index, adjacents[i].row_index)
    return adjacents


def get_territories_of_adjacents(territory):
    # left_down,left_up,up,right_up,right_down,down
    adjacents = [0, 0, 0, 0, 0, 0]
    # up, down
    tmp_up = (territory.col_index, territory.row_index - 1)
    tmp_down = (territory.col_index, territory.row_index + 1)

    # even_row
    if territory.col_index % 2 == 0:
        # left_up, right_up
        tmp_left_up = (territory.col_index - 1, territory.row_index - 1)
        tmp_right_up = (territory.col_index + 1, territory.row_index - 1)
        # left_down, right_down
        tmp_left_down = (territory.col_index - 1, territory.row_index)
        tmp_right_down = (territory.col_index + 1, territory.row_index)
    else:
        # left_up, right_up
        tmp_left_up = (territory.col_index - 1, territory.row_index)
        tmp_right_up = (territory.col_index + 1, territory.row_index)
        # left_down, right_down
        tmp_left_down = (territory.col_index - 1, territory.row_index + 1)
        tmp_right_down = (territory.col_index + 1, territory.row_index + 1)

    adjacents[2] = tiles[tmp_up[0]][tmp_up[1]]
    adjacents[5] = tiles[tmp_down[0]][tmp_down[1]]
    adjacents[1] = tiles[tmp_left_up[0]][tmp_left_up[1]]
    adjacents[3] = tiles[tmp_right_up[0]][tmp_right_up[1]]
    adjacents[0] = tiles[tmp_left_down[0]][tmp_left_down[1]]
    adjacents[4] = tiles[tmp_right_down[0]][tmp_right_down[1]]

    return adjacents

def roll_dice():
    result = 0
    for i in range(2):
        result = result + random.randint(1, 6)
    return result
