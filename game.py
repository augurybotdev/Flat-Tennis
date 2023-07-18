import pygame
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from speeddisplay import SpeedDisplay

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font('Courier New.ttf', 19)
        self.large_font = pygame.font.SysFont('Courier New Bold.ttf', 22*3, bold=True)
        self.medium_font = pygame.font.SysFont('Courier New.ttf', 22*2)
        self.small_medium_font = pygame.font.SysFont('Courier New.ttf', 22)
        self.clock = pygame.time.Clock()
        self.paddle1 = Paddle(50, 300)
        self.paddle2 = Paddle(750, 300)
        self.ball = None
        self.scoreboard = Scoreboard()
        self.speed_display = SpeedDisplay()
        self.speed = 4
        self.paused = True
        self.welcome_message_lines = [
            "Greetings!",
            "",
            "We are coming to you LIVE",
            "from the 2nd Dimension",
            "",
            "and straight from the heart",
            "of the people's republic in the land of Flat",
            "and in conjunction with and in support of",
            "augurybot; e-sports production division:",
            ""
            "it's the first ever, ",
            "competitive live action inter-demensional tournament",
            "we proudly present to you ",
            "the final match to crown the champion: its...",
            "",
            "",
            "",
            "FLAT-TENNIS",
            ""
            "dimenional championship",
            "",
            "",
            "Press Enter/Return",
        ]
        self.instructions_lines = [
            "INSTRUCTIONS",
            "",
            "serve new ball ------- ENTER     ",
            "left paddle up ------- W         ",
            "left paddle down ----- S         ",
            "right paddle up ------ UP ARROW  ",
            "right paddle down ---- DOWN ARROW",
            "game speed ----------- 0-9       ",
            "",
            "",
            "to begin - press ENTER",
        ]

    def show_screen(self, lines):
        self.screen.fill((0, 0, 0))        
        line_spacing = int(self.font.get_height() * 0.1)  
        total_text_height = sum((self.get_font_for_line(line).get_height() + line_spacing) for line in lines)        
        start_y = (self.screen.get_height() - total_text_height) / 2
        y = start_y
        for i, line in enumerate(lines):
            font = self.get_font_for_line(line)
            text_surface = font.render(line, True, (255, 255, 255))            
            x = (self.screen.get_width() - text_surface.get_width()) / 2            
            self.screen.blit(text_surface, (x, y))            
            y += font.get_height() + line_spacing
        pygame.display.flip()

    def get_font_for_line(self, line):
        if line == "FLAT-TENNIS":
            return self.large_font
        elif line == "INSTRUCTIONS":
            return self.medium_font
        elif line == "Greetings!":
            return self.small_medium_font
        else:
            return self.font
        
    def wait_for_enter(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddle1.move_up(self.speed)
        if keys[pygame.K_s]:
            self.paddle1.move_down(self.speed)
        if keys[pygame.K_UP]:
            self.paddle2.move_up(self.speed)
        if keys[pygame.K_DOWN]:
            self.paddle2.move_down(self.speed)
        if keys[pygame.K_RETURN]:
            if self.paused:
                self.ball = Ball(400, 300, self.speed)
                self.paused = False
            else:
                self.ball = None
                self.paused = True
        for i in range(1, 10):
            if keys[getattr(pygame, 'K_KP{}'.format(i))]:
                self.speed = i
                self.speed_display.set_speed(i)

    def update(self):
        if not self.paused and self.ball is not None:
            self.ball.move()
            if self.ball.collides_with(self.paddle1) or self.ball.collides_with(self.paddle2):
                self.ball.bounce()
            if self.ball.out_of_bounds():
                self.scoreboard.increment_score(self.ball.out_of_bounds())
                self.ball = None
                self.paused = True

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        if self.ball is not None:
            self.ball.draw(self.screen)
        self.scoreboard.draw(self.screen)
        self.speed_display.draw(self.screen)

    def run(self):
        self.show_screen(self.welcome_message_lines)
        self.wait_for_enter()

        self.show_screen(self.instructions_lines)
        self.wait_for_enter()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.handle_input()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()
