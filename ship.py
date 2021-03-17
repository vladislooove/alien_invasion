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

  def blitme(self):
    # Draws ship at current position
    self.screen.blit(self.image, self.rect)

