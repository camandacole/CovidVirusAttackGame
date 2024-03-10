import pygame
from pygame.sprite import Sprite
import random

class Virus(Sprite):
    """ A Class that manages a virus object """
    def __init__(self, covid_game):
        """Initialize the Virus and set its starting position."""
        super().__init__()
        self.screen = covid_game.screen
        self.settings = covid_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the virus image and get its rect.
        self.image = pygame.image.load('img/virus.bmp')
        self.image = self.scale_pic(self.image)
        self.rect = self.image.get_rect()

        #set random position for each virus object
        self.rect.midtop = (random.randint(5, self.settings.screen_width-10), 
        random.randint(-(self.settings.screen_height + 100), 0))

        #set speed of virus object
        self.virus_speed = self.settings.virus_speed

    def scale_pic(self, image):
        """ Scale virus image by reducing its initial size"""
        new_img = pygame.transform.smoothscale(image, (50, 50))
        return new_img

    def update(self):
        """ updates virus movement """
        self.rect.move_ip(0, self.virus_speed)