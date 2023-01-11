import pygame
#from level import Level, YSortCameraGroup
from player import Player
from settings import *
from debug import debug

#class positions:
#    def __init__(self):
#
#        self.lev = Level() #instance of the level class
#        self.visible_sprites = YSortCameraGroup()  
#        self.obstacle_sprites = pygame.sprite.Group()
#        self.pla = Player((1600,2300),[self.visible_sprites], self.obstacle_sprites)
#        self.map_w = self.lev.map.get_width()
#        self.map_h = self.lev.map.get_height()
#
#        self.who_is_talking = 0
#         #coordinates 
#        self.librarian_coord = []
#        
#
#        #lists of all the surfaces
#        self.librarian_surf = []
#       
#
#        #surface width and height
#        self.librarian_surf_W_H = []
#        
#
#        #final position
#        self.librarian_final_pos = []
#        
#        #position of rect
#        self.lib_xmin = []
#        self.lib_ymin = []
#        self.lib_xmax = []
#        self.lib_ymax = []
#     
#
#    def get_the_pos(self, get_object_offset_pos):
#        
#        #for name in self.lev.get_objects_offset_pos(self.pla):
#        for name in get_object_offset_pos:
#            if name[0] == 'Librarian':
#                self.librarian_coord.append((tuple(name[1]))) #with tuple i get the just X and Y from vector2 class(?)
#                self.librarian_surf.append(name[2]) #append the surface
#                for surface in self.librarian_surf: #for each surface in the list get width and height
#                    self.librarian_surf_W_H.append((surface.get_width(),surface.get_height()))
#                    for c1,c2 in zip(self.librarian_coord, self.librarian_surf_W_H):
#                        self.librarian_final_pos.append((c1[0] + c2[0], c1[1] + c2[1]))# sum of the coord and surf height and width
#                        return (self.librarian_coord, self.librarian_final_pos) #return the initial x,y and the final x,y
#
#    def get_the_coord(self):
#        self.librarian_coord, self.librarian_final_pos = self.get_the_pos() #get the output of "get_the_pos"
#        #coord of librarian rect
#        for xmin,ymin in self.librarian_coord: #append the itial
#            self.lib_xmin.append(xmin* self.map_h / screen_height)
#            self.lib_ymin.append(ymin* self.map_h / screen_height)
#
#        for xmax,ymax in self.librarian_final_pos: #append the final
#            self.lib_xmax.append(xmax* self.map_h / screen_height)
#            self.lib_ymax.append(ymax* self.map_h / screen_height)
#            return self.lib_xmin, self.lib_ymin, self.lib_xmax, self.lib_ymax #return all four
#        
#
#
#    def click(self, mouse_pos):
#        self.lib_xmin, self.lib_ymin, self.lib_xmax, self.lib_ymax = self.get_the_coord() #get the for var
#    
#        self.mouse_x, self.mouse_y = mouse_pos
#        
#        #self.lib_xmin = self.lib_xmin * self.map_h / screen_height
#        
#        for i in zip(self.lib_xmin,self.lib_ymin,self.lib_xmax,self.lib_ymax):
#            xmin, ymin, xmax, ymax = i
#            if  xmin<= self.mouse_x <= xmax and ymin<= self.mouse_y <= ymax:
#                self.who_is_talking = 5
#                print(self.who_is_talking)
#            else:
              #print("Mouse X", self.map_x, "Y", self.map_y)
# 
# 

class interaction:
    def __init__(self):
        self.something = 0
        self.output = False
        
    def touch(self, objects_offset_pos, player_rect):
        for n,p,s in objects_offset_pos:
            area_rect = pygame.Rect(p[0], p[1], s.get_width() +80, s.get_height()+ 80)
            if pygame.Rect.colliderect(player_rect, area_rect):
                self.output = True
            else:
                self.output = False

            
            
               


class testi:
    def __init__(self):
        #self.click.who_is_talking
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



#pygame.init() 
# #Create the display surface, the window where the game will run 
#screen = pygame.display.set_mode((1200,800)) #
#la = positions()
#print(la.get_the_pos())