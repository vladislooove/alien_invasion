import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_app():
    # Inits game and creates screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion") 
    
    # Running main game loop
    while True:
        gf.check_events(ship)
        gf.update_screen(settings, screen, ship)
        ship.update()

run_app()