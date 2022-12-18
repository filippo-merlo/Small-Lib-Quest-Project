import pygame
from settings import *
import debug

### This is the class defining the vary objects to print in the game

class Player(pygame.sprite.Sprite): # Inherit Sprite method of sprite class
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups) # Call the __init__ method of the Inherited class
        self.image = pygame.image.load("C:/Users/Filippo/Desktop/Small Lib Quest Project/graphics/link.png").convert_alpha() # load image 
        self.image = pygame.transform.scale(self.image, (PLAYERSIZE, PLAYERSIZE)) # scale image
        self.rect = self.image.get_rect(topleft = pos) # create the rect to blit on the screen surf. of the same size of the image and pos given by pos. pos is extracted from the WORLD_MAP in the level class
        self.hitbox = self.rect.inflate(0,-26)
        self.direction = pygame.math.Vector2() # will give as a 2d vector to define the player movement
                                               # now x,y = 0, then we want to modify them such as when you pres right x += 1 * player_speed
        self.speed = SPEED # set pix/sec speed of moovement of the player

        self.obstacle_sprites = obstacle_sprites # instantiate the obstacle_sprites =  pygame.sprite.Group() to use it in this class
        
    ### Connect the user input with variations in the direction 2D  vector
    def input(self):
        keys = pygame.key.get_pressed() # get input
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    ### Use the direction vector to update the player rect position
    def move(self,speed):
        if self.direction.magnitude() != 0:# normalize direction
            self.direction = self.direction.normalize() # if the dir vector is diff from 0 it will be normalized
        self.hitbox.x += self.direction.x * speed # modify the self.rect.x position accordingly with the user input 
        self.collision('horizontal') # add the collision in x direction
        self.hitbox.y += self.direction.y * speed # modify the self.rect.x position accordingly with the user input 
        self.collision('vertical') # add the collision in y direction
        self.rect.center = self.hitbox.center
        
    ### Define collisions
    def collision(self,direction):
        if direction == 'horizontal': # if the movement is within the x dimension of the direction vector 
            for sprite in self.obstacle_sprites: # 
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)
