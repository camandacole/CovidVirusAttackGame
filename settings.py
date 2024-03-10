import random

class Settings:
    """A class to store all settings for Covid Virus Attack game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 650
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # person settings
        self.person_speed = 1

        # virus settings
        self.virus_speed = random.randint(2, 3)
        self.num_of_virus = 12

        # vaccine settings
        self.vaccine_speed = 2
        self.num_of_vac = 3

        # immunity settings
        self.immune_boost = 1

        

