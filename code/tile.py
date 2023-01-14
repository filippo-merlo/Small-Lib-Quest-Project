import pygame

from settings import *

### THIS FILE CONTAINS A CLASS THAT INHERIT A BUILD-IN CLASS OF THE PYGAME PACKAGE THAT ALLOWS YOU TO WORK WITH SPRITES

## Tiles are small squares to compose an image 
## Sprites are graphical objects that can be moved and animated on the screen. 
## The Sprite class provides a basic structure for creating and managing sprites, including properties for position, image, and collision detection

class Tile(pygame.sprite.Sprite): # Inherit Sprite method of sprite class (build-in class in pygame) 
    def __init__(self, pos, surf, groups):
        super().__init__(groups) # Call the __init__ method of the Inherited sprite.Sprite class that accept groups as argument
        self.image = surf # load image (see player file)
        self.rect = self.image.get_rect(topleft = pos) # create the rect to blit on the screen surface of the same size of the image and position given by pos argument. pos is extracted from the "create_map" function in the level class
        self.hitbox = self.rect.inflate(0,0) # hitbox is another rect of the same size of the precedent, that can be modified to get 3D illusion in collision with other tiles
        