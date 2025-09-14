import pygame
from bullets import Bullet

class GameLogic:
    MAX_BULLETS=5

    def __init__(self,red_spaceship,yellow_spaceship,bullet_fire_sound,bullet_hit_sound):
        self.red=red_spaceship
        self.yellow=yellow_spaceship
        self.red_bullets=[]
        self.yellow_bullets=[]
        self.red_score=25
        self.yellow_score=25
        self.bullet_fire_sound=bullet_fire_sound
        self.bullet_hit_sound=bullet_hit_sound
    
    def fire_bullet(self,is_red):
        if is_red and len(self.red_bullets)<self.MAX_BULLETS:
            bullet = Bullet(self.red.rect.x+self.red.rect.width-10,
                            self.red.rect.y+self.red.rect.height//2-2, 1)
            self.red_bullets.append(bullet)
            self.bullet_fire_sound.play()
        
        elif not is_red and len(self.yellow_bullets)<self.MAX_BULLETS:
            bullet = Bullet(self.yellow.rect.x-self.yellow.rect.width+10,
                            self.yellow.rect.y+self.yellow.rect.height//2-2,-1)
            
            self.yellow_bullets.append(bullet)
            self.bullet_fire_sound.play()
        
    
    def update_bullets(self,screen_width):
        for bullet in self.red_bullets[:]:
            bullet.move()
            if bullet.rect.colliderect(self.yellow.rect):
                self.bullet_hit_sound.play()
                self.yellow_score-=1
                self.red_bullets.remove(bullet)
            elif bullet.rect.x>screen_width:
                self.red_bullets.remove(bullet)
        
        for bullet in self.yellow_bullets[:]:
            bullet.move()
            if bullet.rect.colliderect(self.red.rect):
                self.bullet_hit_sound.play()
                self.red_score-=1
                self.yellow_bullets.remove(bullet)
            elif bullet.rect.x<0:
                self.yellow_bullets.remove(bullet)
            