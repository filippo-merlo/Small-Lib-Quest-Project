#%%
import pygame, sys
from settings import *
from tile import Tile, Object_Tile
from player import Player
from debug import debug
from pytmx.util_pygame import load_pygame # module of tmxpy that works for pygame
from pygame.locals import *

SIZE = 800, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = Rect(50, 60, 200, 80)
print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
print(f'center={rect.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                rect = Rect(rect.x, rect.y+50, rect.w, rect.h-50)
        

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    pygame.display.flip()

pygame.quit()

