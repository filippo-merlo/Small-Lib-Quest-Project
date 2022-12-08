import pygame
from settings import *

### Tiles are small squares to compose an image

class Tile(pygame.sprite.Sprite): # Inherit Sprite method of sprite class
    def __init__(self, pos, groups):
        super().__init__(groups) # Call the __init__ method of the Inherited sprite.Sprite class that accept groups as argument
        self.image = pygame.image.load("C:/Users/Filippo/Desktop/Small Lib Quest Project/sprites/objects/tree_1.png").convert_alpha() # load image 
        self.image = pygame.transform.scale(self.image, (TILESIZE*0.8, TILESIZE)) # scale image 
        self.rect = self.image.get_rect(topleft = pos) # create the rect to blit on the screen surf. of the same size of the image and pos given by pos. pos is extracted from the WORLD_MAP in the level class
        self.hitbox = self.rect.inflate(0,-10) # hitbox with 5 px less on the two side of the y axis