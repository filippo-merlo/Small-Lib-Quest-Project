import pygame
from debug import debug

class testi:

    def __init__(self):
       #check dialogue line
        self.Kings_interact = [False, False, False, False] #check if you had the first interaction with all the kings
        self.Librarian1 = False #check if first interaction with librarian has been done
        self.Librarian2 = False #check if second interaction with librarian has been done
        self.Genius = False #check if you've got the books
        self.mission_check = [False, False, False, False] #check if the 4 quest has been solved
        self.endgame = False #last interaction done
        self.statua = True
        
    


    def dialogues(self, name, diag_print, speech):  # methods with all the text interaction of the game
        
        if name: #if there is a name as entry from the colliderect function in Level

            #Librarian Dialogues
            if name == 'Librarian' and not diag_print and not all(self.Kings_interact): #if you have not  talk with the four magic beasts yet
                speech = "LIBRARIAN: You!!! I was waiting for you! You are the hero the Human King sent! The four King of the beasts of this world are mad, you have to help us! Go and look for them at the boundaries of this realm."
                #diag_print= True #says that something has been printed (Then in Level there it takes false, useful to stop the for loop at the first occurences)
                self.Librarian1 = True
                return speech
            elif name == 'Librarian' and not diag_print and all(self.Kings_interact) and not all(self.mission_check): #if you have already talk with the four magic beasts
                speech = "LIBRARIAN: All this stuff?! This library is a mess you'll never find these books, and it's almost lunch break for me, so I cannot help you. We are doomed.. it's the end.. you better pray to that statue on the table!"
                diag_print = True
                self.Librarian2 = True
                return speech
            elif name == 'Librarian' and not diag_print and self.Genius == True and all(self.mission_check): #if you have completed all the mission
                speech = "LIBRARIAN: Can't you see that I'm having my lunch? What?! All the Kings are happy now? Well thank you! We have saved the Kingdom!"
                diag_print = True
                self.endgame = True
                return speech
                
            # Calsifer Dialogues
            if name == 'Calsifer'and not diag_print:
                speech = "CALCIFER: Brrrn*.. Brn.. Brrrrrn*.. 'Damn this fire is hot!'"
                diag_print= True
                return speech

            # Genius Dialogues
            if name == 'Table_up' and not diag_print and self.Librarian2 == False: #table_up is the new genius
                speech = "This statue is kinda ugly! But I feel like it releases a mysterous aura.." 
                diag_print = True
                return speech
            elif name == 'Table_up' and not diag_print and self.Librarian2 == True:
                speech = "THE FLOOR SHAKES! THREE BOOK APPEAR ON THE FLOOR (and a nasty gossip magazine also..)"
                diag_print = True
                self.Genius = True
                return speech
            #elif name == 'Table_up' and not diag_print and self.Librarian2 == True and self.Genius == True:
            #    speech = "GENIUS: Bro i've already gave you the books, just grab them and finish the quests.."
            #    diag_print = True
            #    return speech
                
            #Squid Dialogues
            if name == 'King_squid' and not diag_print and self.Librarian1 == False: #if not interacted with Librarian yet
                speech = "KING SQUID: BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB BLUB"
                diag_print = True
                return speech
            elif name == 'King_squid'and not diag_print and self.Librarian1 == True and self.Genius == False: #if already interacted with Librarian
                speech = "KING SQUID: I'm too old and tired to keep destroying these ships.. But I'm bored, bring me a tabloid!"
                diag_print = True
                if not self.Kings_interact[0]:
                    self.Kings_interact[0] = True
                return speech
            elif name == 'King_squid'and not diag_print and self.Genius == True: #if you've get the books
                speech ="KING SQUID: Thank you! Finally I can read something about the royal family... What?! The Queen died?!? I'm going to destroy even more ships now!"
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
                speech = "KING RACCOON: I'm tired of eating humans! Also, have you heard that meat it's actually bad for the enviroment? I need to be better! I need a book of vegan recipes to save the planet!"
                diag_print = True
                if not self.Kings_interact[1]:
                    self.Kings_interact[1] = True
                return speech
            elif name == 'King_raccoon' and not diag_print and self.Genius == True:
                speech = "KING RACOON: Thank you! Now I can find a tasty way to eat those noisy Bamboos!"
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
                speech = "KING BAMBOO: Look! Me and all my children are having so much fun dancing, but my back hurt so much, I need a book to learn how to strech!"
                diag_print = True
                if not self.Kings_interact[2]:
                    self.Kings_interact[2] = True
                return speech
            elif name == 'King_bamboo' and not diag_print and  self.Genius == True:
                speech = "KING BAMBOO: Oh my Holy Tree, Thank you! I will finally be able to dance with my children again!"
                diag_print = True
                if not self.mission_check[2]:
                    self.mission_check[2] = True
                return speech
        
            #Skeleton Dialogue
            if name == 'King_skeleton' or "The deadman's letter" and not diag_print and  self.Librarian1 == False:
                speech = "NORMAL SKELETON: Sigh* sigh*.. i feel so lonely.."
                diag_print = True
                return speech
            elif name == 'King_skeleton' or "The deadman's letter" and not diag_print and  self.Librarian1 == True and self.Genius == False:
                speech = "NORMAL SKELETON: Hey! I'm not the King! He has disappeard this morning actually.. I'm here alone now.. What should I do..? He left this letter though! But it is written in spanish and I don't understand it.. Also I've not eyes.. Sigh*.. I could use a vocabulary.. I guess.."
                diag_print = True
                if not self.Kings_interact[3]:
                    self.Kings_interact[3] = True
                return speech
            elif name == 'King_skeleton' or "The deadman's letter" and not diag_print and self.Librarian1 == True and self.Librarian2 == True and self.Genius == True:
                speech = "NORMAL SKELETON: Oh thank you, he just said he needed a holiday.. So he flew to Ibiza.. Why didn't he invite me? sigh*.. Nobody wants me.. All my friends are so cold with me.. Maybe because they are all dead?.. Sigh*.."
                diag_print = True
                if not self.mission_check[3]:
                    self.mission_check[3] = True
                return speech

        else:
            None

