import pygame as pg
import time

# ---------------------------------- Game settings ---------------------------------- #

TITLE = "Particle Simulator"
# FONT = pg.font.Font("./wattauchimma/Wattauchimma.ttf", 20)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
AREA = WINDOW_WIDTH * WINDOW_HEIGHT
FRICTION = 0.05
ACCELERATION = 9.8
FPS = 30

# Grid box size
TILE_SIZE = 10
TILE_INDEX_X = WINDOW_WIDTH // TILE_SIZE
TILE_INDEX_Y = WINDOW_HEIGHT // TILE_SIZE

# Total number of tiles
TILE_Q = int(WINDOW_HEIGHT / TILE_SIZE) * int(WINDOW_WIDTH / TILE_SIZE)

# ---------------------------------- Button settings ---------------------------------- #

BUT_WIDTH = 80
BUT_HEIGHT = 80

# ---------------------------------- Colors ---------------------------------- #
#           R	 G    B   A
WHITE =   (255, 255, 255,  1)
BLACK =   (  0,   0,   0,  1)
RED =	  (255,   0,   0,  1)   
GREEN =   (  0, 255,   0,  1)
BLUE =	  ( 61, 157, 212,  1)
ORANGE =  (255, 111,   0,  1)
YELLOW =  (212, 187,  61,  1)
VIOLET =  (205,   0, 255,  1)
L_GREY =  (212, 210, 210,  1)
BGCOLOR = ( 32,  53, 111,  1)

