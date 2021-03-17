import pygame

class Ship():
  def __init__(self, screen):
    # Inits ship
    self.screen = screen
    self.image = pygame.image.load('images/ship.png')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    self.moving_right = False
    self.moving_left = False

  def blitme(self):
    # Draws ship at current position
    self.screen.blit(self.image, self.rect)

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.rect.centerx += 1

    if self.moving_left and self.rect.left > 0:
      self.rect.centerx -= 1