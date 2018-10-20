import pygame
import world
import ui
from constants import *


def start():
    pygame.init()
    pygame.display.set_caption(GAME_NAME)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    world.init(GAME_SIZE)
    clock = pygame.time.Clock()
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
            world.update(event, screen)
            ui.update(event, screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    start()




