import math, random, sys
import pygame as pg 
from pygame.locals import *
from settings import *

#initialize display
pg.init()
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)

class Sand:

	def __init__(self):
		...

class Water:

	def __init__(self):
		...

class Smoke:

	def __init__(self):
		...

pg.mouse.set_cursor(*pg.cursors.arrow)


running = True
#main loop
while running:
	
	#checks the events
	for event in pg.event.get():
		#exits the program
		if event.type == QUIT:
			pg.quit()
			sys.exit()

	pg.display.update()
	CLOCK.tick(FPS)
	SCREEN.fill(BLACK)
