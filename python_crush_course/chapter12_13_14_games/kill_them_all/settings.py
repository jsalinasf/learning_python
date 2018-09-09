
class Settings:
    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Settings
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (102, 178, 255)

        # Character Settings
        self.character_speed_factor = 2
        self.character_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 4

        # Enemy Settings
        self.enemy_possibility = 5  # % Possibility for an enemy to show in a row
        self.enemy_percentage_increase = 1.1  # % of Increment of self.enemy_possibility
        self.enemy_columns = 1  # How many Columns of Enemies are going to attack the character
        self.enemy_speed_factor = 0.1  # How fast Enemies move from right to left
        self.enemy_speed_factor_increase = 0.05  # How fast Enemies speed up

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change through the game."""
        self.enemy_possibility = 5  # % Possibility for an enemy to show in a row
        self.enemy_percentage_increase = 1.1  # % of Increment of self.enemy_possibility
        self.enemy_columns = 1  # How many Columns of Enemies are going to attack the character
        self.enemy_speed_factor = 0.1  # How fast Enemies move from right to left
        self.enemy_speed_factor_increase = 0.05  # How fast Enemies speed up
        self.enemy_points = 50

    def increase_enemy_possibility(self):
        self.enemy_possibility *= self.enemy_percentage_increase

    def increase_enemy_columns(self):
        self.enemy_columns += 1

    def increase_enemy_speed(self):
        self.enemy_speed_factor += self.enemy_speed_factor_increase
