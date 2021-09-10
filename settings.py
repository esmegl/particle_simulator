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

# ---------------------------------- Button settings ---------------------------------- #

BUT_WIDTH = 30
BUT_HEIGHT = 30

# ---------------------------------- Grid settings ---------------------------------- #

# Grid box size
TILE_SIZE = 20
TILE_INDEX_X = WINDOW_WIDTH // TILE_SIZE
TILE_INDEX_Y = WINDOW_HEIGHT // TILE_SIZE

# Total number of tiles
TILE_Q = int(WINDOW_HEIGHT / TILE_SIZE) * int(WINDOW_WIDTH / TILE_SIZE)

# ---------------------------------- Colors ---------------------------------- #
#            R	  G    B   A
WHITE =    (255, 255, 255,  1)
BLACK =    (  0,   0,   0,  1)
D_RED =	   (229,  46,  46,  1)
RED =      (207,  88,  87,  1)
D_GREEN =  (108, 185,  80,  1)   
GREEN =    (151, 223,  96,  1)
D_BLUE =   ( 68, 150, 212,  1)
BLUE =     ( 67, 192, 231,  1)
D_ORANGE = (212, 122,  71,  1)
ORANGE =   (229, 148,  72,  1)
D_YELLOW = (214, 187, 102,  1)
YELLOW =   (239, 189,  98,  1)
VIOLET =   (167,  60, 112,  1)
D_VIOLET = (118,  26,  53,  1)
GREY =     (165, 165, 165,  1)
L_GREY =   (212, 210, 210,  1)
BGCOLOR =  ( 32,  53, 111,  1)

