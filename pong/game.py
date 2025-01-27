import pygame

from pong.ball import Ball
from pong.constants import SCREEN_SIZE, BALL_INITIAL_POSITION


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.ball = Ball(BALL_INITIAL_POSITION)


    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(40)
            self.ball.update()
            self.screen.fill("black")
            self.ball.draw(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False