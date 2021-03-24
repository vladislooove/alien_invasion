import sys
import pygame
from random import randint
from bullet import Bullet
from alien import Alien
from star import Star
from time import sleep

def check_events(settings, screen, ship, bullets, stats, btn):
    # Catching keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if btn.rect.collidepoint(mouse_x, mouse_y):
                stats.is_game_active = True


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
    
def update_screen(settings, screen, ship, bullets, aliens, stars, stats, btn):
    if stats.is_game_active:
        # Set screen background            
        screen.fill(settings.bg_color)

        # Draw stars on the screen
        stars.draw(screen)

        # Draw ship on the screen
        ship.blitme()

        # Draw aliens on the screen
        aliens.draw(screen)

        # Update all bullets position
        for bullet in bullets.sprites():
            bullet.draw_bullet()
    else:
        btn.draw_button()

    # Display the last rendered screen
    pygame.display.flip()

def update_bullets(bullets, aliens, settings, screen, ship):
    # Update bullets position
    bullets.update()

    # Remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed

    settings.fleet_direction *= -1

def update_aliens(settings, screen, aliens, bullets, ship, stats):
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        handle_ship_hit(settings=settings, screen=screen, aliens=aliens, bullets=bullets, ship=ship, stats=stats)

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen.get_rect().bottom:
            handle_ship_hit(settings=settings, screen=screen, aliens=aliens, bullets=bullets, ship=ship, stats=stats)

def handle_ship_hit(settings, screen, aliens, bullets, ship, stats):
    stats.ships_left -= 1

    if stats.ships_left > 0:
        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.is_game_active = False

def fire_bullet(settings, screen, ship, bullets):
    new_bullet = Bullet(settings, screen, ship)

    if (len(bullets) <= settings.bullets_allowed):
        bullets.add(new_bullet)

def get_aliens_number_x(settings, screen):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - alien_width
    return int(available_space_x / alien_width)

def get_number_rows(settings, ship_height, alien_height):
    available_space_y = settings.screen_height - alien_height - ship_height
    return int(available_space_y / (1.5 * alien_height))

def create_alien(settings, screen, aliens, index, row_number):
    alien = Alien(settings, screen)
    alien.x = alien.rect.width + 0 if index == 0 else 1 * alien.rect.width * index
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(settings, screen, aliens, ship):
    alien = Alien(settings, screen)
    number_aliens_x = get_aliens_number_x(settings, screen)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_index in range(number_rows):
        for index in range(number_aliens_x):
            create_alien(settings, screen, aliens, index, row_index)

def create_stars(settings, screen, stars):
    for index in range(30):
        star = Star(settings, screen)
        x = randint(0, settings.screen_width)
        y = randint(0, settings.screen_height)
        star.x = x
        star.rect.x = x
        star.rect.y = y
        stars.add(star)