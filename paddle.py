import pygame

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 100)

    def move_up(self, speed):
        if self.rect.y > 0:
            self.rect.y -= 5 * speed

    def move_down(self, speed):
        if self.rect.y < 500:
            self.rect.y += 5 * speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
