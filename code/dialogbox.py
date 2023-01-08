import pygame
from text import testi
from settings import*


class MyWindow:
    def __init__(self, text, font_size=10, offset = 10):
        # Create the main window
        self.screen_size = pygame.display.get_surface().get_size() #get the screen size
        
        #self.x = 100
        #self.y = 700
        #self.width = 1150
        #self.height = 75

        self.height = 75 #Sets the height to 75 pixels
        self.x = offset # This will position the rectangle "offset" pixels from the left edge of the screen.
        self.y = self.screen_size[1] - self.height - offset # Sets the y attribute to the height of the screen minus the height of the rectangle (75 pixels) minus the offset value.
        self.width = self.screen_size[0] - (offset * 2) # Sets the width attribute to the width of the screen minus twice the offset value. This will reduce the width of the rectangle by "offset" pixels on each side.
        
        self.text = text #instance of the text
        self.font = pygame.font.Font("./graphics/font/font.ttf", font_size) #define font and size
        self.text_surface = self.font.render(self.text, True, (255, 255, 255)) #render the text with the text instance, True is for smoothness, and the color
        self.testi = testi() #instance of the class testi (from text.py)
        self.show_dialog_box = False #init dialogbox at False don't show
    
       
        
    def draw(self, screen): #method to draw the dialog_box
        pygame.draw.rect(screen, (255, 255, 255), (self.x - 10, self.y - 10, self.width + 20, self.height + 20)) #draw the out_rect, to get the white edges
        rect = pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))  #assign the inner rectangle to a var
        screen.blit(self.text_surface, (rect.x + 10, rect.y + 30))  #blit the text onto the screen in the rect position
        
       

    def toggle_dialog_box(self): # method to toggle the value of the show_dialog_box variable from False (intial value) to True and viceversa
        self.show_dialog_box = not self.show_dialog_box

    
    def run_window(self, screen): # method that join an run the dialog box and the text
        text = self.testi.dialogues()  #get the output text from the method of the output text
        self.testo_out = text #crate an instance of text line to show
        self.dialog_box = MyWindow(self.testo_out) #instance of class MyWindow (declaring the variable of text that we need)
        self.dialog_box.draw(screen) #draw the dialogbox
            

    
        
# Create an instance of the MyWindow class
#window = MyWindow()

# Call the show_window() method to display the window
#window.run_window(window.dialogues())
