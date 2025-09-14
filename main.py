import pygame
from spaceship import Spaceship
from game_logic import GameLogic
from ui import UI
from home_screen import HomeScreen
from rules import RulesScreen
from controls import ControlsScreen

pygame.init()
pygame.font.init()
pygame.mixer.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Wars")
clock = pygame.time.Clock()

bullet_fire = pygame.mixer.Sound("Grenade+1.mp3")
bullet_hit = pygame.mixer.Sound("Gun+Silencer.mp3")

RED_CONTROLS = {
    'up': pygame.K_w,
    'down': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'shoot': pygame.K_SPACE
}

YELLOW_CONTROLS = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'shoot': pygame.K_RCTRL
}

red_ship = Spaceship(10,HEIGHT//2-16,'red',RED_CONTROLS)
yellow_ship = Spaceship(WIDTH-60,HEIGHT//2-16,'yellow',YELLOW_CONTROLS)

logic = GameLogic(red_ship,yellow_ship,bullet_fire,bullet_hit)
ui = UI(screen,WIDTH,HEIGHT)

home_screen=HomeScreen(screen)
rules_screen=RulesScreen(screen)
control_screen=ControlsScreen(screen)

def reset_game():
    red_ship.reset_position(10, HEIGHT // 2 - 16)
    yellow_ship.reset_position(WIDTH - 60, HEIGHT // 2 - 16)
    logic.red_score = 25
    logic.yellow_score = 25
    logic.red_bullets.clear()
    logic.yellow_bullets.clear()

def handle_game_end(winner_text):
    ui.draw_winner(winner_text)
    ui.draw_play_again()
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_p:
                    reset_game()
                    waiting = False

def main():
    current_screen='home'

    running = True
    while running:
        screen.fill(BLACK)

        if current_screen=='home':
            home_screen.display()
            current_screen=home_screen.handle_events()
        
        elif current_screen=='rules':
            rules_screen.rules_display()
            current_screen=rules_screen.handle_events()
        
        elif current_screen =='controls':
            control_screen.controls_display()
            current_screen=control_screen.handle_events()

        elif current_screen=='play':
            clock.tick(60)
            screen.fill(BLACK)

            keys = pygame.key.get_pressed()
            red_ship.move(keys,WIDTH,HEIGHT)
            yellow_ship.move(keys,WIDTH,HEIGHT)

            logic.update_bullets(WIDTH)

            ui.draw_scores(logic.red_score, logic.yellow_score)
            ui.draw_middle_line()
            red_ship.draw(screen)
            yellow_ship.draw(screen)
            ui.draw_bullets(logic.red_bullets, logic.yellow_bullets)

            if logic.red_score <= 0:
                handle_game_end("Yellow Wins!")

            if logic.yellow_score <= 0:
                handle_game_end("Red Wins!")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == RED_CONTROLS['shoot']:
                        logic.fire_bullet(is_red=True)
                    if event.key == YELLOW_CONTROLS['shoot']:
                        logic.fire_bullet(is_red=False)

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()