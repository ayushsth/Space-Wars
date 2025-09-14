import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

class UI:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font_small = pygame.font.SysFont('times new roman', 20)
        self.font_score = pygame.font.SysFont('times new roman', 30)
        self.font_large = pygame.font.SysFont('times new roman', 60)
        self.font_medium = pygame.font.SysFont('times new roman', 40)

    def draw_scores(self, red_score, yellow_score):
        red_score_text = self.font_score.render(f"Score: {red_score}", True, WHITE)
        yellow_score_text = self.font_score.render(f"Score: {yellow_score}", True, WHITE)
        self.screen.blit(red_score_text, (30, 20))
        self.screen.blit(yellow_score_text, (self.width - 150, 20))

    def draw_middle_line(self):
        pygame.draw.line(self.screen, WHITE, (self.width / 2, 0), (self.width / 2, self.height), 5)

    def draw_spaceships(self, red, yellow):
        self.screen.blit(red.image, (red.rect.x, red.rect.y))
        self.screen.blit(yellow.image, (yellow.rect.x, yellow.rect.y))

    def draw_bullets(self, red_bullets, yellow_bullets):
        for bullet in red_bullets:
            pygame.draw.rect(self.screen, RED, bullet.rect)
        for bullet in yellow_bullets:
            pygame.draw.rect(self.screen, YELLOW, bullet.rect)

    def draw_winner(self, winner_text):
        winner_font = pygame.font.SysFont('ariel', 60)
        text = winner_font.render(winner_text, True, YELLOW)
        rect = text.get_rect(center=(self.width / 2, self.height / 2))
        self.screen.blit(text, rect)

    def draw_play_again(self):
        replay_font = pygame.font.SysFont('ariel', 40)
        play_again_text = replay_font.render("Press X to Quit! Press P to Play Again!", True, YELLOW)
        rect = play_again_text.get_rect(center=(self.width / 2, self.height / 2 + 60))
        self.screen.blit(play_again_text, rect)
