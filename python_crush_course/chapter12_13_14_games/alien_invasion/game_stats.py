class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize Statistics."""
        self.ai_settings = ai_settings
        self.game_active = True
        self.ships_left = self.ai_settings.ship_limit

    def reset_stats(self, ai_settings):
        """Initialize statistics that can change during the game."""
        self.ships_left = ai_settings.ship_limit

