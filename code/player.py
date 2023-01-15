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
        self.animation_speed = 0.15 # Control the speed on which the player animations are  printed. it multiply self.frame index
        self.frame_index = 0 # an index that is incremented of 1 self.animation.speed per frame and select the player's animation from the list in which they are contained
        self.import_player_assets() # call the import_player_function to fill the self.animation dictionary with the different player's animations
        self.status = 'right_still' # set a player status that determine which animation of the player is printed: right vs. left (in motion) + right_still vs. left_still

        self.direction = pygame.math.Vector2() # will give as a 2d vector to define the player movement
                                               # now x,y = 0, then we want to modify them such as when you pres right x += 1 * player_speed
        self.speed = SPEED # set pix/sec speed of movement of the player, defined in settings.py
        self.obstacle_sprites = obstacle_sprites #instantiate the obstacle_sprites =  pygame.sprite.Group() to use it in this class
                                                 #Build-in class in Pygame that allow to manage multiple sprite at once
        self.block = False # to block the player during dialogues


    ## Function to load the player's animations and put them in list in the self.animations disctionary dividing them in categories: right vs. left (in motion) + right_still vs. left_still
    def import_player_assets(self):
        character_path =  "./sprites/characters/" # select the path root
        frames_dict = {'player_still':[],'player_moove':[]} # create a dict with the two set of images, one for the motion animation and the other for the still animation
        self.animations = {} # create the final animation dict
        r = range(1,6)
        for img in frames_dict.keys(): # iterate over the two keys of the dict
            for i in r: # for i in r = 6
                full_path =  character_path + img + '_'+str(i)+'.png' # generate the full path for the images: path root + img name from the keys + index + .png: an image names could be 'player_still_1.png'
                frames_dict[img].append(pygame.image.load(full_path)) # load the img and append in the dict list
        ## Fill the final animation dict with the right transformation of the images: scaling them to the right PLAYERSIZE and flip theem to make all the left animations
        self.animations['right_still'] = [pygame.transform.scale(i, (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_still']]
        self.animations['left_still'] = [pygame.transform.scale(pygame.transform.flip(i, flip_x = True, flip_y=False), (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_still']]
        self.animations['right'] = [pygame.transform.scale(i, (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_moove']]
        self.animations['left'] = [pygame.transform.scale(pygame.transform.flip(i, flip_x = True, flip_y=False), (PLAYERSIZE_W, PLAYERSIZE_H)) for i in frames_dict['player_moove']]

    ## Connect the user input with variations in the direction 2D vector
    ## NB the map start from the Origin point (0,0) in the top left corner, if i'm moving right the X encreases, and if the player is moving down, the Y encreases
    def input(self):
            keys = pygame.key.get_pressed() # get input
            if keys[pygame.K_UP]: #If key arrow up is pressed
                self.direction.y = -1 # direction gets value -1 (going up i'm getting closer to the 0y point)
                self.status = self.status.replace('_still','') # Set the player status to indicate which animation to print, replace still with '' void, to indicate that the player is mooving
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = self.status.replace('_still','')
            else:
                self.direction.y = 0 # else, if no keys are pressed the player doesn't have to move
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

    ## Set the player status to indicate which animation to print
    def get_status(self):
        if self.direction.y == 0 and self.direction.x == 0: # If there is no input for the player, set the state on _still to print the still animation
            if not '_still' in self.status:
                self.status = self.status + '_still' # + _still because the 'left' or 'right' status is always preserved

    ## Use the direction vector (self.direction) to update the player rect position
    def move(self,speed):
        if self.direction.magnitude() != 0: # normalize direction
            self.direction = self.direction.normalize() # if the direction vector is different from 0 it will be normalized (basically, without this pressing e.g. up and right, would move the player faster because of the input of two vectors)
        self.hitbox.x += self.direction.x * speed # modify the self.rect.x position accordingly with the user input 
        self.collision('horizontal') # add the collision in x direction
        self.hitbox.y += self.direction.y * speed # modify the self.rect.x position accordingly with the user input 
        self.collision('vertical') # add the collision in y direction
        self.rect.center = (self.hitbox.centerx, self.hitbox.centery-10) # set the center of the player's rect. With self.hitbox = self.rect.inflate(-15,-40) we reduce the size of the player's rectangle of tot pixel in the two dimensions, with this we set the position of this rectangle, shifting it of an additional 10px on the y axe to allow the player's immage to overlap with other objects more on the top than on the bottom
        
    ## Define collisions
    def collision(self,direction):
        if direction == 'horizontal': # if the movement is within the x dimension of the direction vector 
            for sprite in self.obstacle_sprites: #loop through all the sprites
                if sprite.hitbox.colliderect(self.hitbox): #if there is a collision with one of the sprite in the obstacle_sprite group
                    if self.direction.x > 0: # if moving right, means that is colliding with the right side of its rect
                        self.hitbox.right = sprite.hitbox.left #then move the player to the left side of the rect of the object with is colliding with
                    if self.direction.x < 0: # if moving left, means that is colliding with the left side of its rect
                        self.hitbox.left = sprite.hitbox.right #then move the player to the right side of the rect of the object with is colliding with
        if direction == 'vertical': # if the movement is within the y dimension of the direction vector 
            for sprite in self.obstacle_sprites:  #loop through all the sprites
                if sprite.hitbox.colliderect(self.hitbox): #if there is a collision with one of the sprite in the obstacle_sprite group
                    if self.direction.y > 0: # if moving down, means that is colliding with the bottom side of its rect
                        self.hitbox.bottom = sprite.hitbox.top #then move the player to the top side of the rect of the object with is colliding with
                    if self.direction.y < 0: # if moving up, means that is colliding with the top side of its rect
                        self.hitbox.top = sprite.hitbox.bottom #then move the player to the bottom side of the rect of the object with is colliding with

    ## Methods for player animations 
    def animate(self):
        animation = self.animations[self.status] # get the animation list corresponding to the player status

        # loop ove the frame index (each time this function is called)
        self.frame_index += self.animation_speed # for a determined animation speed
        if self.frame_index >= len(animation): # if the len of the index become bigger than the size of the animation list, set it to 0 
            self.frame_index = 0
        # set the image
        self.image = animation[int(self.frame_index)] # with the index select the corresponding animation in the list (the index has to be an int to make the selection)
        self.rect = self.image.get_rect(center = self.hitbox.center) # create the rect of the image setting it's center to the actual player rect.center

    #Method called in level class in run method to update all the player methods
    def update(self):
        if not self.block: # if a dialogue is happening self.block is set to True
            self.input() # get input
        self.get_status() # set status
        self.animate() # get the corresponding animations
        self.move(self.speed) # compute the position of the player's rect

        ### WHY THERE IS NOT ANY PRINT/DRAW/BLIT FUNCTION?
        # The player class is istantiated in the level file with:
        # self.player = Player((1600,2300),[self.visible_sprites], self.obstacle_sprites), where the first argument is the starting position in the map
        # it is then drew on the main game screen in leve.run with 
        # self.visible_sprites.custom_draw(self.player)
        # and updated with:
        # self.visible_sprites.update()

        # These functions apply to the player because it is set as an element of the self.visible_sprites group. So every function called on this group is called on the player instance
