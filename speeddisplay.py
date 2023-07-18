import pygame

class SpeedDisplay:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.speed = 4

    def set_speed(self, speed):
        self.speed = speed

    def draw(self, screen):
        speed_text = self.font.render(f"Speed: {self.speed}", True, (255, 255, 255))
        screen.blit(speed_text, (375, 500))
