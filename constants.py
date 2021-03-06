from pygame.locals import *
# encoding: utf-8
# module constants

# Game Disc
GAME_SIZE = (10, 6)
GAME_NAME = "Lotr_Ineraction_Sims"

#Game logic
TIME_ONE_TURN = 1800

INIT_MONEY = 10000
INIT_GOLD = 100

INIT_WOOD = 100
INIT_IRON = 100
INIT_BRICK = 100
INIT_SHEEP = 100
INIT_WHEAT = 100

BORN_POINT = (1, 1)
MOVE_SPEED = 10

MOVING = 1
REST = 2
ATTACKING = 3


RECRUIT_PRICE = 10


# Display Color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 255, 255)

RESOURCE_COLOR = {0: WHITE, 1: RED, 2: GREEN, 3: YELLOW, 4: BLUE}

# Display Map
SCREEN_SIZE = (1280, 720)
MAP_SIZE = (800, 600)
HEX_SIZE = 28
MIDDLE_POINT_OF_FIRST_GRID = (80, 60)
VERTEX_SIZE = 6

#Display ui
UI_LINE_WIDTH = 5
UI_TEXT_SIZE = 20

# 格子间距 = ( HEX_SPACING_RATE - 1) * HEX_SIZE
HEX_SPACING_RATE = 1.2
MAP_NUM_FONT_SIZE = 35

#Render setting
FPS = 10

# 按键控制
P1_MOVE_UP = K_w
P1_MOVE_DOWN = K_s
P1_MOVE_LEFT = K_a
P1_MOVE_RIGHT = K_d
P1_RECRUIT = K_r

#角色信息界面
LABEL_PLAYER_ONE_CONTENT = "Player1:"
LABEL_PLAYER_ONE_POSITION = (MAP_SIZE[0] + 20, 10)

LABEL_POSX_CONTENT = "      PosX:"
LABEL_POSX_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 20)

LABEL_POSY_CONTENT = "      PosY:"
LABEL_POSY_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 40)

LABEL_GOLD_CONTENT = "      Gold:"
LABEL_GOLD_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 60)

LABEL_WOOD_CONTENT = "      Wood:"
LABEL_WOOD_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 80)

LABEL_BRICK_CONTENT = "      Brick:"
LABEL_BRICK_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 100)

LABEL_IRON_CONTENT = "      Iron:"
LABEL_IRON_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 120)

LABEL_SHEEP_CONTENT = "      Sheep:"
LABEL_SHEEP_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 140)

LABEL_WHEAT_CONTENT = "      Wheat:"
LABEL_WHEAT_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 160)

LABEL_SCORE_CONTENT = "      Score:"
LABEL_SCORE_POSITION = (LABEL_PLAYER_ONE_POSITION[0], LABEL_PLAYER_ONE_POSITION[1] + 180)