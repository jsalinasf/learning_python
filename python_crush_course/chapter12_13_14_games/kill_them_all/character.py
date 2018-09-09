import pygame


class Character:
    """A class to represent the character controller by the human player"""

    def __init__(self, ai_settings, screen):
        """Initialize Game's main character."""

        self.screen = screen
        self.ai_settings = ai_settings

        # Load Character Image and set its starting position
        self.image = pygame.image.load("images/character.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the left center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the character's center
        self.center = float(self.rect.centery)

        # Movement flag
        self.move_up = False
        self.move_down = False

    def update(self):
        """Update the Character Positions based on the movement flag."""
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.character_speed_factor
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.character_speed_factor

        # Update rect object from self.center
        self.rect.centery = self.center

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_character(self):
        """Center the character on the screen"""
        self.center = self.screen_rect.centery
