import pygame
from settings import *

class DialogueBox:
    def __init__(self):
        # Create the main window
        self.screen_size = pygame.display.get_surface().get_size() #get the screen size

        self.height = 210 #Sets the height in pixels
        self.x = 30 # This will position the rectangle "offset" pixels from the left edge of the screen.
        self.y = self.screen_size[1] - self.height - self.x # Sets the y attribute to the height of the screen minus the height of the rectangle (75 pixels) minus the offset value.
        self.width = self.screen_size[0] - (self.x * 2) # Sets the width attribute to the width of the screen minus twice the offset value. This will reduce the width of the rectangle by "offset" pixels on each side.
        self.font = pygame.font.Font("./graphics/font/font.ttf", FONT_SIZE) #define font and size
        self.dialoguebox_sound =  pygame.mixer.Sound('./data/sound/dialoguebox_sound.mp3')
        self.show_dialoguebox = False #init dialogbox at False don't show
    
    def blit_text(self, surface, text, pos, font, color=pygame.Color('White')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height * 2 # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
   
    def draw(self, screen, text): #method to draw the dialoguebox
        surf_white = pygame.Surface((self.width+20, self.height+20)) #create surface with the same size of the rect
        surf_black = pygame.Surface((self.width, self.height))
        pygame.draw.rect(surf_white, (255, 255, 255), (0, 0, self.width+20, self.height+20)) #draw the out_rect, to get the white edges
        pygame.draw.rect(surf_black, (0, 0, 0), (10, 10, self.width, self.height))  #assign the inner rectangle to a var
        self.blit_text(surf_black, text, (20, 20), self.font) #print the text on the surf
        screen.blit(surf_white,(self.x - 10, self.y - 10))  #print the surf with the text on the screen
        screen.blit(surf_black,(self.x, self.y)) 
       
    def toggle_dialoguebox(self): # method to toggle the value of the show_dialoguebox variable from False (intial value) to True and viceversa
        self.show_dialoguebox = not self.show_dialoguebox
        self.dialoguebox_sound.play()