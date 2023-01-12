import pygame
#from level import Level, YSortCameraGroup
from player import Player
from settings import *
from debug import debug
#from level import Level

class MyWindow:
    def __init__(self, text, font_size=10, offset = 10):
        # Create the main window
        self.screen_size = pygame.display.get_surface().get_size() #get the screen size
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

    
    def run_window(self, screen, who_is_talking): # method that join an run the dialog box and the text
        text = self.testi.dialogues(who_is_talking)  #get the output text from the method of the output text
        self.testo_out = text #crate an instance of text line to show
        self.dialog_box = MyWindow(self.testo_out) #instance of class MyWindow (declaring the variable of text that we need)
        self.dialog_box.draw(screen) #draw the dialogbox

class testi:
    def __init__(self):
        self.name = None

        # check dialogue line
        self.King_raccoon = False
        self.King_squid = False
        self.King_skeleton = False
        self.King_bamboo = False
        self.Librarian = False
        self.Genius = False
        ## ALL THE VARIABLES UP HERE MIGHT BE USELESS##
        # check interaction
        self.King_raccoon_check = False
        self.King_squid_check = False
        self.King_skeleton_check = False
        self.King_bamboo_check = False
        self.Genius_check = False
        self.missions_check = 0
        self.who_is_talking = 6

    def dialogues(self, who_is_talking):  # methods with all the text interaction of the game
        self.name = who_is_talking
       # Librarian Dialogues
        if self.name == 'Librarian':
            if self.Librarian == False:
                return "LIBRARIAN: You!!! You are the hero the king sent! Go talk with the four magic beasts in the corner of the map"
            elif self.King_raccoon_check == True and self.King_squid_check == True and self.King_skeleton_check == True and self.bambu_check == True:  # if you have talked with all the magic beasts
                self.Librarian = True
                self.Genius = True
                return "LIBRARIAN: For all this stuff you should pray to that Genius! But I have a tabloid! ""YOU HAVE GOT TABLOID”"
            # check if you have completed all 4 the mission and interacted with the Genius
            elif self.Librarian == True and self.Genius_check == True and self.missions_check == 4:
                return "LIBRARIAN: Thank you! You have saved the Kingdom!"
        
        # Calsifer Dialogues
        if self.name == 'Calsifer':
            return "Damn this fire is hot!"

        
        # Genius Dialogues
        if self.name == 'Genius':
            return "AHAH this statue is bald!"
        
        


        
        

#
#
## King_raccoon dialoguse
#        # if first interaction with King_raccoon and you are talking with King_raccoon
#
#        if self.King_raccoon == False and self.who_is_talking == 1:
#            self.King_raccoon_check = True  # then check that you have talked with King_raccoon
#            # and print this
#            return "King_raccoon: I'm tired of eating humans! I could use a book for vegan recipe"
#        # if you already talk with King_raccoon and you are talking with King_raccoon and you have interacted with the statute (so you have the book)
#        elif self.King_raccoon == True and self.who_is_talking == 1 and self.Genius_check == True:
#            self.missions_check += 1  # then the mission is complete
#            return "King_raccoon: Thank you! Now i can finally eat those noisy King_bamboo"  # and print this
#
## King_squid dialogues
#        if self.King_squid == False and self.who_is_talking == 2:
#            self.King_squid_check = True
#            return "King_squid: I'm too old to keep destroying these ships. Bring me a tabloid!"
#        elif self.King_squid == True and self.who_is_talking == 2 and self.Genius_check == True:
#            self.missions_check += 1
#            return "King_squid: Thank you! Finally I can read something about the royal family... What?! The Queen died?!?"
#
## King_skeleton dialogues
#        if self.King_skeleton == False and self.who_is_talking == 3:
#            self.King_skeleton_check = True
#            return "King_skeleton: The boss disappeard! He left this letter but i cannod read it! I need a vocabulary."
#        elif self.King_skeleton == True and self.who_is_talking == 3 and self.Genius_check == True:
#            self.missions_check += 1
#            return "King_skeleton: Oh thank you, he just said he needed an holiday"
#
## King_bamboo dialogues
#        if self.King_bamboo == False and self.who_is_talking == 4:
#            self.bambu_check = True
#            return "King_bamboo: My muscle are all sore! I need a book to learn how to strech!"
#        elif self.King_bamboo == True and self.who_is_talking == 4 and self.Genius_check == True:
#            self.missions_check += 1
#            return "King_bamboo: Oh my God, Thank you! I could finally hug my children again!"
#
## Genius dialogues
#        if self.Genius == False and self.who_is_talking == 5:
#            return "That's a nice Genius"
#        elif self.Genius == True and self.who_is_talking == 5:
#            self.Genius_check = True
#            self.King_raccoon = True
#            self.King_squid = True
#            self.King_bamboo = True
#            self.King_skeleton = True
#            return "THE FLOOR SHAKES! 3 books appear on the floor"
#
## Librarian Dialogues
#        if self.Librarian == False:
#            return "LIBRARIAN: You!!! You are the hero the king sent! Go talk with the four magic beasts in the corner of the map"
#        elif self.King_raccoon_check == True and self.King_squid_check == True and self.King_skeleton_check == True and self.bambu_check == True:  # if you have talked with all the magic beasts
#            self.Librarian = True
#            self.Genius = True
#            return "LIBRARIAN: For all this stuff you should pray to that Genius! But I have a tabloid! ""YOU HAVE GOT TABLOID”"
#        # check if you have completed all 4 the mission and interacted with the Genius
#        elif self.Librarian == True and self.Genius_check == True and self.missions_check == 4:
#            return "LIBRARIAN: Thank you! You have saved the Kingdom!"
#
#
#
#