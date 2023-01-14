import pygame

from settings import *

### THIS FILE HAS IN IT A CLASS WITH ALL THE METHODS THAT REGARD 

class Player(pygame.sprite.Sprite): # Inherit Sprite method of sprite class (build-in class in pygame to manage spirtes)
    #initialize all the variable useful for the methods below
    def __init__(self,pos,groups,obstacle_sprites): #as arguments we have the same of the Tile class in tile.py file
        super().__init__(groups) # Call the __init__ method of the Inherited class
        self.image = pygame.image.load("./sprites/characters/player_still_1.png").convert_alpha() # load image of the player #convert_alpha use only the actual pixel of the png
        self.image = pygame.transform.scale(self.image, (PLAYERSIZE_W, PLAYERSIZE_H)) # scale image with the size of Width and Height that we have chose in settings.py
        self.rect = self.image.get_rect(topleft = pos) # create the rect to blit on the screen surface of the same size of the image and position given by pos argument. position is extracted from the "create_map" function in the level class
        self.hitbox = self.rect.inflate(-15,-40) # hitbox(x,y) is another rect of the same size of the precedent, that can be modified to get 3D illusion in collision with other tiles. In this case it's inflate (reduced both sides) by values that allow us to give a fake 3D illusion
        self.animation_speed = 0.15 # FIL?
        self.frame_index = 0 # FIL?
        self.import_player_assets() # cancellabile?
        self.status = 'right_still' #FIL?

        self.direction = pygame.math.Vector2() # will give as a 2d vector to define the player movement
                                               # now x,y = 0, then we want to modify them such as when you pres right x += 1 * player_speed
        self.speed = SPEED # set pix/sec speed of movement of the player, defined in settings.py
        self.obstacle_sprites = obstacle_sprites #instantiate the obstacle_sprites =  pygame.sprite.Group() to use it in this class
                                                 #Build-in class in Pygame that allow to manage multiple sprite at once
        self.block = False # to block the player during dialogues


    ## ??? FIL
    def import_player_assets(self):
        character_path =  "./sprites/characters/"
        frames_dict = {'player_still':[],'player_moove':[]}
        self.animations = {}
        r = range(1,6)
        for img in frames_dict.keys():
            for i in r:
                full_path =  character_path + img + '_'+str(i)+'.png'
                frames_dict[img].append(pygame.image.load(full_path))
        self.animations['right_still'] = [pygame.transform.scale(i, (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_still']]
        self.animations['left_still'] = [pygame.transform.scale(pygame.transform.flip(i, flip_x = True, flip_y=False), (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_still']]
        self.animations['right'] = [pygame.transform.scale(i, (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_moove']]
        self.animations['left'] = [pygame.transform.scale(pygame.transform.flip(i, flip_x = True, flip_y=False), (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_moove']]

    ## Connect the user input with variations in the direction 2D vector
    ## NB the map start from the Origin point (0,0) in the top left corner, if i'm moving right the X encreases, and if the player is moving down, the Y encreases
    def input(self):
            keys = pygame.key.get_pressed() # get input
            if keys[pygame.K_UP]: #If key arrow up is pressed
                self.direction.y = -1 #direction gets value -1 (going up i'm getting closer to the 0y point)
                self.status = self.status.replace('_still','') #FIL?
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = self.status.replace('_still','')
            else:
                self.direction.y = 0 #elif, if no keys are pressed the player doesn't have to move
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

    #FIL?
    def get_status(self):
        if self.direction.y == 0 and self.direction.x == 0:
            if not '_still' in self.status:
                self.status = self.status + '_still'

    ## Use the direction vector (self.direction) to update the player rect position
    def move(self,speed):
        if self.direction.magnitude() != 0: # normalize direction
            self.direction = self.direction.normalize() # if the direction vector is different from 0 it will be normalized (basically, without this pressing e.g. up and right, would move the player faster because of the input of two vectors)
        self.hitbox.x += self.direction.x * speed # modify the self.rect.x position accordingly with the user input 
        self.collision('horizontal') # add the collision in x direction
        self.hitbox.y += self.direction.y * speed # modify the self.rect.x position accordingly with the user input 
        self.collision('vertical') # add the collision in y direction
        self.rect.center = (self.hitbox.centerx, self.hitbox.centery-10)
        
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

    def animate(self):
        animation = self.animations[self.status]

        # loop ove the frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        # set the image
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    
    def update(self):
        if not self.block:
            self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
