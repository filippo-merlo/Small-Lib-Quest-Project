import pygame

from settings import *

### Tiles are small squares to compose an image

class Tile(pygame.sprite.Sprite): # Inherit Sprite method of sprite class
    def __init__(self, pos, surf, groups):
        super().__init__(groups) # Call the __init__ method of the Inherited sprite.Sprite class that accept groups as argument
        self.image = surf # load image 
        self.rect = self.image.get_rect(topleft = pos) # create the rect to blit on the screen surf. of the same size of the image and pos given by pos. pos is extracted from the WORLD_MAP in the level class
        self.hitbox = self.rect.inflate(0,0) # hitbox with 5 px less on the two side of the y axis