import pygame
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


from settings import Settings
from character import Character
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Kill Them All")

    # Make the Play Button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # Make a Character
    character = Character(ai_settings, screen)

    # Make a group to store the bullets in
    bullets = Group()

    # Make a group to store enemies in
    enemies = Group()

    # Create the Fleet of enemies
    gf.create_fleet(ai_settings, screen, enemies)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, character, enemies, bullets)

        if stats.game_active:
            character.update()
            gf.update_bullets(ai_settings, screen, stats, sb, character, enemies, bullets)
            gf.update_enemies(ai_settings, stats, screen, character, enemies, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, character, enemies, bullets, play_button)

run_game()
