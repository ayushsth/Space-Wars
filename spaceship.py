import pygame

class Spaceship:
    WIDTH,HEIGHT=40,40
    VEL=5

    def __init__(self,x,y,color,controls):
        self.x,self.y=x,y
        self.color=color
        self.image=pygame.image.load(f'spaceship_{color}.png')
        self.image=pygame.transform.scale(self.image,(self.WIDTH,self.HEIGHT))
        self.image=pygame.transform.rotate(self.image, 90 if color=='red' else 270)
        self.rect=pygame.Rect(x,y,40,40)
        self.controls=controls
        self.bullets=[]

    def move(self, keys, screen_width, screen_height):
        if keys[self.controls['up']] and self.rect.y > 0:
            self.rect.y -= self.VEL
        if keys[self.controls['down']] and self.rect.y < screen_height - self.HEIGHT:
            self.rect.y += self.VEL

        if self.color == 'red':
            if keys[self.controls['left']] and self.rect.x > 0:
                self.rect.x -= self.VEL
            if keys[self.controls['right']] and self.rect.x < screen_width / 2 - self.WIDTH:
                self.rect.x += self.VEL
        else:
            if keys[self.controls['left']] and self.rect.x > screen_width / 2:
                self.rect.x -= self.VEL
            if keys[self.controls['right']] and self.rect.x < screen_width - self.WIDTH:
                self.rect.x += self.VEL
                
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x,self.rect.y))

    def reset_position(self,x,y):
        self.rect.x=x
        self.rect.y=y