import pygame

### Define a debug function to print in real time on the screen text output
### Useful during work-in-progress to check the state of a variable

pygame.init()
font = pygame.font.Font(None,30) # func to create a new font object from a file, the first arg will be specified forward

def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface() # get the actual window's surface
    debug_surf = font.render(str(info),True,'White') # set the str to display in the debug message
    debug_rect = debug_surf.get_rect(topleft = (x,y)) # get_rect generate a new rect of the size of the surface on which is called, with standard pos of (0,0)
    pygame.draw.rect(display_surface, 'Black', debug_rect) # draw.rect draws a rectangle on a surface (where,color,the rect)
    display_surface.blit(debug_surf,debug_rect) # blit draws one image onto another