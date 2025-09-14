import pygame

class Bullet:
    bullet_width,bullet_height=35,6
    VEL=5

    def __init__(self,x,y,direction):
        self.rect=pygame.Rect(x,y,self.bullet_width,self.bullet_height)
        self.direction=direction
    
    def move(self):
        self.rect.x+=self.VEL*self.direction