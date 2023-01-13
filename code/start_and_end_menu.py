import pygame
from settings import *
from text import testi

class menu:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]
        self.testi = testi() #instance of testi class from text
        self.text = ''

    def blit_text(self,surface, text, pos, font, color=pygame.Color('White')):
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
                    y += word_height*2  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
            
    def start_menu(self):
            print('')
   
    def end_screen(self):
        if self.testi.endgame == True and self.window.show_dialoguebox == False: #if last interaction True and there is no dialogbox (so you should have close it)
            pygame.time.wait(2000) #then wait 2 seconds and print everything
            pygame.draw.rect(self.display_surface, (255, 255, 255), (0, 0, self.width+20, self.height+20)) #draw the out_rect, to get the white edges
            pygame.draw.rect(self.display_surface, (0, 0, 0), (10, 10, self.width, self.height))  #assign the inner rectangle to a var
           

    def run(self):
        self.start_menu()
        self.end_screen()
        
        



