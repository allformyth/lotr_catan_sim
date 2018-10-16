import pygame
import world
import render

from constants import *
from pygame.locals import *
import control_unit



def update_screen():
    render.render_grids(world.tiles)
    render.render_lands(world.corners)
    render.render_ui(control_unit.players)
    render.render_players(control_unit.players)
    pygame.display.update()


def start():
    pygame.init()
    world.init(GAME_SIZE)
    render.init(world.tiles, world.corners)
    control_unit.init_player()
    clock = pygame.time.Clock()
    game_exit = False
    player = control_unit.players[0]
    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
            if event.type == KEYDOWN:
                if event.key == K_a:
                    player.move(-1, 0)
                elif event.key == K_d:
                    player.move(1, 0)
                elif event.key == K_w:
                    player.move(0, -1)
                elif event.key == K_s:
                    player.move(0, 1)
        update_screen()
        clock.tick(FPS)
    pygame.quit()


if __name__=="__main__":
    start()




