#%%
import pygame
from settings import *
from tile import Tile, Object_Tile
from player import Player
from debug import debug
from pytmx.util_pygame import load_pygame # module of tmxpy that works for pygame

pygame.init() 
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 

tmx_data = load_pygame('C:/Users/Filippo/Desktop/Small Lib Quest Project/data/tmx/map.tmx')

#%%

def get_objects_rect(tmx_data):
    obj_pos_list = []
    for layer in tmx_data.objectgroups:
                 if layer.name in ["Key_objects","NPC","Legendary_creatures"]:
                    for obj in tmx_data.get_layer_by_name(layer.name):
                         if obj.image:
                            name = obj.name
                            pos = (obj.x*ZOOM, obj.y*ZOOM)
                            surf = obj.image
                            surf = pygame.transform.scale(surf,(round(obj.width*ZOOM),round(obj.height*ZOOM)))
                            if name in ['Librarian','Calsifer','King_squid','King_raccoon','King_skeleton','King_skeleton','King_skeleton','King_skeleton','King_bamboo',"The deadman's letter",'Genius']:
                                obj_pos_list.append([name,pos,surf])
    return obj_pos_list

print(get_objects_rect(tmx_data))

def get_objects_pos(obj_pos_list, player):
    self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
    self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h
    correct_obj_pos_list = []
    for name,pos,surf in obj_pos_list:
        offset_pos = pos - self.offset # in his position - the offset given by the position of the player
        if self.offset.x >= self.map.get_width() - self.width:
            offset_pos.x = 0 - (self.map.get_width() - self.width)
        if self.offset.y >= self.map.get_height() - self.height:
            offset_pos.y = 0 - (self.map.get_height() - self.height)
        if self.offset.x <= 0:
            offset_pos.x = 0 
        if self.offset.y <= 0:
            offset_pos.y = 0
        correct_obj_pos_list.append([name,offset_pos,surf])
    return correct_obj_pos_list
        
