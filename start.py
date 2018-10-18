import pygame
import world
import render

from constants import *
import player


def update_screen():
    pygame.display.update()


def start():
    pygame.init()
    world.init(GAME_SIZE)
    render.init(world.tiles, world.corners)
    # clock = pygame.time.Clock()
    game_exit = False
    player = world.players[0]
    render.render_ui(world.players)
    screen = pygame.display.get_surface()
    while not game_exit:
        world.update(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True
            if event.type == KEYDOWN:
                if event.key == P1_MOVE_LEFT:
                    player.move(-1, 0)
                elif event.key == P1_MOVE_RIGHT:
                    player.move(1, 0)
                elif event.key == P1_MOVE_UP:
                    player.move(0, -1)
                elif event.key == P1_MOVE_DOWN:
                    player.move(0, 1)
                elif event.key == P1_RECRUIT:
                    pass
        update_screen()
        # clock.tick(FPS)
    pygame.quit()


if __name__=="__main__":
    start()




