import pygame

class testi:

    def __init__(self):
       #check dialogue line
        self.King_raccoon = False #check if you've got the quest of the raccoon
        self.King_squid = False #check if you've got the quest of the squid
        self.King_skeleton = False #check if you've got the quest of the skeleton
        self.King_bamboo = False #check if you've got the quest of the bamboo
        self.Librarian1 = False #check if first interaction with librarian has been done
        self.Librarian2 = False #check if second interaction with librarian has been done
        self.Genius = False #check if you've got the books
        self.mission_check = [False, False, False, False] #check if the 4 quest has been solved
        self.endgame = False #last interaction done
    


    def dialogues(self, name, diag_print, speech):  # methods with all the text interaction of the game
        
        if name: #if there is a name as entry from the colliderect function in Level

            #Librarian Dialogues
            if name == 'Librarian' and not diag_print and self.King_raccoon == False and self.King_squid == False and self.King_skeleton == False and self.King_bamboo == False: #if you have not  talk with the four magic beasts yet
                speech = "LIBRARIAN: You!!! You are the hero the king sent! Go talk with the four magic beasts in the corner of the map"
                diag_print= True #says that something has been printed (Then in Level there it takes false, useful to stop the for loop at the first occurences)
                self.Librarian1 = True
                return speech
            elif name == 'Librarian' and not diag_print and self.King_raccoon == True and self.King_squid == True and self.King_skeleton == True and self.King_bamboo == True and not all(self.mission_check): #if you have already talk with the four magic beasts
                speech = "LIBRARIAN: For all this stuff you should pray to that Genius on the table! But the tabloid! ""YOU'VE GOT TABLOID"
                diag_print = True
                self.Librarian2 = True
                return speech
            elif name == 'Librarian' and not diag_print and self.Genius == True and all(self.mission_check): #if you have completed all the mission
                speech = "LIBRARIAN: Thank you! You have saved the Kingdom!"
                diag_print
                self.endgame = True
                return speech
                
            # Calsifer Dialogues
            if name == 'Calsifer'and not diag_print:
                speech = "Damn this fire is hot!"
                diag_print= True
                return speech


            # Genius Dialogues
            if name == 'Genius' and not diag_print and self.Librarian2 == False:
                speech = "It's kinda ugly! But it release a mysterous aurea.."
                diag_print = True
                return speech
            elif name == 'Genius' and not diag_print and self.Librarian2 == True:
                speech = "THE FLOOR SHAKES! THREE BOOK APPEARS ON THE FLOOR"
                diag_print = True
                self.Genius = True
                return speech
            elif name == 'Genius' and not diag_print and self.Genius == True:
                speech = "GENIUS: Bro i've already gave you the books, just grab them and finish the quests.."
                diag_print = True
                return speech


        
            #Squid Dialogues
            if name == 'King_squid' and not diag_print and self.Librarian1 == False: #if not interacted with Librarian yet
                speech = "KING SQUID: BLUB BLUB BLUB"
                diag_print = True
                return speech
            elif name == 'King_squid'and not diag_print and self.Librarian1 == True and self.Genius == False: #if already interacted with Librarian
                speech = "KING SQUID: I'm too old to keep destroying these ships.. But i'm bored, bring me a tabloid!"
                diag_print = True
                self.King_squid = True
                return speech
            elif name == 'King_squid'and not diag_print and self.Genius == True: #if you've get the books
                speech ="KING SQUID: Thank you! Finally I can read something about the royal family... What?! The Queen died?!?"
                diag_print = True
                if not self.mission_check[0]:
                    self.mission_check[0] = True
                return speech
                
            

            
            #Raccoon Dialogues
            if name == 'King_raccoon' and not diag_print and self.Librarian1 == False:
                speech ="KING RACCOON: Grrr.. I'm Hungry! Who's there? I'm going to eat you!"
                diag_print = True
                return speech
            elif name == 'King_raccoon' and not diag_print and self.Librarian1 == True and self.Genius == False:
                speech = "KING RACCOON: I'm tired of eating humans! I could use a book for vegan recipe"
                diag_print = True
                self.King_raccoon = True
                return speech
            elif name == 'King_raccoon' and not diag_print and self.Genius == True:
                speech = "KING RACOON: Thank you! Now I can finally eat those noisy Bamboo!"
                diag_print = True
                if not self.mission_check[1]:
                    self.mission_check[1] = True
                return speech

            
            #Bamboo Dialogue
            if name == 'King_bamboo' and not diag_print and self.Librarian1 == False:
                speech = "KING BAMBOO: Oi.. oi.. Who are you? Stay away from my family!"
                diag_print = True
                return speech
            elif name == 'King_bamboo' and not diag_print and self.Librarian1 == True and self.Genius == False:
                speech = "KING BAMBOO: My muscle are all sore! I need a book to learn how to strech!"
                diag_print = True
                self.King_bamboo = True
                return speech
            elif name == 'King_bamboo' and not diag_print and  self.Genius == True:
                speech = "KING BAMBOO: Oh my Tree, Thank you! I will finally be able to hug my children again!"
                diag_print = True
                if not self.mission_check[2]:
                    self.mission_check[2] = True
                return speech
        


            #Skeleton Dialogue
            if name == 'King_skeleton' or "The deadman's letter" and not diag_print and  self.Librarian1 == False:
                speech = " NORMAL SKELETON: Sigh, sigh,.. i feel so lonely.."
                diag_print = True
                return speech
            elif name == 'King_skeleton' or "The deadman's letter" and not diag_print and  self.Librarian1 == True and self.Genius == False and self.King_skeleton == False:
                speech = "NORMAL SKELETON: My King has disappeard! He left this letter but i cannod read it! I need a vocabulary!"
                diag_print = True
                self.King_skeleton = True
                return speech
            elif name == 'King_skeleton' or "The deadman's letter" and not diag_print and self.Genius == True:
                speech = "NORMAL SKELETON: Oh thank you, he just said he needed a holiday.. Why didn't he invite me? sigh.."
                diag_print = True
                if not self.mission_check[3]:
                    self.mission_check[3] = True
                return speech










#import pygame
#from level import Level, YSortCameraGroup
#from player import Player
#from settings import *
#from debug import debug
#from level import Level
#
#
#class testi:
#    def __init__(self):
#        self.level = Level()
#        self.name = None
#        
#        # check dialogue line
#        self.King_raccoon = False
#        self.King_squid = False
#        self.King_skeleton = False
#        self.King_bamboo = False
#        self.Librarian = False
#        self.Genius = False
#        ## ALL THE VARIABLES UP HERE MIGHT BE USELESS##
#        # check interaction
#        self.King_raccoon_check = False
#        self.King_squid_check = False
#        self.King_skeleton_check = False
#        self.King_bamboo_check = False
#        self.Genius_check = False
#        self.missions_check = 0
#        self.who_is_talking = None
#
#   
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