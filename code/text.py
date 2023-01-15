#THIS FILE CONTAINS ALL THE TEXT POSSIBILITIES THAT CAN BE SHOWN IN THE GAME

class testi:

    ##In the init we have all the variables that check that the correct line of text is shown
    def __init__(self):
       #check dialogue line
        self.Kings_interact = [False, False, False, False] #check if you had the first interaction with all the kings
        self.Librarian1 = False #check if first interaction with librarian has been done
        self.Librarian2 = False #check if second interaction with librarian has been done
        self.Genius = False #check if you've got the books
        self.mission_check = [False, False, False, False] #check if the 4 quest has been solved
        self.endgame = False #last interaction done
        self.Genius_count = 0 #check for the second interaction in a row with the Genius/statue (after the books are dropped)
        self.Librarian_count = 1 #check for the second interaciton in a row with the Librarian (to get to the endgame)
        
    ## methods with all the text interaction of the game
    def dialogues(self, name, show_dialoguebox):  
        if name: #if there is a name as entry from the check_interactio function in Level (when player rect and npcs rect are colliding and SPACEBAR is pressed)
            
            #Librarian Dialogues
            if name == 'Librarian' and show_dialoguebox and not all(self.Kings_interact): #if you have not talk with the four magic beasts yet
                speech = "LIBRARIAN: You!!! I was waiting for you! You are the hero the Human King sent! The four Beast Kings of this region are mad, you have to help us! The last time they were mad all together something tremendous happened! ..even though it was the reason the librarian position became vacant *Blink*.. But now is BAD! Even WORSE! Go and look for them at the boundaries of this realm!"
                show_dialoguebox = False #says that something has been printed (Then in Level class it takes false, useful to stop the for loop at the first occurency)
                self.Librarian1 = True #check that you have interacted with the Librarian the first time (now the quests can start)
                return speech #return the line of text that has to be shown (in Level, as arugment in the dialogbox.draw functions called from the DialogueBox.py file)
            elif name == 'Librarian' and show_dialoguebox and all(self.Kings_interact) and not all(self.mission_check): #if you have already talk with the four magic beasts
                speech = "LIBRARIAN: All this stuff?! This library is a mess you'll never find these books, and it's almost lunch break for me, so I cannot help you. AH we are doomed.. it's the end.. nothing will save us.. you better go and pray to that statue on the table!"
                show_dialoguebox = False
                self.Librarian2 = True
                return speech
            elif name == 'Librarian' and show_dialoguebox and self.Genius == True and self.Librarian_count == 0 and all(self.mission_check): #if you have completed all the mission
                speech = "LIBRARIAN: Can't you see that I'm having my lunch? What?! All the Kings are happy now? Well thank you! WE have saved the Kingdom! Yuppie! Please if you see the Human King tell him about my essential contribuition to the mission! Ah you should talk with Calcifer before leaving."
                show_dialoguebox = False
                self.Librarian_count += 1 #now you can interact with the librarian again and another text will be shown
                self.Genius_count += 1
                return speech
            elif name == 'Librarian' and show_dialoguebox and self.Librarian_count == 1: #if you have completed all the mission
                speech = "I'm so proud of me today *Blink*. Ah, before leaving you should talk with Calcifer."
                show_dialoguebox = False
                return speech
                
            # Calsifer Dialogues
            if name == 'Calsifer'and show_dialoguebox and self.Librarian_count == 0:
                speech = "CALCIFER: Brrrn*.. Brn.. Brrrrrn*.. 'Damn this fire is hot!'"
                show_dialoguebox= False
                return speech
            elif name == 'Calsifer'and show_dialoguebox and self.Librarian_count == 1:
                speech = "Brrrn*.. Good job MATE, check THIS out! This piece is FIIIREEE!!! You deserve it.  Brrrrrn*.." #does not say anything, but...
                show_dialoguebox= False
                self.endgame = True #...update the endgame variable that will activate the endgame screen in main.py
                return speech

            # Genius Dialogues
            if name == 'Table_up' and show_dialoguebox and self.Librarian2 == False: #table_up is the new genius
                speech = "This statue is kinda ugly! But I feel like it releases a mysterous aura.." 
                show_dialoguebox = False
                return speech
            elif name == 'Table_up' and show_dialoguebox and self.Librarian2 == True and self.Genius_count == 0:
                speech = "You sit in front of the statue.. meanwhile you are sadly thinking about the horrible destiny you will have to face the shiny baldness of the statue capture your gaze.. you touch the statue and!!! THE FLOOR SHAKES!!! THREE BOOK APPEAR ON THE FLOOR (and a nasty gossip magazine also..)"
                show_dialoguebox = False
                self.Genius = True
                self.Genius_count += 1
                return speech
            elif name == 'Table_up' and show_dialoguebox and self.Librarian2 == True and self.Genius_count == 1:
                speech = "GENIUS: Bro I've already gave you the books, just deliver them and finish the quests.. And don't touch my head again.."
                show_dialoguebox = False
                return speech
            elif name == 'Table_up' and show_dialoguebox and self.Librarian2 == True and self.Genius_count == 2:
                speech = "GENIUS: Well done bro.. I like this library after all.. It would have been a shame if those guys had smashed it again.. Ah you should talk with that lil spark over there befoare rolling out of here."
                show_dialoguebox = False
                return speech
            
            #Squid Dialogues
            if name == 'King_squid' and show_dialoguebox and self.Librarian1 == False: #if you have not interacted with Librarian yet
                speech = "KING SQUID: ° ° BLUB BLUB BLUB ° ° BLUB ° ° BLUB BLUB ° ° BLUB BLUB BLUB ° ° BLUB BLUB BLUB ° °"
                show_dialoguebox = False
                return speech
            elif name == 'King_squid' and show_dialoguebox and self.Librarian1 == True and self.Genius == False: #if already interacted with Librarian
                speech = "KING SQUID: I'm too old and tired to keep destroying these ships ° BLUB ° But I'm bored, what other things could I do? ° bored BLUB ° You! Bring me somethig entertaining! Bring me a tabloid! ° BLUB BLUB °"
                show_dialoguebox = False
                if not self.Kings_interact[0]: #if the first position of the list "Kings_interact" is false...
                    self.Kings_interact[0] = True #...set it a true
                return speech
            elif name == 'King_squid' and show_dialoguebox and self.Genius == True: #if you've gotten the books
                speech ="KING SQUID: Thank you! ° BLUB ° Finally I can read something about the royal family... What?! The Queen died?!? I'm going to destroy even more ships now! ° angry BLUB BLUB °"
                show_dialoguebox = False
                if not self.mission_check[0]:
                    self.mission_check[0] = True
                return speech
                
            #Raccoon Dialogues
            if name == 'King_raccoon' and show_dialoguebox and self.Librarian1 == False:
                speech ="KING RACCOON: Grrr.. I'm Hungry! Who's there? I'm going to eat you!"
                show_dialoguebox = False
                return speech
            elif name == 'King_raccoon' and show_dialoguebox and self.Librarian1 == True and self.Genius == False:
                speech = "KING RACCOON: I'm tired of eating humans! Also, have you heard that meat it's actually bad for the enviroment? I need to be better! I need a book of vegan recipes to save the planet!"
                show_dialoguebox = False
                if not self.Kings_interact[1]:
                    self.Kings_interact[1] = True
                return speech
            elif name == 'King_raccoon' and show_dialoguebox and self.Genius == True:
                speech = "KING RACOON: Thank you! Now I can find a tasty way to eat those noisy Bamboos!"
                show_dialoguebox = False
                if not self.mission_check[1]:
                    self.mission_check[1] = True
                return speech

            #Bamboo Dialogue
            if name == 'King_bamboo' and show_dialoguebox and self.Librarian1 == False:
                speech = "KING BAMBOO: Frù.. Frù.. ~chasse~ ohi! Frù.. Frù.. ~twist~ ohi ohi!"
                show_dialoguebox = False
                return speech
            elif name == 'King_bamboo' and show_dialoguebox and self.Librarian1 == True and self.Genius == False:
                speech = "KING BAMBOO: Look! Me and my family are having so much fun dancing ~chasse~ ohi! But my back hurt so much.. I am not flexible as when I was little anymore.. Frù.. it feels like I'm made of wood.. ~twist~ OHI! I need a yoga book to learn how to strech.. Frù!"
                show_dialoguebox = False
                if not self.Kings_interact[2]:
                    self.Kings_interact[2] = True
                return speech
            elif name == 'King_bamboo' and show_dialoguebox and  self.Genius == True:
                speech = "KING BAMBOO: Oh my Holy Tree, Thank you! Frù! I will finally be able to dance with my children again ~pirouette~!"
                show_dialoguebox = False
                if not self.mission_check[2]:
                    self.mission_check[2] = True
                return speech
        
            #Skeleton Dialogue
            if name == 'King_skeleton' or "The deadman's letter" and show_dialoguebox and  self.Librarian1 == False:
                speech = "NORMAL SKELETON: Sigh* sigh*.. I feel so lonely.."
                show_dialoguebox = False
                return speech
            elif name == 'King_skeleton' or "The deadman's letter" and show_dialoguebox and  self.Librarian1 == True and self.Genius == False:
                speech = "NORMAL SKELETON: Hey! I'm not the King! He has disappeard this morning actually.. I'm here alone now.. What should I do..? He left this letter though! But it is written in spanish and I don't understand it.. Also I've not eyes.. Sigh*.. I could use a vocabulary.. I guess.."
                show_dialoguebox = False
                if not self.Kings_interact[3]:
                    self.Kings_interact[3] = True
                return speech
            elif name == 'King_skeleton' or "The deadman's letter" and show_dialoguebox and self.Librarian1 == True and self.Librarian2 == True and self.Genius == True:
                speech = "NORMAL SKELETON: Oh thank you, he just said he needed a holiday.. So he flew to Ibiza.. Why didn't he invite me? sigh*.. Nobody wants me.. All my friends are so cold with me.. Maybe because they are all dead?.. Sigh*.."
                show_dialoguebox = False
                if not self.mission_check[3]:
                    self.mission_check[3] = True
                return speech
        else:
            speech = " "
            return speech