from constants import *
import world_unit
import random


grids = []
numbers = []
lands=[]


def init(game_size):
    tmp_list = [2] + [3] * 2 + [4]*2 + [5]*2 + [6]*2 + [7]*2 + [8]*2 + [9]*2 + [10] * 2 + [11]*2 +[12]
    tmp_list2 = tmp_list * 3
    numbers.extend(tmp_list2)

    for x in range(game_size[0]+2):
        grids.append([])
        for y in range(game_size[1]+2):
            random_resource = random.randint(1, 4)
            if x == 0 or x == game_size[0]+1 or y == 0 or y == game_size[1]+1:
                random_resource = -1
                number = -1
            else:
                random_index = random.randint(0, len(numbers) - 1)
                number = numbers.pop(random_index)
            grids[x].append(world_unit.Territory(x, y, random_resource, number))

    for x in range(game_size[0]):
        for y in range(game_size[1]):
            adjcents = get_territories_of_adjacents(grids[x+1][y+1])
            land1 = world_unit.Land([adjcents[0], adjcents[1], grids[x+1][y+1]])
            land2 = world_unit.Land([adjcents[1], adjcents[2], grids[x + 1][y + 1]])
            land3 = world_unit.Land([adjcents[2], adjcents[3], grids[x + 1][y + 1]])
            land4 = world_unit.Land([adjcents[3], adjcents[4], grids[x + 1][y + 1]])
            land5 = world_unit.Land([adjcents[4], adjcents[5], grids[x + 1][y + 1]])
            land6 = world_unit.Land([adjcents[5], adjcents[0], grids[x + 1][y + 1]])

            try_add_to_list(land1)
            try_add_to_list(land2)
            try_add_to_list(land3)
            try_add_to_list(land4)
            try_add_to_list(land5)
            try_add_to_list(land6)


def try_add_to_list(land):
    if not is_in_list(land):
        lands.append(land)


def is_in_list(land):

    result = False
    for ld in lands:
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
    return grids[pos_col, pos_row]


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

    adjacents[2] = grids[tmp_up[0]][tmp_up[1]]
    adjacents[5] = grids[tmp_down[0]][tmp_down[1]]
    adjacents[1] = grids[tmp_left_up[0]][tmp_left_up[1]]
    adjacents[3] = grids[tmp_right_up[0]][tmp_right_up[1]]
    adjacents[0] = grids[tmp_left_down[0]][tmp_left_down[1]]
    adjacents[4] = grids[tmp_right_down[0]][tmp_right_down[1]]

    return adjacents

def roll_dice():
    result = 0
    for i in range(2):
        result = result + random.randint(1, 6)
    return result


