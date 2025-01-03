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
