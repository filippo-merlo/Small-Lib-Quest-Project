import pygame, sys
from pytmx.util_pygame import load_pygame # module of tmxpy that works for pygame, we need this to handle the tmx file where the map is contained. The map was created using Tiled, an application for designing games levels
from pathlib import Path

from settings import *
from tile import Tile
from player import Player
from  DialogueBox import *
from text import testi

### THIS FILE HAS EVERYTHING!!!!!!

### The Level class will contain every visible object in the game 
class Level:
    def __init__(self):

        ## Get the display surface specified in the main and get his sizes 
        self.display_surface = pygame.display.get_surface() 
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]
        ## Create an offset vector that will be used to get the offset position of the objects in the map. They will be moving accordingly with the players input. This will print the player on the center of the screen and make the camera moving around following him
        self.offset = pygame.math.Vector2() #will give as a 2d vector to define the player movement
        
        ## Sprites are all the objects printed on the screen in videogames 
        # in pygame the sprite class allows to combines a surface(an image) and a rectangle (needed to moove the surfaces on the main one) + other features in the same object
        # Sprite Group, allows to target (es update), a determined category of sprites.
        self.visible_sprites = YSortCameraGroup()  # Custom Group that is needed to draw each element accordingly with the position of the player. It will generate the illusion of the player mooving in the map (with a camera following him from the top), when actually it will happen the opposite, the map is mooving accordingly of the changes of the player's rect coordinates
        self.obstacle_sprites = pygame.sprite.Group() # Build-in class in Pygame that allow to manage multiple sprite at once, we need it to create a separate group of sprites that will be use for making the non-overlapable walls of the map

        ## Load and scale the map BACKGROUND immage accordingly with the ZOOM level we decided
        self.tmx_data = load_pygame(Path('./data/tmx/map.tmx')) # load tmx file with the coordinates and paths to all the images of the games objects
        self.map = pygame.image.load(Path('./data/tmx/map.png')).convert_alpha() # load map image 
        self.map = pygame.transform.scale(self.map,(self.map.get_width()*ZOOM,self.map.get_height()*ZOOM)) # scale the map accordingly with the zoom level
       
        ## Sprite set up
        self.create_map() # function that extract all the map tiles immages from the tmx file
        self.get_objects_pos() # function that get the position in the map of some objects
        self.animations_list = self.get_animated_tiles() 
        self.animations_list_objects = self.get_animated_objects()
        self.player = Player((1600,2300),[self.visible_sprites], self.obstacle_sprites) # use class player
        self.upper_tiles_list = self.get_upper_tiles()

        ## SET DIALOGUES AND INTERACTIONS
        self.who_is_talking = None #output of check interaction function
        self.speach = ""  #gets in input the current line of text for the dialogue
        self.dialogue_block = True # Control that only one dialogue is extracted.
        self.dialoguebox = DialogueBox() #instance of the class Mywindow
        self.testi = testi() #instance of the class testi        
        
    ### CREATE MAP FROM THE .tmx FILE
    def create_map(self):
         for layer in self.tmx_data.visible_layers: # from visible layers in the .tmx map file (all the tiles are disposed in different layers to control the overlappings)
             if layer.name in ["Buildings", "Library"] and hasattr(layer,'data'): # select the layers named buildings and library, nad chech if they are empty 
                 for x,y,surf in layer.tiles(): # from each layer extract position and image of each single tile 
                     pos = (x*TILESIZE, y*TILESIZE) # define position
                     surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM))) # scale image
                     Tile(pos = pos, surf = surf, groups = [self.visible_sprites]) # create tile assigning it to the self.visible_sprites
         for layer in self.tmx_data.objectgroups: # same for objects (they are more or less the same but they are genrated differently in Tiled, the application we used to create the level)
             if layer.name in ["Forrest_trees"]:
                 for obj in self.tmx_data.get_layer_by_name(layer.name):
                     if obj.image:
                         pos = (obj.x*ZOOM, obj.y*ZOOM)
                         surf = pygame.transform.scale(obj.image, (round(obj.width*ZOOM),round(obj.height*ZOOM)))
                         Tile(pos = pos, surf = surf, groups = [self.visible_sprites])
         for layer in self.tmx_data.visible_layers: # same here
             if layer.name in ["Vegetation"] and hasattr(layer,'data'):
                 for x,y,surf in layer.tiles():
                     pos = (x*TILESIZE, y*TILESIZE)
                     surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM)))
                     Tile(pos = pos, surf = surf, groups = [self.visible_sprites])
         for layer in self.tmx_data.layers: # same here
             if layer.name in ["Invisible_borders"]:
                 for x,y,surf in layer.tiles():
                     pos = (x*TILESIZE, y*TILESIZE)
                     surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM)))
                     Tile(pos = pos, surf = surf, groups = [self.obstacle_sprites]) # this tiles are assigned to the obstacle_sprites group because they wont be printed, they will define the borders and non overlapping areas of the map
         for layer in self.tmx_data.objectgroups: # same as previous
             if layer.name in ["Key_objects"]:
                 for obj in self.tmx_data.get_layer_by_name(layer.name):
                     if obj.image:
                         pos = (obj.x*ZOOM, obj.y*ZOOM)
                         surf = obj.image
                         surf = pygame.transform.scale(surf,(round(obj.width*ZOOM),round(obj.height*ZOOM)))
                         Tile(pos = pos, surf = surf, groups = [self.visible_sprites])

    def get_upper_tiles(self):
        upper_tiles_list = [] # same system of before but for tiles that needs to be printed over the player, so they are handled differently
        for layer in self.tmx_data.visible_layers:
            if layer.name in ["Upper_parts","Lower_upper_parts"] and hasattr(layer,'data'):
                for x,y,surf in layer.tiles():
                    tile_pos = (x*TILESIZE, y*TILESIZE)
                    surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM)))
                    upper_tiles_list.append([tile_pos,surf])
        for layer in self.tmx_data.objectgroups:
             if layer.name in ["Key_objects","Objects_no_interactions"]:
                 for obj in self.tmx_data.get_layer_by_name(layer.name):
                     if obj.image and obj.name in ['Genius','Table_up']:
                         tile_pos = (obj.x*ZOOM, obj.y*ZOOM)
                         surf = obj.image
                         surf = pygame.transform.scale(surf,(round(obj.width*ZOOM),round(obj.height*ZOOM)))
                         upper_tiles_list.append([tile_pos,surf])
        return upper_tiles_list # list of upper tiles
    
    def update_upper_tiles(self, upper_tiles_list, player): # since upper tiles are not in a sprite group we have to compute theyr onset differently than the self.visible_sprites that are an istance of the YSortCameraGroup() class
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h

        ## For every img in upper_tiles_list compute the offset accordingly with the player position
        for tile_pos,surf in upper_tiles_list:
            offset_pos = tile_pos - self.offset # his position - the offset given by the position of the player
            # to dont make the "camera" (motion of the map) follow the player even after the map boundaries, when the player offset crosses the distance of half the screen thoward the map boundaries the pffset becomes the size of the map - half of the gamescreen..
            if self.offset.x >= self.map.get_width() - self.width:
                offset_pos.x = tile_pos[0] - (self.map.get_width() - self.width)
            if self.offset.y >= self.map.get_height() - self.height:
                offset_pos.y = tile_pos[1] - (self.map.get_height() - self.height)
            if self.offset.x <= 0: # or in his original position
                offset_pos.x = tile_pos[0] 
            if self.offset.y <= 0:
                offset_pos.y = tile_pos[1]
            self.display_surface.blit(surf, offset_pos) # blit/draw the updated tiles on the main surface

    def create_map_from_img(self, player): # same as upper tiles but for teh map image, it's starting position in (0,0)
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
        offset_pos = (0,0) - self.offset # his position - the offset given by the position of the player
        # to dont make the "camera" (motion of the map) follow the player even after the map boundaries, when the player offset crosses the distance of half the screen thoward the map boundaries the offset becomes the size of the map - half of the gamescreen..
        if self.offset.x >= self.map.get_width() - self.width:
            offset_pos.x = 0 - (self.map.get_width() - self.width)
        if self.offset.y >= self.map.get_height() - self.height:
            offset_pos.y = 0 - (self.map.get_height() - self.height)
        if self.offset.x <= 0: # or the upper left corner of the map 
            offset_pos.x = 0 
        if self.offset.y <= 0:
            offset_pos.y = 0
        self.display_surface.blit(self.map,offset_pos) # blit/draw the map on the main surface

    ## HANDLE ANIMATED TILES
    def get_animated_tiles(self): 
        animations_list = []   
        for layer in self.tmx_data.visible_layers:
            if layer.name in ['Vegetation', 'Library'] and hasattr(layer,'data'):
                for x,y,image in layer.tiles(): # get tiles position and image from the layers
                    for gid, props in self.tmx_data.tile_properties.items(): # get the props dictionary from self.tmx_data.tile_properties.items()
                        if props['frames'] != [] and image == self.tmx_data.get_tile_image_by_gid(props['frames'][0].gid): # if the image from the layer has an animation: only images that have a 'frames' list in props dict have animations
                            animated_img_dict = { # fill animated_img_dict with all the info of the animated images
                                'id' : props['id'],
                                'gid': gid,
                                'frames': props['frames'], # image frames
                                'pos' : (x*TILESIZE,y*TILESIZE),                          
                                'duration': props['frames'][0].duration, # duration of each frame
                                'current_frame': 0, # set a current frame index
                                'last_update': 0 # set a last update index
                            }
                            animations_list.append(animated_img_dict) # append the dict object to the animations_list (a list of dictionaries of animated images)
                
        return animations_list

    def get_animated_objects(self): # same process but for objects instead of tiles
        animations_list = []   
        for layer in self.tmx_data.objectgroups:
            for obj in layer:
                if obj.image:
                    pos = (obj.x*ZOOM, obj.y*ZOOM)
                    width = obj.width
                    height = obj.height
                    image = obj.image               
                    for gid, props in self.tmx_data.tile_properties.items():
                        if props['frames'] != [] and image == self.tmx_data.get_tile_image_by_gid(props['frames'][0].gid):
                            animated_img_dict = {
                                'id' : props['id'],
                                'gid': gid,
                                'frames': props['frames'],
                                'pos' : pos, 
                                'width' : width,
                                'height' : height,
                                'duration': props['frames'][0].duration,
                                'current_frame': 0,
                                'last_update': 0
                            }
                            animations_list.append(animated_img_dict)

        return animations_list

    def update_animated_tiles(self, animations_list, player): # it gets as input the list of dicts for animated images
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
        
        for animation in animations_list: # iterate over the list of dicts containing the info for animated tiles

            # Get the current time (in frames)
            current_time = pygame.time.get_ticks() 
            # Check if it's time to update the frame
            if current_time - animation['last_update'] > animation['duration']: # if the point in the animation sequence (total time - last update) is bigger than the single animation duration
                # Increment the frame index
                animation['current_frame'] = (animation['current_frame'] + 1) % len(animation['frames']) # if a < b, a % b = a, if a > b, a % b = rest, so 1 % 7 = 1, 7 % 7 = 0 and 8 % 7 = 1
                animation['last_update'] = current_time # keep track of the time in every images

            # Compute the position of the tiles relatively to the player's position
            for animation in animations_list:  
                # Get the current frame for the tile
                current_frame = animation['frames'][animation['current_frame']] # Get the current image frame 
                # Calculate the position of the tile
                tile_pos = animation['pos']
                offset_pos = tile_pos - self.offset # in his position - the offset given by the position of the player
                if self.offset.x >= self.map.get_width() - self.width:
                    offset_pos.x = tile_pos[0] - (self.map.get_width() - self.width)
                if self.offset.y >= self.map.get_height() - self.height:
                    offset_pos.y = tile_pos[1] - (self.map.get_height() - self.height)
                if self.offset.x <= 0:
                    offset_pos.x = tile_pos[0] 
                if self.offset.y <= 0:
                    offset_pos.y = tile_pos[1]
                # Get the image for the current frame
                tile_image = self.tmx_data.get_tile_image_by_gid(current_frame.gid) # Get the image of the current frame 
                tile_image = pygame.transform.scale(tile_image,(tile_image.get_width()*ZOOM,tile_image.get_height()*ZOOM)) # scale image
                # Blit the image on the game surface
                self.display_surface.blit(tile_image, offset_pos)

    # same as before but for objects
    def update_animated_objects(self, animations_list_objects, player):
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
    
        # Update the animation for each object
        for animation in animations_list_objects:

            # Get the current time
            current_time = pygame.time.get_ticks()
            # Check if it's time to update the frame
            if current_time - animation['last_update'] > animation['duration']:
                # Increment the frame index
                animation['current_frame'] = (animation['current_frame'] + 1) % len(animation['frames']) # if a < b, a % b = a, if a > b, a % b = rest, so 1 % 7 = 1, 7 % 7 = 0 and 8 % 7 = 1
                animation['last_update'] = current_time # keep track of the time in every images

            for animation in animations_list_objects:  
                # Get the current frame for the tile
                current_frame = animation['frames'][animation['current_frame']]
                # Calculate the position of the tile
                tile_pos = animation['pos']
                offset_pos = tile_pos - self.offset # in his position - the offset given by the position of the player
                if self.offset.x >= self.map.get_width() - self.width:
                    offset_pos.x = tile_pos[0] - (self.map.get_width() - self.width)
                if self.offset.y >= self.map.get_height() - self.height:
                    offset_pos.y = tile_pos[1] - (self.map.get_height() - self.height)
                if self.offset.x <= 0:
                    offset_pos.x = tile_pos[0] 
                if self.offset.y <= 0:
                    offset_pos.y = tile_pos[1]
                # Get the image for the current frame
                tile_image = self.tmx_data.get_tile_image_by_gid(current_frame.gid)
                tile_image = pygame.transform.scale(tile_image, (round(animation['width']*ZOOM),round(animation['height']*ZOOM))) # Scale the immage
                # Blit the image to the screen
                self.display_surface.blit(tile_image, offset_pos)

### Functions to get only object of interest (to use in dialogues) offsetted position
    def get_objects_pos(self):
        self.obj_pos_list = []
        for layer in self.tmx_data.objectgroups:
                    if layer.name in ["Key_objects","NPC","Legendary_creatures","Objects_no_interactions"]:
                        for obj in self.tmx_data.get_layer_by_name(layer.name):
                            if obj.image:
                                name = obj.name
                                pos = (obj.x*ZOOM, obj.y*ZOOM)
                                surf = obj.image
                                surf = pygame.transform.scale(surf,(round(obj.width*ZOOM),round(obj.height*ZOOM)))
                                if name in ['Librarian','Calsifer','King_squid','King_raccoon','King_skeleton','King_bamboo',"The deadman's letter"]:
                                    self.obj_pos_list.append([name,pos,surf])
                                if name in ['Table_up']:
                                    self.obj_pos_list.append([name,pos,pygame.transform.scale(surf,(surf.get_width()*2.5,surf.get_height()))])
          
    def get_objects_offset_pos(self,player):
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
        self.correct_obj_pos_list = []
        for name,pos,surf in self.obj_pos_list:
            offset_pos = pos - self.offset # in his position - the offset given by the position of the player
            if self.offset.x >= self.map.get_width() - self.width:
                offset_pos.x = pos[0] - (self.map.get_width() - self.width)
            if self.offset.y >= self.map.get_height() - self.height:
                offset_pos.y = pos[1] - (self.map.get_height() - self.height)
            if self.offset.x <= 0:
                offset_pos.x = pos[0] 
            if self.offset.y <= 0:
                offset_pos.y = pos[1]
            self.correct_obj_pos_list.append([name,offset_pos,surf])
        return self.correct_obj_pos_list ## so it gives in output the list, and we can use it in text.position.get_the_pos

### Functions to get the dialogues
    def player_coord(self):
        
        ### PLAYER COORDINATES FOR INTERACTION (so it's in the center of the screen)
        self.offset.x = self.player.rect.x+PLAYERSIZE_W - self.half_width # get the player rectangle center position on x and subtract half of the dislay w
        self.offset.y = self.player.rect.y+PLAYERSIZE_H - self.half_height # get the player rectangle center position on y and subtract half of the display h
    
        offset_pos = self.player.rect.center - self.offset # in his position - the offset given by the position of the player
        if self.offset.x >= self.map.get_width() - self.width:
            offset_pos.x = self.player.rect.x - (self.map.get_width() - self.width)
        if self.offset.y >= self.map.get_height() - self.height:
            offset_pos.y = self.player.rect.y - (self.map.get_height() - self.height)
        if self.offset.x <= 0:
            offset_pos.x = self.player.rect.x 
        if self.offset.y <= 0:
            offset_pos.y = self.player.rect.y
       
        our_personal_player_rect = pygame.Rect(offset_pos,(PLAYERSIZE_W,PLAYERSIZE_H))
       
        return our_personal_player_rect

    def check_interaction(self):
        objects_offset_pos= self.get_objects_offset_pos(self.player) #function to get the pos of the npc scaled on the player
        player_area = self.player_coord() #function to get the player coord based on the center of its rect
        dialogue_icon = pygame.image.load(Path('./sprites/icons/dialogue_icon.png')).convert_alpha()
        dialogue_icon = pygame.transform.scale(dialogue_icon, (TILESIZE,TILESIZE))
        for name,pos,surf in objects_offset_pos: #check in which rect the player is in by the collision betw
                            width = surf.get_width()+20
                            height = surf.get_height()+80
                            position = (pos[0]-surf.get_width()/5, pos[1]-surf.get_height()/5)
                            area_rect = pygame.Rect(position, (width, height))
                            if pygame.Rect.colliderect(player_area, area_rect):
                                self.display_surface.blit(dialogue_icon,(player_area.centerx, player_area.centery-dialogue_icon.get_height()))
        #check event click
        for event in pygame.event.get(): # Get the vector with all the events (input from the user) 
            if event.type == pygame.KEYDOWN: #if a key is pressed..
                if event.key == pygame.K_ESCAPE: #.. and the key is [ESCAPE]
                    pygame.quit() # quit pygame
                    sys.exit() # quit the while loop
                if event.key == pygame.K_SPACE: #.. and the key is [SPACEBAR]
                    for name,pos,surf in objects_offset_pos: #check in which rect the player is colliding with
                        width = surf.get_width()+20 #rescale the width to encrease the interaction area 
                        height = surf.get_height()+80 #rescale the height to encrease the interaction area
                        position = (pos[0]-surf.get_width()/5, pos[1]-surf.get_height()/5) #???
                        area_rect = pygame.Rect(position, (width, height)) #assign to a var the rect of the npc
                        if pygame.Rect.colliderect(player_area, area_rect): #if player is colliding with the rect (and the SPACEBAR IS PRESSED)
                            self.dialoguebox.toggle_dialoguebox() #change from False to True or viceversa the attribute show_dialoguebox (basically if the dialogue box has to be shown or not)
                            self.who_is_talking = name #get the name of the npc the player is interacting with
                            self.dialogue_block = False #to control the text output, is false so, nothing has been printed yet so you can print something. 
                                                        #This is also checked in every dialogue interaction in "text.py" and in the same file, it change its state in True

### Run method called in main loop, in which all the other methods that we are using to run the game are in                                               
    def run(self):
        ## Draw and update the game
        self.create_map_from_img(self.player)
        self.visible_sprites.custom_draw(self.player)
        self.update_upper_tiles(self.upper_tiles_list,self.player)
        self.update_animated_tiles(self.animations_list, self.player)
        self.update_animated_objects(self.animations_list_objects, self.player)
        self.visible_sprites.update()
        
        ## Make dialogues work
        self.check_interaction() #run the events interaction function
        if self.dialoguebox.show_dialoguebox: #if the text box has to be shown (if is True)
            if not self.dialogue_block: # Control that only one dialogue is extracted. Otherwise it will run all the if skipping subsequent conditions for es  it would skip "if Genius == 0: Genius += 1" going instantly to  "if Genius == 1"
                self.speech = self.testi.dialogues(self.who_is_talking, self.dialoguebox.show_dialoguebox) #the text line is get from the "dialogues" function in "text.py". It gets as arguments the name of which npc the player is interacting with and if the dialogue box has to be shown (True/False)
                self.dialogue_block = True #reset the block to true, so it gets only one interaction each time
            self.dialoguebox.draw(self.display_surface, self.speech) #then show the dialogbox in the given position of the screen and with the right text, got from the "dialogues" function in "text.py"
            self.player.block = True #block the player movements (while the dialogue is shown)
            self.player.direction.x = 0
            self.player.direction.y = 0

        if not self.dialoguebox.show_dialoguebox: #if the dialogue box is not shown
            self.player.block = False #deactivate player block, so you can move it again
        
class YSortCameraGroup(pygame.sprite.Group): #this sprite group is going to work as a camera, we are going to sort the sprites by the y coordinate
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]
        self.offset = pygame.math.Vector2()
        self.map = pygame.image.load("./data/tmx/map.png").convert_alpha() # load map image 
        self.map = pygame.transform.scale(self.map,(self.map.get_width()*ZOOM,self.map.get_height()*ZOOM))


    def custom_draw(self,player): # to add the camera
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
    
        #for sprite in self.sprites(): # draw each sprite in the surface...
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset # in his position - the offset given by the position of the player
            if self.offset.x >= self.map.get_width() - self.width:
                offset_pos.x = sprite.rect.x - (self.map.get_width() - self.width)
            if self.offset.y >= self.map.get_height() - self.height:
                offset_pos.y = sprite.rect.y - (self.map.get_height() - self.height)
            if self.offset.x <= 0:
                offset_pos.x = sprite.rect.x 
            if self.offset.y <= 0:
                offset_pos.y = sprite.rect.y
                
            self.display_surface.blit(sprite.image,offset_pos)
            
    # how the camera works:
    # We draw the image in the rect of the sprite, but
    # we can usa a vectror2 to offset the rect and thus blit the image somewere else