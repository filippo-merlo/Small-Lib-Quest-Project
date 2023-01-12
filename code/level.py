import pygame, sys
from settings import *
from tile import Tile, Object_Tile
from player import Player
from debug import debug
from pytmx.util_pygame import load_pygame # module of tmxpy that works for pygame
from dialogbox import MyWindow
from text import testi


# The Level class will contain every visible object in the game 
class Level:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.width = self.display_surface.get_size()[0]
        self.height = self.display_surface.get_size()[1]
        self.offset = pygame.math.Vector2()
        
        # Sprites are all the objects printed on the screen in videogames 
        # in pygame the sprite class allows to combines a surface(an image) and a rectangle (needed to moove the surfaces on the main one) + other features in the same object
        # Sprite Group, allows to target (es update), a determined category of sprites.
        self.visible_sprites = YSortCameraGroup()  
        self.obstacle_sprites = pygame.sprite.Group()
        # What the sprite.Group() does:
        # it stores different sprites, if i call
        self.tmx_data = load_pygame('./data/tmx/map.tmx')
        self.map = pygame.image.load('./data/tmx/map.png').convert_alpha() # load map image 
        self.map = pygame.transform.scale(self.map,(self.map.get_width()*ZOOM,self.map.get_height()*ZOOM))
        # Sprite set up
        self.create_map()
        self.get_objects_pos()
        self.animations_list = self.get_animated_tiles()
        self.animations_list_objects = self.get_animated_objects()
        self.player = Player((1600,2300),[self.visible_sprites], self.obstacle_sprites) # use class player
        self.upper_tiles_list = self.get_upper_tiles()

        ## SET DIALOGUES AND INTERACTIONS
    
        
        self.who_is_talking = None #output of check interaction function
        self.speech = "" #gets in input the current line of text for the dialgue
        self.dialgue_printed = False #keep track if something has to be printed or no
        self.dialogbox = MyWindow(self.speech) #instance of the class Mywindow
        self.testi = testi() #instance of the class testi
        
    

    def create_map(self):
         for layer in self.tmx_data.visible_layers:
             if layer.name in ["Buildings", "Library"] and hasattr(layer,'data'):
                 for x,y,surf in layer.tiles():
                     pos = (x*TILESIZE, y*TILESIZE)
                     surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM)))
                     Tile(pos = pos, surf = surf, groups = [self.visible_sprites])
         for layer in self.tmx_data.objectgroups:
             if layer.name in ["Forrest_trees"]:
                 for obj in self.tmx_data.get_layer_by_name(layer.name):
                     if obj.image:
                         pos = (obj.x*ZOOM, obj.y*ZOOM)
                         surf = pygame.transform.scale(obj.image, (round(obj.width*ZOOM),round(obj.height*ZOOM)))
                         Object_Tile(pos = pos, surf = surf, groups = [self.visible_sprites])
    
         for layer in self.tmx_data.visible_layers:
             if layer.name in ["Vegetation"] and hasattr(layer,'data'):
                 for x,y,surf in layer.tiles():
                     pos = (x*TILESIZE, y*TILESIZE)
                     surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM)))
                     Tile(pos = pos, surf = surf, groups = [self.visible_sprites])
         
         for layer in self.tmx_data.layers:
             if layer.name in ["Invisible_borders"]:
                 for x,y,surf in layer.tiles():
                     pos = (x*TILESIZE, y*TILESIZE)
                     surf = pygame.transform.scale(surf, (round(surf.get_width()*ZOOM),round(surf.get_height()*ZOOM)))
                     Tile(pos = pos, surf = surf, groups = [self.obstacle_sprites])
        
         for layer in self.tmx_data.objectgroups:
             if layer.name in ["Key_objects"]:
                 for obj in self.tmx_data.get_layer_by_name(layer.name):
                     if obj.image:
                         pos = (obj.x*ZOOM, obj.y*ZOOM)
                         surf = obj.image
                         surf = pygame.transform.scale(surf,(round(obj.width*ZOOM),round(obj.height*ZOOM)))
                         Object_Tile(pos = pos, surf = surf, groups = [self.visible_sprites])

    def get_upper_tiles(self):
        upper_tiles_list = []
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
        return upper_tiles_list
    
    def update_upper_tiles(self, upper_tiles_list, player):
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h

        for tile_pos,surf in upper_tiles_list:
            offset_pos = tile_pos - self.offset # in his position - the offset given by the position of the player
            if self.offset.x >= self.map.get_width() - self.width:
                offset_pos.x = tile_pos[0] - (self.map.get_width() - self.width)
            if self.offset.y >= self.map.get_height() - self.height:
                offset_pos.y = tile_pos[1] - (self.map.get_height() - self.height)
            if self.offset.x <= 0:
                offset_pos.x = tile_pos[0] 
            if self.offset.y <= 0:
                offset_pos.y = tile_pos[1]
            self.display_surface.blit(surf, offset_pos)

    def create_map_from_img(self, player):
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
        offset_pos = (0,0) - self.offset # in his position - the offset given by the position of the player
        
        if self.offset.x >= self.map.get_width() - self.width:
            offset_pos.x = 0 - (self.map.get_width() - self.width)
        if self.offset.y >= self.map.get_height() - self.height:
            offset_pos.y = 0 - (self.map.get_height() - self.height)
        if self.offset.x <= 0:
            offset_pos.x = 0 
        if self.offset.y <= 0:
            offset_pos.y = 0
        self.display_surface.blit(self.map,offset_pos)

    def get_animated_tiles(self): 
        animations_list = []   
        for layer in self.tmx_data.visible_layers:
            if layer.name in ['Vegetation', 'Library'] and hasattr(layer,'data'):
                for x,y,image in layer.tiles():                
                    for gid, props in self.tmx_data.tile_properties.items():
                        if props['frames'] != [] and image == self.tmx_data.get_tile_image_by_gid(props['frames'][0].gid):
                            animated_img_dict = {
                                'id' : props['id'],
                                'gid': gid,
                                'frames': props['frames'],
                                'pos' : (x*TILESIZE,y*TILESIZE),                              
                                'duration': props['frames'][0].duration,
                                'current_frame': 0,
                                'last_update': 0
                            }
                            animations_list.append(animated_img_dict)
                
        return animations_list

    def get_animated_objects(self):
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

    def update_animated_tiles(self, animations_list, player):
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
        
        for animation in animations_list:

            # Get the current time
            current_time = pygame.time.get_ticks()
            # Check if it's time to update the frame
            if current_time - animation['last_update'] > animation['duration']:
                # Increment the frame index
                animation['current_frame'] = (animation['current_frame'] + 1) % len(animation['frames'])
                # Set the last update time to the current time
                if animation['current_frame'] > len(animation['frames']):
                    animation['current_frame'] = 0
                animation['last_update'] = current_time

            for animation in animations_list:  
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
                tile_image = pygame.transform.scale(tile_image,(tile_image.get_width()*ZOOM,tile_image.get_height()*ZOOM))
                # Blit the image to the screen
                self.display_surface.blit(tile_image, offset_pos)

    def update_animated_objects(self, animations_list_objects, player):
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
    
        # Update the animation for each tile
        for animation in animations_list_objects:

            # Get the current time
            current_time = pygame.time.get_ticks()
            # Check if it's time to update the frame
            if current_time - animation['last_update'] > animation['duration']:
                # Increment the frame index
                animation['current_frame'] = (animation['current_frame'] + 1) % len(animation['frames'])
                # Set the last update time to the current time
                if animation['current_frame'] > len(animation['frames']):
                    animation['current_frame'] = 0
                animation['last_update'] = current_time

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
                tile_image = pygame.transform.scale(tile_image, (round(animation['width']*ZOOM),round(animation['height']*ZOOM)))
                # Blit the image to the screen
                self.display_surface.blit(tile_image, offset_pos)

### Functions to get object of interest offsetted position
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
                                if name in ['Librarian','Calsifer','King_squid','King_raccoon','King_skeleton','King_bamboo',]:
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
        dialogue_icon = pygame.image.load('./sprites/icons/dialogue_icon.png').convert_alpha()
        dialogue_icon = pygame.transform.scale(dialogue_icon, (TILESIZE,TILESIZE))
        for name,pos,surf in objects_offset_pos: #check in which rect the player is in by the collision betw
                            width = surf.get_width()+20
                            height = surf.get_height()+80
                            position = (pos[0]-surf.get_width()/5, pos[1]-surf.get_height()/5)
                            area_rect = pygame.Rect(position, (width, height))
                            pygame.draw.rect(self.display_surface, (0,0,0), area_rect)
                            if pygame.Rect.colliderect(player_area, area_rect):
                                self.display_surface.blit(dialogue_icon,(player_area.centerx, player_area.centery-dialogue_icon.get_height()))
        for event in pygame.event.get():     
            #sia qui che main, temporaneo? bho vedremo amici
            if event.type == pygame.QUIT: # the QUIT event is clicking on the red cross at the top right of the window
                pygame.quit() # quit pygame
                sys.exit() # quit the while loop  
            #check event click
            if event.type == pygame.KEYDOWN: #if you click a key
                if event.key == pygame.K_SPACE:  #and the key is spacebar
                        for name,pos,surf in objects_offset_pos: #check in which rect the player is in by the collision betw
                            width = surf.get_width()+20
                            height = surf.get_height()+80
                            position = (pos[0]-surf.get_width()/5, pos[1]-surf.get_height()/5)
                            area_rect = pygame.Rect(position, (width, height))
                            if pygame.Rect.colliderect(player_area, area_rect):
                                self.dialogbox.toggle_dialog_box() #change from False to True or viceversa
                                self.dialgue_printed = False #says that something has not been printed yet
                                self.who_is_talking = name             
                                           
    def run(self):
        # draw and update the game
        self.create_map_from_img(self.player)
        self.visible_sprites.custom_draw(self.player)
        self.update_upper_tiles(self.upper_tiles_list,self.player)
        self.update_animated_tiles(self.animations_list, self.player)
        self.update_animated_objects(self.animations_list_objects, self.player)
        self.visible_sprites.update()

        self.check_interaction() #run the events interaction function
        self.testi.dialogues(self.who_is_talking, self.dialgue_printed, self.speech)
        if self.dialogbox.show_dialog_box: #if the text box has to be shown (is True)
            self.dialogbox.run_window(self.display_surface, self.testi.dialogues(self.who_is_talking, self.dialgue_printed, self.speech)) #then shown it #then shown it
            self.dialogbox.run_window(self.display_surface, self.testi.dialogues(self.who_is_talking, self.dialgue_printed, self.speech)) #then shown it #then shown it
        

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




