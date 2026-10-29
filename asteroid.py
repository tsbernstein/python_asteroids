import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)

            v1 = pygame.math.Vector2.rotate(self.velocity, angle)
            v2 = pygame.math.Vector2.rotate(self.velocity, -angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            [x, y] = self.position

            asteroid_1 = Asteroid(x, y, new_radius)
            asteroid_1.velocity = v1 * 1.2

            asteroid_2 = Asteroid(x, y, new_radius)
            asteroid_2.velocity = v2 * 1.2
