from pong.constants import BALL_RADIUS, BALL_COLOR, SCREEN_SIZE
import pygame

TOP_RECT =  pygame.Rect(0, 0, SCREEN_SIZE[0], 1)
BOTTOM_RECT = pygame.Rect(0, SCREEN_SIZE[1], SCREEN_SIZE[0], SCREEN_SIZE[1])


class Ball:
    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.radius = BALL_RADIUS
        self.color = BALL_COLOR
        self.movement = pygame.Vector2(0, -2)
        self.bounding_box = pygame.Rect(0, 0, 40, 40)
        self.bounding_box.center = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self):
        self.position += self.movement
        self.bounding_box.center = self.position
        if self.bounding_box.collidelist([BOTTOM_RECT, TOP_RECT]) != -1:
            self.movement.y = -self.movement.y
