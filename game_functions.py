import sys
import pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship, bullets, aliens):
    # Set screen background            
    screen.fill(settings.bg_color)

    # Draw ship on the screen
    ship.blitme()

    # Draw aliens on the screen
    aliens.draw(screen)

    # Update all bullets position
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Display the last rendered screen
    pygame.display.flip()

def update_bullets(bullets):
    # Update bullets position
    bullets.update()

    # Remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(settings, screen, ship, bullets):
    new_bullet = Bullet(settings, screen, ship)

    if (len(bullets) <= settings.bullets_allowed):
        bullets.add(new_bullet)

def get_aliens_number_x(settings, screen):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - alien_width
    return int(available_space_x / alien_width)

def create_alien(settings, screen, aliens, index):
    alien = Alien(settings, screen)
    alien.x = alien.rect.width + 0 if index == 0 else 1 * alien.rect.width * index
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(settings, screen, aliens):
    number_aliens_x = get_aliens_number_x(settings, screen)

    for index in range(number_aliens_x):
        create_alien(settings, screen, aliens, index)
