import pygame
import sys

WHITE=(255,255,255)

class RulesScreen:
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.SysFont('times new roman',60)
        self.medium_font=pygame.font.SysFont('times new roman',40)
        self.small_font=pygame.font.SysFont('times new roman',20)
    
    def rules_display(self):
        RULES=self.font.render("RULES",True,WHITE)
        RULES_rect=RULES.get_rect()
        RULES_rect.center=(400,50)

        rule1_font=self.medium_font.render("1)Shoot the Opponents Spaceship!",True,WHITE)
        rule1_font_rect=rule1_font.get_rect()
        rule1_font_rect.center=(400,150)

        rule2_font=self.medium_font.render("2)Each player can shoot only 5 bullets at a time!",True,WHITE)
        rule2_font_rect=rule2_font.get_rect()
        rule2_font_rect.center=(400,200)

        rule3_font=self.medium_font.render("3)Player whose score reaches zero first loses!",True,WHITE)
        rule3_font_rect=rule3_font.get_rect()
        rule3_font_rect.center=(400,250)

        rule4_font=self.medium_font.render("4)Press 'P' to Play Again!",True,WHITE)
        rule4_font_rect=rule4_font.get_rect()
        rule4_font_rect.center=(400,300)

        rule5_font=self.medium_font.render("5)Press 'X' to QUIT!",True,WHITE)
        rule5_font_rect=rule5_font.get_rect()
        rule5_font_rect.center=(400,350)

        back_to_homepage=self.small_font.render("Back To Home Page: Press 'B'",True,WHITE)
        back_to_homepage_rect=back_to_homepage.get_rect()
        back_to_homepage_rect.center=(130,590)

        quit=self.small_font.render("QUIT: Press 'Q'",True,WHITE)
        quit_rect=quit.get_rect()
        quit_rect.center=(730,590)

        self.screen.blit(RULES,RULES_rect)
        self.screen.blit(rule1_font,rule1_font_rect)
        self.screen.blit(rule2_font,rule2_font_rect)
        self.screen.blit(rule3_font,rule3_font_rect)
        self.screen.blit(rule4_font,rule4_font_rect)
        self.screen.blit(rule5_font,rule5_font_rect)

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
                
        return 'rules'