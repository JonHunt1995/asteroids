import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

  def update(self, dt):
    self.position += (self.velocity * dt)
  # If asteroid gets hit, it gets split into two smaller asteroids
  # If the asteroid is too small, then 
  def split(self):
    old_velocity = self.velocity
    old_radius = self.radius
    self.kill()

    if old_radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_angle = random.uniform(20, 50)
    velocity1 = old_velocity.rotate(random_angle)
    velocity2 = old_velocity.rotate(-random_angle)
    new_radius = old_radius - ASTEROID_MIN_RADIUS
    asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteroid1.velocity = velocity1
    asteroid2.velocity = velocity2
    asteroid1.velocity *= 1.2
    asteroid2.velocity *= 1.2


    
    