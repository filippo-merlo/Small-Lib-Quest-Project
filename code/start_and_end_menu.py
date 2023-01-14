import pygame
from settings import *


class menu:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.font_top_end = pygame.font.Font("./graphics/font/font.ttf", 80) #define font and size
        self.font_bottom_end = pygame.font.Font("./graphics/font/font.ttf", 50)
        self.image_start = pygame.image.load("./graphics/Title/Small Lib Quest(Gold font).png").convert_alpha()
        self.font_bottom_start =  pygame.font.Font("./graphics/font/font.ttf", 30)

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
            
    def start_menu(self, first_screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]: 
            
            # Create the rectangles surfaces
            surface_top = pygame.Surface((self.width, self.half_height))
            surface_bottom = pygame.Surface((self.width, self.half_height))

            # Fill the rectangles surfaces with the same color

            surface_top.fill((0, 0, 0))
            surface_bottom.fill((0, 0, 0))

            # Create the rectangles
            rect_top_rect = surface_top.get_rect()
            rect_bottom_rect = surface_bottom.get_rect(bottom = self.height)

            # Create the text surface
            text_bottom = self.font_bottom_start.render("Press arrow keys to move and spacebar to interact!", True, (255, 255, 255))


            # Blit the text/image on the center of their corresponding rectangle surfaces
            surface_top.blit(self.image_start, self.image_start.get_rect(center = surface_top.get_rect().center))
            surface_bottom.blit(text_bottom,text_bottom.get_rect(center = surface_bottom.get_rect().center))
            

            # Blit the rectangles surfaces on the main screen
            if first_screen:
                self.display_surface.blit(surface_top, rect_top_rect)
                self.display_surface.blit(surface_bottom, rect_bottom_rect)

   
    def end_screen(self):
        #if endgame == True and show_dialog_box == False: #if last interaction True and there is no dialogbox (so you should have close it)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_m]: 
            pygame.time.wait(2) #then wait 2 seconds and print everything
            
            # Create the rectangles surfaces
            surface_top = pygame.Surface((self.width, self.half_height))
            surface_bottom = pygame.Surface((self.width, self.half_height))

            # Fill the rectangles surfaces with the same color

            surface_top.fill((0, 0, 0))
            surface_bottom.fill((0, 0, 0))

            # Create the rectangles
            rect_top_rect = surface_top.get_rect()
            rect_bottom_rect = surface_bottom.get_rect(bottom = self.height)

            # Create the text surfaces
            text_top = self.font_top_end.render("THE END", True, (255, 255, 255))
            text_bottom = self.font_bottom_end.render("Thank you for playing! Press esc to close", True, (255, 255, 255))


            # Blit the text on the center of their corresponding rectangle surfaces
            surface_top.blit(text_top,text_top.get_rect(center = surface_top.get_rect().center))
            surface_bottom.blit(text_bottom,text_bottom.get_rect(center = surface_bottom.get_rect().center))
            

            # Blit the rectangles surfaces on the main screen
            self.display_surface.blit(surface_top, rect_top_rect)
            self.display_surface.blit(surface_bottom, rect_bottom_rect)

        

    def run(self,first_screen):
        self.start_menu(first_screen)
        self.end_screen()

        



