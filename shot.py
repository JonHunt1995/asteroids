import pygame
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.velocity = pygame.Vector2(0, 0)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

  def update(self, dt):
    self.position += (self.velocity * dt)
    #if self.position.x > SCREEN_WIDTH:
      #self.position = 0
    #elif self.position.x < 0:
      #self.position = SCREEN_WIDTH
    #if self.position.y > SCREEN_HEIGHT:
      #self.position.y = 0
    #elif self.position.y < 0:
      #self.position.y = SCREEN_HEIGHT
