class testi:
    def __init__(self):
         #check dialogue line
        self.squirrel = False
        self.kraken = False
        self.skeleton = False
        self.bamboo = False
        self.librarian = False
        self.statue = False
        ## ALL THE VARIABLES UP HERE MIGHT BE USELESS##
        #check interaction
        self.squirrel_check = False
        self.kraken_check = False
        self.skeleton_check = False
        self.bambu_check = False
        self.statue_check = False
        self.missions_check = 0
        self.who_is_talking = 6
    
    def dialogues (self):  #methods with all the text interaction of the game
#Squirrel dialoguse    
        if self.squirrel == False and self.who_is_talking == 1: #if first interaction with squirrel and you are talking with squirrel
            self.squirrel_check = True #then check that you have talked with squirrel
            return "SQUIRREL: I'm tired of eating humans! I could use a book for vegan recipe" #and print this
        elif self.squirrel == True and self.who_is_talking == 1 and self.statue_check == True: #if you already talk with squirrel and you are talking with squirrel and you have interacted with the statute (so you have the book)
            self.missions_check += 1 #then the mission is complete
            return "SQUIRREL: Thank you! Now i can finally eat those noisy bamboo" #and print this
            
#Kraken dialogues
        if self.kraken == False and self.who_is_talking == 2: 
            self.kraken_check = True
            return "KRAKEN: I'm too old to keep destroying these ships. Bring me a tabloid!"
        elif self.kraken == True and self.who_is_talking == 2 and self.statue_check == True:
            self.missions_check += 1
            return "KRAKEN: Thank you! Finally I can read something about the royal family... What?! The Queen died?!?"

#Skeleton dialogues
        if self.skeleton == False and self.who_is_talking == 3: 
            self.skeleton_check = True
            return "SKELETON: The boss disappeard! He left this letter but i cannod read it! I need a vocabulary."
        elif self.skeleton == True and self.who_is_talking == 3 and self.statue_check == True:
            self.missions_check += 1
            return "SKELETON: Oh thank you, he just said he needed an holiday"

#Bamboo dialogues
        if self.bamboo == False and self.who_is_talking == 4: 
            self.bambu_check = True
            return "BAMBOO: My muscle are all sore! I need a book to learn how to strech!"
        elif self.bamboo == True and self.who_is_talking == 4 and self.statue_check == True:
            self.missions_check += 1
            return "BAMBOO: Oh my God, Thank you! I could finally hug my children again!"

#Statue dialogues
        if self.statue == False and self.who_is_talking == 5: 
            return "That's a nice statue"
        elif self.statue == True and self.who_is_talking == 5:
            self.statue_check = True  
            self.squirrel = True
            self.kraken = True
            self.bamboo = True
            self.skeleton = True
            return "THE FLOOR SHAKES! 3 books appear on the floor"

#Librarian Dialogues
        if self.librarian == False and self.who_is_talking == 6:
            return "LIBRARIAN: You!!! You are the hero the king sent! Go talk with the four magic beasts in the corner of the map"
        elif self.squirrel_check == True and self.kraken_check == True and self.skeleton_check == True and self.bambu_check == True and self.who_is_talking == 6: #if you have talked with all the magic beasts
            self.librarian = True
            self.statue = True
            return "LIBRARIAN: For all this stuff you should pray to that statue! But I have a tabloid! ""YOU HAVE GOT TABLOID”"
        elif self.librarian == True and self.statue_check == True and self.missions_check == 4 and self.who_is_talking == 6: # check if you have completed all 4 the mission and interacted with the statue
            return "LIBRARIAN: Thank you! You have saved the Kingdom!"