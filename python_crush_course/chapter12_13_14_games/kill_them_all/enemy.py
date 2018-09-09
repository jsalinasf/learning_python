import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """A class to represent a single enemy in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the enemy and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the enemy image and set its rect attribute
        self.image = pygame.image.load("images/enemy.bmp")
        self.rect = self.image.get_rect()

        # Start each new enemy at the top right of the screen
        self.rect.x = self.rect.width

        # Store a decimal value for the Enemy's center
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the enemy at its current position."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if Enemy is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """Move Enemy left."""
        self.x += (self.ai_settings.enemy_speed_factor * -1)
        self.rect.x = self.x
