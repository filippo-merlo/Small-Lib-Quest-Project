import pygame
from pathlib import Path

from settings import *

### THIS FILE CONTAINS THE CLASS AND THE METHODS THAT WE ARE USING TO CALL THE DIALOGUE BOX THAT COINTAINS THE TEXT FOR THE INTERACTIONS

class DialogueBox:
    def __init__(self):
        self.screen_size = pygame.display.get_surface().get_size() #get the screen size

        self.height = 210 #Sets the height in pixels
        self.x = 30 # This will position the rectangle "offset" pixels from the left edge of the screen.
        self.y = self.screen_size[1] - self.height - self.x # Sets the y attribute to the height of the screen minus the height of the rectangle (75 pixels) minus the offset value.
        self.width = self.screen_size[0] - (self.x * 2) # Sets the width attribute to the width of the screen minus twice the offset value. This will reduce the width of the rectangle by "offset" pixels on each side.
        self.font = pygame.font.Font(Path("./graphics/font/font.ttf"), FONT_SIZE) #define font and size
        self.dialoguebox_sound =  pygame.mixer.Sound(Path('./data/sound/dialoguebox_sound.mp3')) #import sound for the dialogue box 
        self.show_dialoguebox = False #init dialogbox at False don't show

    ## Function to split the text in differnt lines based on the lenght of it 
    def blit_text(self, surface, text, pos, font, color=pygame.Color('White')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words of the current text to display
        space = font.size(' ')[0]   # The width of a space based on the font used
        max_width, max_height = surface.get_size() #get the width of height of the surface where the text has to be printed
        x, y = pos #get the position in where the text has to be printed
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color) #get the surface covered by the text
                word_width, word_height = word_surface.get_size() #it split the surface covered by the text in two variables
                if x + word_width >= max_width: #if adding another word would exceed the max width of the surface:
                    x = pos[0]  # Reset the x position to restart another line
                    y += word_height * 2 # Start a new row by lowering the y position (on screen, so encreasing the value of it) by the first row (the already written one) and keeping a empty row as space 
                surface.blit(word_surface, (x, y)) #When the line is ended blit the line on the screen
                x += word_width + space #x parameter is set again to his initial value before starting the next loop for the next line
            x = pos[0]  # Reset the x, get another line from the text
            y += word_height  #Start on new row with the new line
   
    def draw(self, screen, text): #method to draw the dialoguebox
        surf_white = pygame.Surface((self.width+20, self.height+20)) #create surface with the same size of the rect
        surf_black = pygame.Surface((self.width, self.height))
        pygame.draw.rect(surf_white, (255, 255, 255), (0, 0, self.width+20, self.height+20)) #draw the out_rect, to get the white edges
        pygame.draw.rect(surf_black, (0, 0, 0), (10, 10, self.width, self.height))  #assign the inner rectangle to a var
        self.blit_text(surf_black, text, (20, 20), self.font) #print the text on the surf
        screen.blit(surf_white,(self.x - 10, self.y - 10))  #print the surf with the text on the screen
        screen.blit(surf_black,(self.x, self.y)) 
       
    def toggle_dialoguebox(self): # method to toggle the value of the show_dialoguebox variable from False (intial value) to True and viceversa
        self.show_dialoguebox = not self.show_dialoguebox #if true chang it to false and viceversa
        self.dialoguebox_sound.play() #display the dialogbox