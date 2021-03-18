import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # Class that represents enemy
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)