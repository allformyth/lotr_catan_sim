import world
import pygame
from constants import *
from pygame.locals import *
import render


def update_screen():
    render.render_grids(world.grids)
    render.render_vertexes(world.lands)
    render.render_ui()
    render.render_update_screen()


def start():
    pygame.init()
    world.init(GAME_SIZE)
    print(len(world.lands))
    render.init()
    game_exit = False
    update_screen()
    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
        update_screen()
    pygame.quit()


if __name__=="__main__":
    start()




