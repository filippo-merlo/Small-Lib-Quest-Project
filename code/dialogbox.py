import pygame
from text import testi


class MyWindow:
    def __init__(self, text, font_size=10):
        # Create the main window
        self.x = 100
        self.y = 700
        self.width = 1150
        self.height = 75
        self.text = text
        self.font = pygame.font.Font("../graphics/font.ttf", font_size)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.testi = testi()
        self.show_dialog_box = False #init dialogbox at False don't show
        #self.dialog_box = DialogBox(100, 100, 200, 50, self.testo_out)
       
        

    def draw(self, screen):
        # Draw the rectangle
        rect = pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        # Blit the text onto the screen
        screen.blit(self.text_surface, (rect.x + 10, rect.y + 10))
        #rect2 = pygame.draw.rect(screen(255, 255, 255), (self.x, self.y, self.width+10, self.height+10)




    def toggle_dialog_box(self): #sopra inizializzata a False, qui cambia da true a False e viceversa quando chiamata (ossia quando si preme il mouse più giù)
         # Toggle the value of the show_dialog_box variable
        #global show_dialog_box
        self.show_dialog_box = not self.show_dialog_box

    
    def run_window(self, screen):
            #get the output text from the method of the output text
            text = self.testi.dialogues()
        # Join the wrapped lines of text into a single string, separated by newlines
            self.testo_out = text
            self.dialog_box = MyWindow(self.testo_out) 
            self.dialog_box.draw(screen)
            

    
        
# Create an instance of the MyWindow class
#window = MyWindow()

# Call the show_window() method to display the window
#window.run_window(window.dialogues())
