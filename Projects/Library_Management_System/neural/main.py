import pygame
from sys import exit
import os
import config
import components

pygame.init()
clock=pygame.time.Clock()

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time=10
    while True:
        quit_game()
        config.win.fill((0,0,0))

        config.ground.draw(config.win)

        if pipes_spawn_time<=0:
            generate_pipes()
            pipes_spawn_time=200
        
        pipes_spawn_time-=1

        for pipe in config.pipes:
            pipe.draw(config.win)
            pipe.update()
            if pipe.off_screen:
                config.pipes.remove(pipe)
        
        clock.tick(60)
        pygame.display.flip()

main()