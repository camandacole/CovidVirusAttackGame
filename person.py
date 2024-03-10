import pygame
from pygame.sprite import Sprite

class Person(Sprite):
    """ A class to manage Person object  """

    def __init__(self, covid_game):
        """Initialize the person and set its starting position."""
        super().__init__()
        self.screen = covid_game.screen
        self.settings = covid_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('img/boy1.bmp')
        self.image = self.scale_pic(self.image)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def scale_pic(self, image):
        """ Scale vaccine immage by reducing its initial size"""
        new_img = pygame.transform.smoothscale(image, (90, 75))
        return new_img


    def update(self):
        """Update the persons position and checks boundaries"""
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.rect.move_ip(1, 0)
        if self.moving_left and self.rect.left > 0:
            self.rect.move_ip(-1, 0)
        if self.moving_up and self.rect.top >= 0:
            self.rect.move_ip(0, -1)
        if self.moving_down and self.rect.bottom <= self.settings.screen_height:
            self.rect.move_ip(0, 1)  
                   

    def blitme(self):
        """Draw the person at its current location."""
        self.screen.blit(self.image, self.rect)    
