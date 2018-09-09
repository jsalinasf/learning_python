import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the character."""

    def __init__(self, ai_settings, screen, character):
        """Create a bullet object at the character's current position."""

        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centery = character.rect.centery
        self.rect.right = character.rect.right

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet to the left of the screen."""
        # Update decimal position of the bullet
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = self.x


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

