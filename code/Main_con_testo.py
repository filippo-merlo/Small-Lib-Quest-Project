import pygame, sys
from settings import * #import everything from settings
from level import Level
from dialogbox import MyWindow
from text import testi


class Game:
    def __init__(self):
        #general setup
        pygame.init() #initatione pygame
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) #initiating the screengame
        pygame.display.set_caption("L'ineluttabile insofferenza dell'essere") #game name
        self.clock = pygame.time.Clock() #initiating the clock
        self.level = Level() #instance of level class
        self.testo = testi() #instance of text class
        self.window = MyWindow(self.testo.dialogues()) #instance of the text method
        


    def run(self):
        
        while True:
            for event in pygame.event.get():#event loop, everything pass thru here
                if event.type == pygame.QUIT: #checking if we are closing the game
                    pygame.quit()
                    sys.exit()
                # Check if the left mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.window.toggle_dialog_box() #change from False to True or viceversa
                   

            self.screen.fill('red') #color of the screen
        
                  
            #debug('INSERT HERE WHAT I WANT TO DISPLAY')
            self.level.run() #run the class in the main loop
            # If the dialogue box should be shown, draw it on the screen
            if self.window.show_dialog_box: #if the text box has to be shown (is True)
                self.window.run_window(self.screen) #then shown it
            pygame.display.update() #uptading the screen
            self.clock.tick(FPS) #at this frame rate

### Run the game with .run() method
if __name__ == '__main__': # If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
                           # __name__ is a built-in variable which evaluates to the name of the current module
    game = Game()
    game.run()
