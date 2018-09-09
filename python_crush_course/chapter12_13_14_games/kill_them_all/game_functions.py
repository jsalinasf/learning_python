import pygame
import sys
import random
from time import sleep

from bullet import Bullet
from enemy import Enemy


def check_fleet_edges(enemies):
    """Respond appropriately if any enemies have reached the edge"""
    for enemy in enemies:
        if enemy.check_edges():
            return True


def update_enemies(ai_settings, stats, screen, character, enemies, bullets):
    """Update the positions of all enemies in the fleet"""
    if not(check_fleet_edges(enemies)):
        enemies.update()
    else:
        # Enemy reach the left of the screen
        character_hit(ai_settings, stats, screen, character, enemies, bullets)

    if pygame.sprite.spritecollideany(character, enemies):
        character_hit(ai_settings, stats, screen, character, enemies, bullets)


def should_create_enemy(ai_settings):
    """Evaluates if an enemy should be created based on game difficulty"""
    create_enemy_yes = int(ai_settings.enemy_possibility)
    create_enemy_no = int(100 - ai_settings.enemy_possibility)
    weighted_choices = [('Yes', create_enemy_yes), ('No', create_enemy_no)]
    population = [val for val, cnt in weighted_choices for i in range(cnt)]
    flag = random.choice(population)
    if flag == "Yes":
        choice = True
    elif flag == "No":
        choice = False
    return choice


def get_number_enemies(ai_settings, enemy_height):
    """Determine the number of enemies in a column"""
    number_enemies_y = int(ai_settings.screen_height / enemy_height)
    return number_enemies_y


def create_enemy(ai_settings, screen, enemies, enemy_number, enemy_vertical_separation, enemy_height, column_number):
    """Create and place an enemy in a column"""
    enemy = Enemy(ai_settings, screen)
    enemy.y = (enemy_vertical_separation * (enemy_number + 1)) + (enemy_height * enemy_number)
    if enemy_number == 0:
        enemy.y = enemy_vertical_separation
    enemy.rect.y = enemy.y
    enemy.x = ai_settings.screen_width + (enemy.rect.width + 2 * enemy.rect.width * column_number)
    enemy.rect.x = enemy.x
    enemies.add(enemy)


def create_fleet(ai_settings, screen, enemies):
    """Create a full wave of Enemies"""
    # Create an enemy and find the number of enemies in a row
    #  Spacing between each enemy is equal to one enemy
    enemy = Enemy(ai_settings, screen)
    enemy_height = enemy.rect.height
    number_enemies_y = get_number_enemies(ai_settings, enemy_height)
    left_over = int(ai_settings.screen_height % enemy_height)
    enemy_vertical_separation = left_over / (number_enemies_y + 1)

    # Create fleet row of Enemies
    for column_number in range(ai_settings.enemy_columns):
        for enemy_number in range(number_enemies_y):
            if should_create_enemy(ai_settings):
                create_enemy(ai_settings, screen, enemies, enemy_number, enemy_vertical_separation, enemy_height,
                             column_number)


def fire_bullet(ai_settings, screen, character, bullets):
    """Fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, character)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, character, bullets):
    if event.key == pygame.K_UP:
        # Move the Character UP
        character.move_up = True
    elif event.key == pygame.K_DOWN:
        # Move the Character DOWN
        character.move_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, character, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, character):
    if event.key == pygame.K_UP:
        # Stop moving Character UP
        character.move_up = False
    elif event.key == pygame.K_DOWN:
        # Stop moving Character DOWN
        character.move_down = False


def check_play_button(ai_settings, screen, stats, play_button, character, enemies, bullets, mouse_x, mouse_y):
    """start a new game when player click Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Reset game settings.
        ai_settings.initialize_dynamic_settings()

        #  Hide the mouse cursor
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        # Empty the list of Enemies and Bullets
        enemies.empty()
        bullets.empty()

        # Create a New Fleet and center the character
        create_fleet(ai_settings, screen, enemies)
        character.center_character()


def check_events(ai_settings, screen, stats, play_button, character, enemies, bullets):
    """Respond to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, character, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, character, enemies, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, sb, character, enemies, bullets, play_button):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)

    # Draw the score information
    sb.show_score()

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    character.blitme()
    enemies.draw(screen)

    # Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def check_bullet_enemies_collisions(ai_settings, screen, stats, sb, character, enemies, bullets):
    """Respond to bullet-enemy collisions."""
    # Remove any bullets and enemies that have collided

    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)

    if collisions:
        for enemies in collisions.values():
            stats.score += ai_settings.enemy_points * len(enemies)
            stats.enemies_shoot += 1
        sb.prep_score()

    if len(enemies) == 0:
        # Destroy existing bullets and create new fleet
        bullets.empty()
        increase_game_speed(ai_settings)
        create_fleet(ai_settings, screen, enemies)


def increase_game_speed(ai_settings):
    ai_settings.increase_enemy_possibility()
    ai_settings.increase_enemy_speed()
    ai_settings.increase_enemy_columns()


def update_bullets(ai_settings, screen, stats, sb, character, enemies, bullets):
    """Update position of bullets and get rif of old bullets."""
    # Update bullets position
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.right > ai_settings.screen_width:
            bullets.remove(bullet)

    check_bullet_enemies_collisions(ai_settings, screen, stats, sb, character, enemies, bullets)


def character_hit(ai_settings, stats, screen, character, enemies, bullets):
    """Respond to Character being reached by Enemies."""

    if stats.characters_left > 0:
        # Decrement characters_left - AKA: Player lifes
        stats.characters_left -= 1

        # Create a new fleet and center the character
        create_fleet(ai_settings, screen, enemies)
        character.center_character()

        # Pause
        sleep(1.0)

        # Empty the list of Enemies and bullets
        enemies.empty()
        bullets.empty()

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

