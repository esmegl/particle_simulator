import math, random, sys
import pygame as pg 
from pygame.locals import *
from settings import *

# ---------------------------------- Initialize display ---------------------------------- #
pg.init()
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption(TITLE)

# ---------------------------------- Functions ---------------------------------- #

def draw_grid():
	for i in range(0, WINDOW_WIDTH, TILE_SIZE):
		pg.draw.line(SCREEN, L_GREY, (i, 0), (i, WINDOW_HEIGHT), 1)

	for j in range(0, WINDOW_HEIGHT, TILE_SIZE):
		pg.draw.line(SCREEN, L_GREY, (0, j), (WINDOW_WIDTH, j), 1)

# Checks if the surrounding tiles are empty
def is_empty (x, y) -> bool:
	...

# ---------------------------------- Classes ---------------------------------- #

""" class Sand:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		...

	def update (self):

		# Check if the mouse was pressed
		if pg.mouse.get_pressed(num_buttons=3)[0]:
			...

		# Check the empty places for the sand particles to fall
		self.go_down = is_empty(x, y + 1)
		self.go_left = is_empty(x - 1, y)
		self.go_right = is_empty(x + 1, y)
		
		# If both places (left and right) are empty select a place to fall randomly
		if self.go_left and self.go_right:
			left = random.randint(0, 9)
			right = random.randint(0, 9)

			if left > right:
				self.go_right = False
			else:
				self.go_left = False

	def draw (self):
		...
"""

class Water:

	...

class Smoke:

	# is_up = is_up = is_empty(x, y - 1)
	...

# Initial mouse positon
x = pg.mouse.get_pos()[0]
y = pg.mouse.get_pos()[1]

# sand = Sand(x, y)

# square = Square()

running = True
# ---------------------------------- Main loop ---------------------------------- #
while running:
	
	# Checks the events
	for event in pg.event.get():
		# Exits the program
		if event.type == QUIT:
			pg.quit()
			sys.exit()

		# Checks if the mouse is pressed
		# print(pg.mouse.get_pressed(num_buttons=3)[0])


	# selected_particle = 
	draw_grid()

	pg.display.update()
	# Limit the framerate
	CLOCK.tick(FPS)
	SCREEN.fill(BLACK)
	# square.update()
	# square.draw()

