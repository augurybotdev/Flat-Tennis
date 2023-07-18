import pygame

class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score1 = 0
        self.score2 = 0

    def increment_score(self, player):
        if player == 1:
            self.score2 += 1
        elif player == 2:
            self.score1 += 1

    def draw(self, screen):
        score_text = self.font.render(f"{self.score1} - {self.score2}", True, (255, 255, 255))
        screen.blit(score_text, (375, 550))
