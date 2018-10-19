import pygame
from constants import *
import math


def calc_coordinate_of_city(city):
    """
    :param city:
    :return:the city's position
    """
    coordinate = [0, 0]
    t1, t2, t3 = city.adjcents_territory[0], city.adjcents_territory[1], city.adjcents_territory[2]
    p1 = calc_grid_middle_point_coordinate(t1.col_index, t1.row_index)
    p2 = calc_grid_middle_point_coordinate(t2.col_index, t2.row_index)
    p3 = calc_grid_middle_point_coordinate(t3.col_index, t3.row_index)
    coordinate[0], coordinate[1] = int((p1[0] + p2[0] + p3[0])/3), int((p1[1] + p2[1] + p3[1])/3)
    return coordinate


def calc_vertexes_coordinate_of_grid(middle_point):
    """
    :param middle_point:
    :return:all the vertexes of a hex
    """
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


def get_territories_index_of_adjacents(col, row):
    """
    :param col:
    :param row:
    :return:territories
    """
    # oder left_down,left_up,up,right_up,right_down,down
    # 顺序 左下，左上，上，右上，右下，下
    adjacents = [0, 0, 0, 0, 0, 0]
    # even_col
    if col % 2 == 0:
        adjacents[0] = [col - 1, row + 0]
        adjacents[1] = [col - 1, row - 1]
        adjacents[2] = [col + 0, row - 1]
        adjacents[3] = [col + 1, row - 1]
        adjacents[4] = [col + 1, row - 0]
        adjacents[5] = [col + 0, row + 1]
    # odd_col
    else:
        adjacents[0] = [col - 1, row + 1]
        adjacents[1] = [col - 1, row - 0]
        adjacents[2] = [col - 0, row - 1]
        adjacents[3] = [col + 1, row - 0]
        adjacents[4] = [col + 1, row + 1]
        adjacents[5] = [col + 0, row + 1]
    return adjacents


def calc_grid_middle_point_coordinate(grid_pos_col, grid_pos_row):
    middle_point = [0, 0]
    if grid_pos_col % 2 == 0:
        middle_point[0] = MIDDLE_POINT_OF_FIRST_GRID[0] + (grid_pos_col * HEX_SIZE * 3 / 2) * HEX_SPACING_RATE
        middle_point[1] = MIDDLE_POINT_OF_FIRST_GRID[1] + (grid_pos_row * math.sqrt(3) * HEX_SIZE ) * HEX_SPACING_RATE
    else:
        middle_point[0] = MIDDLE_POINT_OF_FIRST_GRID[0] + (HEX_SIZE * 3 / 2 + (grid_pos_col - 1) * HEX_SIZE * 3/2) * HEX_SPACING_RATE
        middle_point[1] = MIDDLE_POINT_OF_FIRST_GRID[1] + (math.sqrt(3) * HEX_SIZE / 2 + grid_pos_row * math.sqrt(3) * HEX_SIZE) * HEX_SPACING_RATE
        #
    return middle_point

def get_land_by_three_territory(territory1_pos, territory2_pos, territory3_pos):
    result = None
    return result


def get_lands_of_one_territory(territory_pos):
    result = []
    return result