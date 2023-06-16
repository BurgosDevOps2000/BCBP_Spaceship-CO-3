import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class YouDied:
    def __init__(self, score, max_score):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font_large = pygame.font.Font(None, 60)
        self.font_small = pygame.font.Font(None, 36)
        self.text_large = self.font_large.render("GAME OVER", True, (255, 0, 0))
        self.text_large_rect = self.text_large.get_rect()
        self.text_large_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        self.text_small = self.font_small.render(f"Score: {score}", True, (255, 255, 255))
        self.text_small_rect = self.text_small.get_rect()
        self.text_small_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        self.restart_text = self.font_small.render("Press ENTER to restart", True, (255, 255, 255))
        self.restart_text_rect = self.restart_text.get_rect()
        self.restart_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        self.text_max_score = self.font_small.render(f"Max Score: {max_score}", True, (255, 255, 255))
        self.text_max_score_rect = self.text_max_score.get_rect()
        self.text_max_score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)
        self.restart = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.restart:
                            self.reset_game()
                            self.restart = False
                        else:
                            running = False

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text_large, self.text_large_rect)
            self.screen.blit(self.text_small, self.text_small_rect)
            self.screen.blit(self.text_max_score, self.text_max_score_rect)
            self.screen.blit(self.restart_text, self.restart_text_rect)
            pygame.display.flip()

        pygame.quit()

    
