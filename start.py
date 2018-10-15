import world
import pygame
from locals.constants import *
from pygame.locals import *
import control_unit
import render

def update_screen():
    render.render_grids(world.grids)
    render.render_lands(world.lands)
    render.render_ui()
    render.render_update_screen()


def game_init():
    pygame.init()
    world.init(GAME_SIZE)
    render.init(world.grids, world.lands)
    update_screen()

def start():
    game_init()
    clock = pygame.time.Clock()
    player = control_unit.Player()
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
            if event.type == KEYDOWN:
                if keycoude == K_0:
                    player.move(10,0)
            if event.type == KEYUP:
                
        clock.tick(FPS)
    pygame.quit()


if __name__=="__main__":
    start()




