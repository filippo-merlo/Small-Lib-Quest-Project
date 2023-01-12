import pygame
from settings import *

class menu:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]


    def start_menu(self):
            print('')
   
   

    def run(self):
        self.start_menu()


