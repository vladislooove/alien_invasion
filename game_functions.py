import sys
import pygame

def check_events(ship):
    # Catching keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right += True
            elif event.key == pygame.K_LEFT:
                ship.moving_left -= True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(settings, screen, ship):
    # Set screen background            
    screen.fill(settings.bg_color)

    # Draw ship on the screen
    ship.blitme()

    # Display the last rendered screen
    pygame.display.flip()