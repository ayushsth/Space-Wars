import pygame
import sys

WHITE=(255,255,255)
BLUE=(0,0,255)

pixelpurl_font=r'C:\Users\Dell\Desktop\Python Tutorial\Projects\Space Wars\fonts\PixelPurl.ttf'
class HomeScreen:
    def __init__(self,screen):
        self.screen=screen
        self.font=pygame.font.SysFont('times new roman',50)
        self.small_font=pygame.font.SysFont('times new roman',40)
        self.pixelpurl=pygame.font.SysFont('pixelpurl_font',50)

    
    def display(self):
        SW_font=pygame.font.SysFont('Ariel',100)
        SPACE_WARS_font=SW_font.render("SPACE WARS",True, BLUE)
        HS_rect=SPACE_WARS_font.get_rect()
        HS_rect.center=(400,40)

        HS_fonts=pygame.font.SysFont('times new roman',50)
        Controls_font=HS_fonts.render("Controls => Press 'C'",True,WHITE)
        Controls_font_rect=Controls_font.get_rect()
        Controls_font_rect.center=(400,150)

        Rules_font=HS_fonts.render("Rules => Press 'R'",True,WHITE)
        Rules_font_rect=Rules_font.get_rect()
        Rules_font_rect.center=(400,250)

        Play_font=HS_fonts.render("Play => Press 'SPACE'",True,WHITE)
        Play_font_rect=Play_font.get_rect()
        Play_font_rect.center=(400,350)

        Quit_font=HS_fonts.render("Quit the Game => Press 'X'",True,WHITE)
        Quit_font_rect=Quit_font.get_rect()
        Quit_font_rect.center=(400,450)

        self.screen.blit(SPACE_WARS_font,HS_rect)
        self.screen.blit(Controls_font,Controls_font_rect)
        self.screen.blit(Rules_font,Rules_font_rect)
        self.screen.blit(Play_font,Play_font_rect)
        self.screen.blit(Quit_font,Quit_font_rect)

        pygame.display.update()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    return 'controls'
                
                if event.key==pygame.K_r:
                    return 'rules'
                
                if event.key==pygame.K_SPACE:
                    return 'play'
                
                if event.key==pygame.K_x:
                    pygame.quit()
                    sys.exit()

        return 'home'