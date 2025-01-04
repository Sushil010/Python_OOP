print("Flappy Bird")

import pygame
import os
import neat
import time
import random

WIN_HEIGHT=600
WIN_WIDTH=800

Bird_img=[

    pygame.transform.scale2x(
    pygame.image.load(os.path.join('Flap AI\imgs','bird1.png'))
                            ),

    pygame.transform.scale2x(
    pygame.image.load(os.path.join('Flap AI\imgs','bird1.png'))
                            ),

    pygame.transform.scale2x(
    pygame.image.load(os.path.join('Flap AI\imgs','bird1.png'))
                            )

]

Pipe_img=[

    pygame.transform.scale2x(
    pygame.image.load(os.path.join('Flap AI\imgs','pipe.png'))
                            )

]


background_img=[

    pygame.transform.scale2x(
    pygame.image.load(os.path.join('Flap AI\imgs','bg.png'))
                            )

]

base_img=[

    pygame.transform.scale2x(
    pygame.image.load(os.path.join('Flap AI\imgs','base.png'))
                            )

]



class Bird:
    imgs=bird_img
    max_rotation=25
    rotation_velocity=20
    animation_time=5

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.tilt=0
        self.tick_count=0
        self.vel=0
        self.height=self.y
        self.img_count=0
        self.images=self.imgs[0]
    
    def jump(self):
        self.vel=-10.5
        self.tick_count=0
        self.height=self.y

    def move(self):
        self.tick += 1


while True:
    Bird.move()
    
