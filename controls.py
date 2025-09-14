import pygame
import sys

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)

class ControlsScreen:
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.SysFont('times new roman',60)
        self.medium_font=pygame.font.SysFont('times new roman',40)
        self.small_font=pygame.font.SysFont('times new roman',20)
    
    def controls_display(self):
        CONTROLS=self.font.render("CONTROLS",True,WHITE)
        CONTROLS_rect=CONTROLS.get_rect()
        CONTROLS_rect.center=(400,50)

        RED_SPACESHIP=self.medium_font.render("RED SPACESHIP:",True,RED)
        RED_SPACESHIP_rect=RED_SPACESHIP.get_rect()
        RED_SPACESHIP_rect.center=(400,150)


        red_control=self.medium_font.render("W,S,A,D:UP,DOWN,LEFT,RIGHT",True,RED)
        red_control_rect=red_control.get_rect()
        red_control_rect.center=(400,220)

        red_shoot=self.medium_font.render("SPACE:Shoot Bullets",True,RED)
        red_shoot_rect=red_shoot.get_rect()
        red_shoot_rect.center=(400,270)

        
        YELLOW_SPACESHIP=self.medium_font.render("YELLOW SPACESHIP:",True,YELLOW)
        YELLOW_SPACESHIP_rect=YELLOW_SPACESHIP.get_rect()
        YELLOW_SPACESHIP_rect.center=(400,350)

        yellow_control=self.medium_font.render("Arrow Keys:UP,DOWN,LEFT,RIGHT",True,YELLOW)
        yellow_control_rect=yellow_control.get_rect()
        yellow_control_rect.center=(400,420)

        yellow_shoot=self.medium_font.render("RIGHT CTRL(RCTRL):Shoot Bullets",True,YELLOW)
        yellow_shoot_rect=yellow_shoot.get_rect()
        yellow_shoot_rect.center=(400,470)

        back_to_homepage=self.small_font.render("Back To Home Page: Press 'B'",True,WHITE)
        back_to_homepage_rect=back_to_homepage.get_rect()
        back_to_homepage_rect.center=(130,590)

        quit=self.small_font.render("QUIT: Press 'Q'",True,WHITE)
        quit_rect=quit.get_rect()
        quit_rect.center=(730,590)

        self.screen.blit(CONTROLS,CONTROLS_rect)
        self.screen.blit(RED_SPACESHIP,RED_SPACESHIP_rect)
        self.screen.blit(YELLOW_SPACESHIP,YELLOW_SPACESHIP_rect)

        self.screen.blit(red_control,red_control_rect)
        self.screen.blit(red_shoot,red_shoot_rect)

        self.screen.blit(yellow_control,yellow_control_rect)
        self.screen.blit(yellow_shoot,yellow_shoot_rect)

        self.screen.blit(back_to_homepage,back_to_homepage_rect)
        self.screen.blit(quit,quit_rect)

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    return 'main'
                if event.key==pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_b:
                    return 'home'
        
        return 'controls'