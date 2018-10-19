import pygame
import world
import render
from constants import *


def game_init():
    pygame.init()
    world.init(GAME_SIZE)
    render.init()


def start():
    game_init()
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
        world.update(event, screen)

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    start()




