import pygame



class MyWindow:
    def __init__(self, text, font_size=20, offset = 30):
        # Create the main window
        self.screen_size = pygame.display.get_surface().get_size() #get the screen size

        self.height = 200 #Sets the height in pixels
        self.x = offset # This will position the rectangle "offset" pixels from the left edge of the screen.
        self.y = self.screen_size[1] - self.height - offset # Sets the y attribute to the height of the screen minus the height of the rectangle (75 pixels) minus the offset value.
        self.width = self.screen_size[0] - (offset * 2) # Sets the width attribute to the width of the screen minus twice the offset value. This will reduce the width of the rectangle by "offset" pixels on each side.
        self.text = text #instance of the text
        self.font = pygame.font.Font("./graphics/font/font.ttf", font_size) #define font and size
        self.text_surface = self.font.render(self.text, True, (255, 255, 255)) #render the text with the text instance, True is for smoothness, and the color
        self.show_dialog_box = False #init dialogbox at False don't show
    
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
                    y += word_height * 2 # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

        
    def draw(self, screen): #method to draw the dialog_box
        pygame.draw.rect(screen, (255, 255, 255), (self.x - 10, self.y - 10, self.width + 20, self.height + 20)) #draw the out_rect, to get the white edges
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))  #assign the inner rectangle to a var
        #screen.blit(self.text_surface, (rect.x + 10, rect.y + 30))  #blit the text onto the screen in the rect position
        self.blit_text(screen, self.text, (self.x + 10, self.y + 10), self.font)
        
       
    def toggle_dialog_box(self): # method to toggle the value of the show_dialog_box variable from False (intial value) to True and viceversa
        self.show_dialog_box = not self.show_dialog_box
    
    def run_window(self, screen, text): # method that join an run the dialog box and the text
        self.dialog_box = MyWindow(text) #instance of class MyWindow (declaring the variable of text that we need)
        self.dialog_box.draw(screen) #draw the dialogbox
            
