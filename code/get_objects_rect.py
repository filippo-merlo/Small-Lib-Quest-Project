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
                            prop = obj.properties
                            if "colliders" in prop.keys():
                                o = prop["colliders"]
                                print(dir(o))
                            #name = obj.name
                            #pos = (obj.x*ZOOM, obj.y*ZOOM)
                            #surf = obj.image
                            #surf = pygame.transform.scale(surf,(round(obj.width*ZOOM),round(obj.height*ZOOM)))
                            #if name in ['Librarian','Calsifer','King_squid','King_raccoon','King_skeleton','King_skeleton','King_skeleton','King_skeleton','King_bamboo',"The deadman's letter",'Genius']:
                            #    obj_pos_list.append([name,pos,surf])
    return obj_pos_list

print(get_objects_rect(tmx_data))


        
