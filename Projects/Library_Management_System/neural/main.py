import pygame
from sys import exit
import os
import config


pygame.init()
clock=pygame.time.Clock()

def quit_game():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

def main():
    while True:
        quit_game()
        config.win.fill((0,0,0))
        pygame.display.update()
        clock.tick(60)

main()