import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        f1_rotated = self.velocity.rotate(random_angle)
        f2_rotated = self.velocity.rotate(-random_angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1], new_radius)
        a1.velocity = f1_rotated * 1.2
        a2 = Asteroid(self.position[0], self.position[1], new_radius)
        a2.velocity = f2_rotated * 1.2
