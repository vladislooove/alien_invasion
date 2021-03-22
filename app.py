import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_app():
    # Inits game and creates screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen)
    alien = Alien(settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings, screen, aliens)
    pygame.display.set_caption("Alien Invasion") 
    
    # Running main game loop
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(settings, screen, ship, bullets, aliens)
        gf.update_bullets(bullets)

run_app()