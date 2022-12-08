import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

# The Level class will contain every visible object in the game 
class Level:
    def __init__(self):

        # Get the display surface specified in the main
        self.display_surface = pygame.display.get_surface()

        # Sprites are all the objects printed on the screen in videogames 
        # in pygame the sprite class allows to combines a surface(an image) and a rectangle (needed to moove the surfaces on the main one) + other features in the same object
        # Sprite Group, allows to target (es update), a determined category of sprites.
        self.visible_sprites = YSortCameraGroup() 
        self.obstacle_sprites = pygame.sprite.Group()
        # What the sprite.Group() does:
        # it stores different sprites, if i call 
        # 
        #

        # Sprite set up
        self.create_map()


    def create_map(self):
        ### Convert the world map in positions and place each different object
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE # for each vector element compute his position taking into account the standard size in pixel according to TILESIZE
                y = row_index * TILESIZE 
                if col == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites]) # use class Tile
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites) # use class player



    def run(self):
        # draw and update the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group): #this sprite group is going to work as a camera, we are going to sort the sprites by the y coordinate
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()

    
    def custom_draw(self,player): # to add the camera
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width # get the player rectangle position on x and subtract half of the dislay w
        self.offset.y = player.rect.centery - self.half_height # get the player rectangle position on y and subtract half of the dislay h

        #for sprite in self.sprites(): # draw each sprite in the surface...
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset # in his position - the offset given by the position of the player
            self.display_surface.blit(sprite.image,offset_pos)
    # how the camera works:
    # We draw the image in the rect of the sprite, but
    # we can usa a vectror2 to offset the rect and thus blit the image somewere else
    
