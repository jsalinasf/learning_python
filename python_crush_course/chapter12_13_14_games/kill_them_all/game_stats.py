
class GameStats():
    """Tracks analytics of the game"""
    def __init__(self, ai_settings):
        """Initialize Statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Kill Them all in INactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.characters_left = self.ai_settings.character_limit
        self.score = 0
        self.enemies_shoot = 0
