import pygame
import random

from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, NEW_ANGLE_ASTEROID_ONE, NEW_ANGLE_ASTEROID_TWO


# Asteroid class as enemies 
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = "white"
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        new_angle = random.uniform(NEW_ANGLE_ASTEROID_ONE, NEW_ANGLE_ASTEROID_TWO)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = pygame.math.Vector2.rotate(self.velocity, new_angle) * 1.2

        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two.velocity = pygame.math.Vector2.rotate(self.velocity, -new_angle) * 1.2



