### Import all the usefull libraries 
import pygame, sys
from pathlib import Path
from settings import *
from level import Level
from start_and_end_menu import Menu

### CREATE THE GAME CLASS, THIS IS THE CLASS THAT HAS TO BE RAN
class Game:
    def __init__(self):
        ## Initiate pygame
        pygame.init() 
        ## Create the display surface, the main surface where all the games images will be printed 
        info = pygame.display.Info() # get the info of the display
        size = (info.current_w, info.current_h) #from info get the size of the display Width and Height
        pygame.display.set_mode(size, pygame.FULLSCREEN) # set the display surface in FULLSCREEN mode
        pygame.display.set_caption('Small Lib Quest') # Set the window's name
        self.clock = pygame.time.Clock() # create a clock object to set a celing for the frame rate on which the update of the screen will be performed
        ## Import music
        pygame.mixer.music.load(Path('./data/sound/zelda_theme_8_bit.mp3')) # import music file
        ## Instantiate the level class (containing the whole game) and the menu class (containing the functions to print the start and the end screens)
        self.level = Level() # Create the Level object imported from level.
        self.menu = Menu() # Instantiate menu class
        self.start = True # If true the start screen is printed, if false the self.level instrance is runned, and the game start

        self.switch_music = True
    

### Create the while loop that will update the screen each frame
    def run(self):
        pygame.mixer.music.play() #Play the music
        while True: #while the game is open --> everything will pass through here
            ## Set the Quit  button
            for event in pygame.event.get(): # Get the vector with all the events (input from the user) 
                if event.type == pygame.KEYDOWN: #if you press a key
                    if event.key == pygame.K_ESCAPE: #and the key is <ESCAPE>
                        pygame.quit() # quit pygame
                        sys.exit() # quit the while loop
                    if event.key == pygame.K_RETURN: #Key to press to start the game after the introduction screen
                        self.start = False #variable to check if the introduction screen has to be shown or not
                    
            ## other events in the main loop        
            if self.start: #if the game is open (this variable is intialized at True)
                self.menu.start_menu() #show the itro screen

            if self.start == False and self.level.testi.endgame == False: #start become false after closing the intro screen, and endgame is intialized as False
                ## Run the level object from Level class with all the functions we need in the Game
                self.level.run() # run the Level Object
                ## When the music file reproduction finish restart the music
                if pygame.mixer.music.get_pos() >= 2.37*60000: # get the music timing and compare with the duration of the music file
                    pygame.mixer.music.fadeout(6000) # set a fadeout for ending the music reproduction
                if pygame.mixer.music.get_pos() == -1: # when the fadeout is performed the timing become -1
                    pygame.mixer.music.play() # start a new music file reproduction

            if self.level.testi.endgame: #if endgame is reached
                if self.switch_music: #if variable switch music is True (is initialized as True)
                    pygame.mixer.music.load(Path('./data/sound/Hudson Mohawke - Cbat.mp3')) #load the new music
                    pygame.mixer.music.play() #and play it
                    self.switch_music = False #then swithc music become false
                if pygame.mixer.music.get_pos() <= 0.415*60000: #if music-time is under a certain amount of time played
                    self.level.run() #run the level method (the if statement is out of the other one, because we wanted to change music)
                if pygame.mixer.music.get_pos() >= 0.415*60000: #if the music is over a certain amount of time played
                    self.menu.end_screen() #run the end screen

            #if self.level.testi.endgame: #if the var that check for the endgame (from dialogues in testi class) is True then
            #    self.menu.end_screen() #show the end screen
            
            self.clock.tick(FPS) # set the maximum frame rate (from settings.py)
            pygame.display.update() # this method will update the screen at each iteration of the while loop
           
### Run the game with .run() method
if __name__ == '__main__': # If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
                           # __name__ is a built-in variable which evaluates to the name of the current module
    game = Game() # Instantiate the game class
    game.run() # Start the game while loop