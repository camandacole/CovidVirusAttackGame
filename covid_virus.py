import sys
from time import sleep
from settings import Settings

import pygame
from person import Person
from immunity import Immunity
from vaccine import Vaccine
from virus import Virus
from background import Background

class CovidVirusAttack:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode([self.settings.screen_width, 
        self.settings.screen_height])
        self.isRunning = True

        #initilize clock to slow the rate of frames per second
        self.clock = pygame.time.Clock()

        #music 
        pygame.mixer.music.load("sounds/626083__josefpres__8-bit-game-loop-"+
        "010-simple-mix-1-long-120-bpm.wav")
        pygame.mixer.music.play(loops=-1)

        self.hit_sound = pygame.mixer.Sound("sounds/coin2.mp3")

        #Initialize game objects 
        self.person = Person(self)

        # initialize groups
        self.viruses = pygame.sprite.Group()
        self.vaccines = pygame.sprite.Group()

        #initialize backgound
        self.background = Background(self)

        # initialize immunity object for person
        self.immunity = Immunity(self)

        # call method to create vaccines and virus
        self.create_viruses()
        self.create_vaccines()
      
    def run_game(self):
        """Start the main loop for the game."""
        while self.isRunning:
            self._check_events()
            self.person.update()
            self.update_viruses()
            self.update_vaccines()
            self.immunity.update()
            self.update_screen()
    

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                self._check_mousedown_events(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._check_mouseup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.person.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.person.moving_left = True
        elif event.key == pygame.K_UP:
            self.person.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.person.moving_down = True       
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.person.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.person.moving_left = False
        elif event.key == pygame.K_UP:
            self.person.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.person.moving_down = False 


    def _check_mousedown_events(self, event): 
        """ Responds to mouse down events """
        if event.button == 1:
            self.person.moving_left = True
        elif event.button == 3:
            self.person.moving_right = True 
                               

    def _check_mouseup_events(self, event): 
        """ Responds to mouse up events"""
        if event.button == 1:
            self.person.moving_left = False
        elif event.button == 3:
            self.person.moving_right = False          


    def create_viruses(self):
        """ Create Virus objects and add to group """
        for i in range(1,self.settings.num_of_virus):
            virus = Virus(self)
            self.viruses.add(virus)         
   
    def update_viruses(self):
        """ Updates virus movement and checks for collision"""
        for virus in self.viruses.sprites():
            self.check_bottom(virus, self.viruses)
        
        if len(self.viruses) == 0:
            self.create_viruses()

        self.viruses.update()
        for virus in self.viruses.sprites():
           isCollide = pygame.Rect.colliderect(self.person.rect, virus.rect)
           if isCollide:
             self.immunity.decrease_immunity_level()
             self.viruses.remove(virus)
             self.hit_sound.play()
           if self.immunity.level == -1:
              self.end_game()
              isRunning = False


    def update_vaccines(self):
        """ Updates vaccine movement and checks for
        collision with person object """
        for vaccine in self.vaccines.sprites():
            self.check_bottom(vaccine, self.vaccines)
        
        if len(self.vaccines) == 0:
            self.create_vaccines()

        self.vaccines.update()
        for vaccine in self.vaccines.sprites():
           isCollide = pygame.Rect.colliderect(self.person.rect, vaccine.rect)
           if isCollide:
              self.immunity.increase_immunity_level()
              self.vaccines.remove(vaccine)
              self.hit_sound.play()


    def check_bottom(self, game_object, object_group):
        """ Checks if game object has reach end of sccreen and removes 
        it from group. """
        if game_object.rect.bottom > self.screen.get_rect().bottom:
            object_group.remove(game_object)
                   

    def create_vaccines(self):
        """ create vaccines objects """
        for i in range(1,self.settings.num_of_vac):
            vaccine = Vaccine(self)
            self.vaccines.add(vaccine)
            

    def end_game(self):
        """ display game over text on screen and stops game loop"""
        self.isRunning = False
        #display Game over text
        text_color = (30, 30, 30)
        font = pygame.font.SysFont(None, 56)
        text = font.render("Game Over", True, text_color, 
        self.settings.bg_color)
        text_rect = text.get_rect()
        text_rect.center = self.screen.get_rect().center
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        sleep(0.5)          
          

    def update_screen(self):
        """ Update screen to redraw game"""
        self.screen.fill((230, 230, 230))
        self.background.show_background()
        self.person.blitme()
        self.viruses.draw(self.screen)
        self.vaccines.draw(self.screen)
        self.immunity.show_level()
        pygame.display.flip()
        self.clock.tick(200)
           
  
if __name__ == '__main__':
    # Make a game instance, and run the game.
    virus = CovidVirusAttack()
    virus.run_game()