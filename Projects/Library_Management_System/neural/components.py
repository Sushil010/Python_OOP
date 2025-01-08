import pygame

class Ground:
    ground_level=500

    def __init__(self,win_width):
        self.x,self.y=0,Ground.ground_level
        self.rect = pygame.Rect(self.x,self.y,win_width,5)

    # 
    def draw(self,win):
        pygame.draw.rect(win,(255,255,255),self.rect)
