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
        self.img=self.imgs[0]
    
    def jump(self):
        self.vel=-10.5
        self.tick_count=0
        self.height=self.y

    def move(self):
        self.tick_count+= 1

        d=self.vel*self.tick_count + 1.5*self.tick_count**2

        # -10.5*1+1.5*1=-7,-4,-2,0
        # this equation will set up a parabolic path for motion of 
        # bird to move upward motion until it reaches at top

        if d>=16:
            d=16
        
        if d<0:
            d -= 2

        self.y=self.y+d


        # tilting in upward position

        if d<0 or self.y < self.height + 50:
            if self.tilt < self.max_rotation:
                self.tilt=self.max_rotation
        
        else:
            if self.tilt> -90:
                self.tilt -= self.rotation_velocity


    def draw(self,win):
        self.img_count+=1

        if self.img_count<self.animation_time:
            self.img=self.imgs[0]

        elif self.img_count<self.animation_time * 2:
            self.img=self.imgs[1]

        elif self.img_count<self.animation_time * 3:
            self.img=self.imgs[2]
        
        elif self.img_count<self.animation_time * 4:
            self.img=self.imgs[1]
        
        elif self.img_count<self.animation_time * 4 + 1:
            self.img=self.imgs[0]
            self.img_count=0
        
        if self.tilt <= -80:
            self.img =self.imgs[1]
            sels.img_count = self.animation_time*2
        
        rotated_image=pygame.transform.rotate(self.img,self.tilt)

