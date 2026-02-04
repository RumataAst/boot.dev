import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

# Bullets that are represented by smaller circles

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        color = "red"
        pygame.draw.circle(screen, color, self.position, SHOT_RADIUS, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

