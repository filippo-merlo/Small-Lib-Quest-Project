import pygame

from settings import *

### THIS FILE CONTAINS THE CLASS WITH THE METHOD WE ARE USING FOR THE INTRODUCTION SCREEN AND THE ENDGAME SCREEN

class Menu:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface() #get the total surface of the display
        self.width = self.display_surface.get_size()[0] #get the width of the the display's surface
        self.height = self.display_surface.get_size()[1]#get the height of the the display's surface
        self.half_width = self.display_surface.get_size()[0]//2 #get half of the width of the the display's surface
        self.half_height = self.display_surface.get_size()[1]//2 #get half of the height of the the display's surface
        
        # Settings for the start sceen
        self.image_start = pygame.image.load("./graphics/Title/Small Lib Quest(Gold font).png").convert_alpha() #import image for start screen #convert_alpha use only the actual pixel of the png
        self.image_end = pygame.image.load("./graphics/Title/THE_END(Gold font).png").convert_alpha() #import image for end screen
        self.font =  pygame.font.Font("./graphics/font/font.ttf", 20) #define font and size of the start font
        self.end_font = pygame.font.Font("./graphics/font/font.ttf", 30) #define font and size of the end font

    def blit_text(self, surface, text, pos, font, color=pygame.Color('White')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words of the current text to display
        space = font.size(' ')[0]  # The width of a space based on the font used
        max_width, max_height = surface.get_size() #get the width of height of the surface where the text has to be printed
        x, y = pos #get the position in where the text has to be printed
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color) #get the surface covered by the text
                word_width, word_height = word_surface.get_size() #it split the surface covered by the text in two variables
                if x + word_width >= max_width: #if adding another word would exceed the max width of the surface:
                    x = pos[0]  # Reset the x position to restart another line
                    y += word_height*2  # Start a new row by lowering the y position (on screen, so encreasing the value of it) by the first row (the already written one) and keeping a empty row as space 
                surface.blit(word_surface, (x, y)) #When the line is ended blit the line on the screen
                x += word_width + space #x parameter is set again to his initial value before starting the next loop for the next line
            x = pos[0]  # Reset the x, get another line from the text
            y += word_height  #Start on new row with the new line
            
    def start_menu(self):      
        # Create the rectangles surfaces
        surface = pygame.Surface((self.width, self.height)) #create a surface
        text_surf_x = self.width//2
        text_surf_y = self.height//3
        text_surface = pygame.Surface((text_surf_x, text_surf_y))
        Gold_border_1 = pygame.Surface((text_surf_x+20, text_surf_y+20))
        Gold_border_2 = pygame.Surface((text_surf_x+60, text_surf_y+60))
        white_border = pygame.Surface((text_surf_x+40, text_surf_y+40))
        # Fill the rectangles surfaces with the same color
        surface.fill((0, 0, 0)) #white color
        text_surface.fill((0, 0, 0)) #black color
        white_border.fill((255, 255, 255)) #white color
        Gold_border_1.fill((255, 225, 0)) #gold color
        Gold_border_2.fill((255, 225, 0)) #gold color
        # Create the text 
        text1 = "Press <ARROW KEYS> to move your player and the <SPACEBAR> to interact with NPCs.\n\n\nPress <RETURN> to start the game!\n\n\nPress <ESCAPE> to close the game.."
        # Blit the text/image on the center of their corresponding rectangle surfaces
        surface.blit(self.image_start, self.image_start.get_rect(center =(surface.get_rect().centerx, surface.get_rect().centery - 200))) #blit the image on the screen in the middle of the surface
        self.blit_text(text_surface, text1, (20,20), self.font) #uses the function blit_text(surface,text,position,font) to show the text on the screen.
        
        ##Display everything
        self.display_surface.blit(surface, (0,0))
        self.display_surface.blit(Gold_border_2, ((self.half_width-self.width//4)-30, (self.half_height+20)-30))
        self.display_surface.blit(white_border, ((self.half_width-self.width//4)-20, (self.half_height+20)-20))
        self.display_surface.blit(Gold_border_1, ((self.half_width-self.width//4)-10, (self.half_height+20)-10))
        self.display_surface.blit(text_surface, (self.half_width-self.width//4, self.half_height+20))
        

    def end_screen(self):

        pygame.time.wait(2) #then wait 2 seconds and print everything
        surface = pygame.Surface((self.width, self.height))
        text_surf_x = self.width//1.5
        text_surf_y = self.height//2
        text_surface1 = pygame.Surface((text_surf_x, text_surf_y))
        text_surface2 = pygame.Surface((text_surf_x, text_surf_y))

        # Fill the rectangles surfaces with the same color
        surface.fill((0, 0, 0))
        text_surface1.fill((0, 0, 0))
        text_surface2.fill((0, 0, 0))
        # Create the text 
        text1 = "Thank you for playing our game!"
        text2 = "A game designed by: Filippo Merlo & Matteo Melis\n\n\nA special thanks to Clear Code <3\n\n\nPress <ESCAPE> to exit the game."
        # Blit the text/image on the center of their corresponding rectangle surfaces
        surface.blit(self.image_end , self.image_end.get_rect(center =(surface.get_rect().centerx, surface.get_rect().centery - 200)))
        self.blit_text(text_surface1, text1, (20,20), self.end_font)
        self.blit_text(text_surface2, text2, (20,20), self.font)
    
        self.display_surface.blit(surface, (0,0)) #show the image on the screen
        self.display_surface.blit(text_surface1, (self.half_width-(text_surf_x//2), self.half_height+60)) #show the first portion of text
        self.display_surface.blit(text_surface2, (self.half_width-(text_surf_x//2), self.half_height+180))#show the first portion of text
        