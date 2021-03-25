import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group
from button import Button

def run_app():
    # Inits game and creates screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()
    stars = Group()
    stats = GameStats(settings)
    gf.create_fleet(settings, screen, aliens, ship)
    gf.create_stars(settings, screen, stars)
    pygame.display.set_caption("Alien Invasion")
    btn = Button(settings, screen, "Play")
    
    # Running main game loop
    while True:
        gf.check_events(settings, screen, ship, bullets, stats, btn, aliens)
        gf.update_screen(settings, screen, ship, bullets, aliens, stars, stats, btn)

        if stats.is_game_active:
            ship.update()
            gf.update_aliens(settings, screen, aliens, bullets, ship, stats)
            gf.update_bullets(bullets, aliens, settings, screen, ship)

run_app()