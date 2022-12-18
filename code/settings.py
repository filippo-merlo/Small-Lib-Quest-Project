### GAME SETUP

## Get the current pc screen's size 
from screeninfo import get_monitors
monitor_sizes = get_monitors()
screen_width = monitor_sizes[0].width # screen's width
screen_height = monitor_sizes[0].height # screen's height
# Set the game window' size
WIDTH = int(screen_width-screen_width*0.1) # to reduce it of 10%
HEIGHT = int(screen_height-screen_height*0.1) # to reduce it of 10%


FPS = 60 # set frame rate
ZOOM = 3
TILESIZE = 16*ZOOM # size of tiles
PLAYERSIZE = TILESIZE*2 # set the player size
SPEED = 20



