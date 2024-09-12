import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x_or_pos, y_or_radius, radius_or_velocity=None, velocity=None):
        if isinstance(x_or_pos, pygame.Vector2):
        # Handle Vector2 case
            super().__init__(x_or_pos.x,x_or_pos.y, y_or_radius)
            self.velocity = radius_or_velocity if radius_or_velocity is not None else pygame.Vector2(0, 0)
        else:
        # Handle separate x, y coordinates case
            super().__init__(x_or_pos, y_or_radius, radius_or_velocity)
            self.velocity = velocity if velocity is not None else pygame.Vector2(0, 0)

    def draw(self, screen):
         pygame.draw.circle(screen, "white",(self.position.x, self.position.y),self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        angle = random.uniform(20, 50)
        a1 =  pygame.math.Vector2.rotate(self.velocity, angle)
        a2 =  pygame.math.Vector2.rotate(self.velocity, -angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position, new_radius, a1 * 1.2)
        new_asteroid2 = Asteroid(self.position, new_radius, a2 * 1.2)
        self.kill()
        return new_asteroid1, new_asteroid2