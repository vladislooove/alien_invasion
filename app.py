import sys
import pygame

from settings import Settings
from ship import Ship

def run_app():
    # Inits game and creates screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion") 
    
    # Running main game loop
    while True:
        # Catching keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Set screen background            
            screen.fill(settings.bg_color)

            # Draw ship on the screen
            ship.blitme()

            # Display the last rendered screen
            pygame.display.flip()

run_app()