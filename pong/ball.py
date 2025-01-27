from pong.constants import BALL_RADIUS, BALL_COLOR
import pygame

class Ball:
    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.radius = BALL_RADIUS
        self.color = BALL_COLOR
        self.movement = pygame.Vector2(1, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self):
        self.position += self.movement