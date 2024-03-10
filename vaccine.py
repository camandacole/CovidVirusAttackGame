import pygame
from pygame.sprite import Sprite
import random

class Vaccine(Sprite):
	""" A Class that is used to boosts players immunity level """
	def __init__(self, covid_game):
		"""Initialize the Vaccine and its properties"""
		super().__init__()
		self.screen = covid_game.screen
		self.settings = covid_game.settings
		self.screen_rect = self.screen.get_rect()

		# Load the vaccine image and get its rect.
		self.image = pygame.image.load('img/vaccine.bmp')
		self.image = self.scale_pic(self.image)
		self.rect = self.image.get_rect()

	    #Set random position for each virus object
		self.rect.midtop = (random.randint(5, self.settings.screen_width-10),
        random.randint(-(self.settings.screen_height + 500), 0))

		#set speed of vaccine object
		self.vaccine_speed = self.settings.vaccine_speed

	def scale_pic(self, image):
		""" Scale vaccine immage by reducing its initial size"""
		new_img = pygame.transform.smoothscale(image, (50, 50))
		return new_img	

	def update(self):
		""" update movement of vaccine to move down """
		self.rect.move_ip(0, self.vaccine_speed)
            



            


