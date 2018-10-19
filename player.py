from constants import *
import map_
import pygame


class Player():
    id = 0

    def __init__(self):
        self.pos_col, self.pos_row = BORN_POINT
        self.money = INIT_GOLD
        self.id = Player.id
        self.coordinate = map_.calc_grid_middle_point_coordinate(self.pos_col, self.pos_row)
        self.sodiers_num = 0
        Player.id += 1

    def get_pos(self):
        return self.pos_col, self.pos_row

    def move(self, x, y):
        self.pos_col = self.pos_col + x if 1 <= self.pos_col + x <= GAME_SIZE[0] else self.pos_col
        self.pos_row = self.pos_row + y if 1 <= self.pos_row + y <= GAME_SIZE[1] else self.pos_row
        self.coordinate = map_.calc_grid_middle_point_coordinate(self.pos_col, self.pos_row)

    def recruit(self):
        num_ = 10
        cost_ = num_ * 10
        if self.money >= cost_:
            self.sodiers_num += 10
            self.money -= cost_

    def attck(self):
        win = True


    def build_city(self):
        pass

    def render(self, screen):
        player_width = 20
        pygame.draw.rect(screen, BLACK, [self.coordinate[0] - int(player_width / 2),
                                         self.coordinate[1] - int(player_width / 2),
                                         player_width, player_width])

    def update(self, event):
        if event.type == KEYDOWN:
            if event.key == P1_MOVE_LEFT:
                self.move(-1, 0)
            elif event.key == P1_MOVE_RIGHT:
                self.move(1, 0)
            elif event.key == P1_MOVE_UP:
                self.move(0, -1)
            elif event.key == P1_MOVE_DOWN:
                self.move(0, 1)
            elif event.key == P1_RECRUIT:
                self.recruit()
