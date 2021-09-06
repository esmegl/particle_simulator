import pygame as pg
import time

# ---------------------------------- Game settings ---------------------------------- #

TITLE = "Particle Simulator"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
AREA = WINDOW_WIDTH * WINDOW_HEIGHT
FRICTION = 0.05
ACCELERATION = 9.8
FPS = 60

# Grid box size
TILE_SIZE = 5
TILE_INDEX_X = WINDOW_WIDTH // TILE_SIZE
TILE_INDEX_Y = WINDOW_HEIGHT // TILE_SIZE

# Total number of tiles
TILE_Q = int(WINDOW_HEIGHT / TILE_SIZE) * int(WINDOW_WIDTH / TILE_SIZE)

# ---------------------------------- Colors ---------------------------------- #
#           R	 G    B
WHITE =   (255, 255, 255)
BLACK =   (  0,   0,   0)
RED =	  (255,   0,   0)   
GREEN =   (  0, 255,   0)
BLUE =	  ( 61, 157, 212)
ORANGE =  (255, 111,   0)
YELLOW =  (212, 187,  61)
VIOLET =  (205,   0, 255)
L_GREY =  (212, 210, 210)
BGCOLOR = ( 32,  53, 111)