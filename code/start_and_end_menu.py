import pygame
from settings import *


class Menu:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface()
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        
        # Settings for the start sceen
        self.image_start = pygame.image.load("./graphics/Title/Small Lib Quest(Gold font).png").convert_alpha()
        self.font =  pygame.font.Font("./graphics/font/font.ttf", 25)
        self.font_the_end = pygame.font.Font("./graphics/font/font.ttf", 80) #define font and size

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
                    y += word_height*2  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
            
    def start_menu(self):      
        # Create the rectangles surfaces
        surface = pygame.Surface((self.width, self.height))
        text_surface = pygame.Surface((self.width//2, self.height//4))
        Gold_border_1 = pygame.Surface(((self.width//2)+20, (self.height//4)+20))
        Gold_border_2 = pygame.Surface(((self.width//2)+60, (self.height//4)+60))
        white_border = pygame.Surface(((self.width//2)+40, (self.height//4)+40))
        # Fill the rectangles surfaces with the same color
        surface.fill((0, 0, 0))
        text_surface.fill((0, 0, 0))
        white_border.fill((255, 255, 255))
        Gold_border_1.fill((255, 223, 0))
        Gold_border_2.fill((255, 223, 0))
        # Create the text 
        text1 = "Press <ARROW KEYS> to move your player and the <SPACEBAR> to interact.\n\n\nPress <RETURN> to start the game!"
        # Blit the text/image on the center of their corresponding rectangle surfaces
        surface.blit(self.image_start, self.image_start.get_rect(center =(surface.get_rect().centerx, surface.get_rect().centery - 200)))
        self.blit_text(text_surface, text1, (20,20), self.font)
        
        self.display_surface.blit(surface, (0,0))
        self.display_surface.blit(Gold_border_2, ((self.half_width-self.width//4)-30, (self.half_height+20)-30))
        self.display_surface.blit(white_border, ((self.half_width-self.width//4)-20, (self.half_height+20)-20))
        self.display_surface.blit(Gold_border_1, ((self.half_width-self.width//4)-10, (self.half_height+20)-10))
        self.display_surface.blit(text_surface, (self.half_width-self.width//4, self.half_height+20))
        

    def end_screen(self):
        #if endgame == True and show_dialog_box == False: #if last interaction True and there is no dialogbox (so you should have close it)
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
