import pygame
import random

class Ball:
    def __init__(self, x, y, speed):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.dx = random.choice((-1, 1)) * speed
        self.dy = random.choice((-1, 1)) * speed

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.y < 0 or self.rect.y > 585:
            self.dy *= -1

    def bounce(self):
        self.dx *= -1

    def out_of_bounds(self):
        if self.rect.x < 0:
            return 1
        if self.rect.x > 785:
            return 2
        return 0

    def collides_with(self, paddle):
        return self.rect.colliderect(paddle.rect)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
