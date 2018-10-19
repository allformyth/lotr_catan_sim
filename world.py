import territory
import city
import random
import player
import map_
from constants import *

grids = []
corners = []
players = []
token_numbers = []

def init(game_size):
    max_cols, max_rows = game_size[0], game_size[1]
    tmp_list = [2] + [3] * 2 + [4] * 2 + [5] * 2 + [6] * 2 + [7] * 2 + [8] * 2 + [9] * 2 + [10] * 2 + [11] * 2 + [12]
    tmp_list = tmp_list * 3
    token_numbers.extend(tmp_list)

    # 生成Grids - 最外圈为地图边界
    for x in range(max_cols + 2):
        grids.append([])
        # 边界地块也要生成出来
        for y in range(max_rows + 2):
            random_resource = 0
            tmp_token_number = -1
            if x != 0 and x != max_cols + 1 and y != 0 and y != max_rows + 1:
                random_resource = random.randint(1, 4)
                random_index = random.randint(0, len(token_numbers) - 1)
                tmp_token_number = token_numbers.pop(random_index)
            grids[x].append(territory.Territory(x, y, random_resource, tmp_token_number))


    # 生成 Corners
    for x in range(max_cols):
        for y in range(max_rows):
            self_grid = get_grid([x + 1, y + 1])
            adj_index = map_.get_territories_index_of_adjacents(x + 1, y + 1)
            adjcents = [get_grid(element) for element in adj_index]

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
    for tile_col in grids:
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


def get_grid(pos):
    return grids[pos[0]][pos[1]]


def roll_dice():
    result = 0
    for i in range(2):
        result = result + random.randint(1, 6)
    return result


def update(event, screen):
    for grid_cols in grids:
        for grid in grid_cols:
            grid.update(event)
            grid.render(screen)
    for city in corners:
        city.update(event)
        city.render(screen)
    for player in players:
        player.update(event)
        player.render(screen)

