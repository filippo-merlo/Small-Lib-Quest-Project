### Import all the usefull libraries 
import pygame, sys
from settings import *
from debug import debug
from level import Level
from start_and_end_menu import menu


### Create the Game class
class Game:
    def __init__(self):
        ## Initiate pygame
        pygame.init() 
        ## Create the display surface, the window where the game will run 
        info = pygame.display.Info()
        size = (info.current_w, info.current_h)
        pygame.display.set_mode(size, pygame.FULLSCREEN)
        pygame.display.set_caption('Small Lib Quest') # Set the window's name
        self.clock = pygame.time.Clock() # create a clock object to set a celing for the frame rate on which the update of the screen will be performed
        # Imprt music and initialize level class
        pygame.mixer.music.load('./data/sound/zelda_theme_8_bit.mp3') # import music file
        self.level = Level() # Create the Level object imported from level.
        self.menu = menu()

    ### Create the while loop that will update the screen each frame
    def run(self):
        pygame.mixer.music.play() #Play the music
        #pygame.mixer.music.set_volume(0)
        while True:
            ## Set the Quit  button
            for event in pygame.event.get(): # Get the vector with all the events (input from the user) 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit() # quit pygame
                        sys.exit() # quit the while loop
                    
            ### Starting Menu

            ### Run the level object and update
            self.level.run() # run the Level Object
            self.menu.run()
    
            if pygame.mixer.music.get_pos() >= 2.37*60000:
                pygame.mixer.music.fadeout(6000)

            if pygame.mixer.music.get_pos() == -1:
                 pygame.mixer.music.play()
            
            #pygame.mixer.music.set_volume(0)

            
            self.clock.tick(FPS) # set the maximum frame rate
            pygame.display.update() # this method will update the screen at each iteration of the while loop
           

### Run the game with .run() method
if __name__ == '__main__': # If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
                           # __name__ is a built-in variable which evaluates to the name of the current module
    game = Game()
    game.run()
