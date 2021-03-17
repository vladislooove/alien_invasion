import sys
import pygame

def run_app():
    # Inits game and creates screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion") 

    # Running main game loop
    while True:
        # Catching keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # Display the last rendered screen
            pygame.display.flip()

run_app()