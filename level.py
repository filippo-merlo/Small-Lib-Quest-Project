import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

# The Level class will contain every visible object in the game 
class Level:
    def __init__(self):

        # Get the display surface from everywere in the code
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup, the sprite object is a base class for visible game objects
        self.visible_sprites = pygame.sprite.Group() # define a group of sprites object
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprite set up
        self.create_map()


    def create_map(self):
        ### Convert the world map in positions
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)



    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)

