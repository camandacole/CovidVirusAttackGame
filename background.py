import pygame
from pygame.sprite import Sprite
import random

class Background():
    """ A Class that sets background of display screen """
    def __init__(self, covid_game):
        """Initialize background properties"""
        super().__init__()
        self.screen = covid_game.screen
        self.settings = covid_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the background image and get its rect.
        self.image = pygame.image.load('img/background.bmp')
        self.image = self.scale_pic(self.image)
        self.rect = self.image.get_rect()
       
        self.rect.center = self.screen_rect.center

    def scale_pic(self, image):
        """ Scale background pic tp fit screen size """
        new_img = pygame.transform.smoothscale(image, 
        (self.settings.screen_width, self.settings.screen_height))
        return new_img    

    def show_background(self):
        """ display background on screen """
        self.screen.blit(self.image, self.rect)