import pygame

class Immunity:
    """ Class that manages immunity level of person object """
    def __init__(self, covid_game):
        """ Initializes Immunity properties"""
        self.screen = covid_game.screen
        self.settings = covid_game.settings
        self.screen_rect = self.screen.get_rect()

        self.level = 10
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 20)

        #display immunity text
        self.text = self.font.render("Immunity Level:", True, self.text_color,
        self.settings.bg_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.topright = self.screen_rect.topright
   	    
    def increase_immunity_level(self):
        """ Increases immunity level """
        self.level += self.settings.immune_boost

    def decrease_immunity_level(self):
        """ Decreases immunity level """
        if self.level != -1:
            self.level -= 1	

    def update(self):
        """ updates immunity level for person object """
        level = str(self.level)
        self.image = self.font.render(level, True, self.text_color,
        self.settings.bg_color)
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right - 20
        self.rect.top = 20
    	
    def show_level(self):
        """displays immunity level on the game screen """
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.image, self.rect)		
    	 	 		

    	    