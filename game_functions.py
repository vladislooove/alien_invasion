import sys
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    # Catching keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)

def check_key_down_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets):
    # Set screen background            
    screen.fill(settings.bg_color)

    # Draw ship on the screen
    ship.blitme()

    # Display the last rendered screen
    pygame.display.flip()

    # Update all bullets position
    for bullet in bullets.sprites():
        bullet.draw_bullet()