from screeninfo import get_monitors

### GAME SETUP
## Get the current pc screen's size 
monitor_sizes = get_monitors()
screen_width = monitor_sizes[0].width # screen's width
screen_height = monitor_sizes[0].height # screen's height

## Other in-game parameters 
FPS = 60 # set frame rate
ZOOM = 3 #Parameter to scale the map to the screen
TILESIZE = 16*ZOOM # size of tiles
PLAYERSIZE_W = TILESIZE*1.2 # set the player Width in size
PLAYERSIZE_H = TILESIZE*1.7# set the player Height size
SPEED = 10 #set the speed of the player (in movement)

# Font
FONT_SIZE = 17 #set the general font