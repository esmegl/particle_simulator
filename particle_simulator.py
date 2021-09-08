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

# Retutns the index of the tile I want to select
def flatten_index(x, y):
	index = TILE_INDEX_X * y + x
	return index


# Given the index of the tile, returns the top and left position
def uflattern_index(index):
	# x coordinate
	x = (index % TILE_INDEX_X) 
	# y coordinate
	y = ((index - x) // TILE_INDEX_X) 
	return x, y 


def draw_grid():
	for i in range(0, WINDOW_WIDTH, TILE_SIZE):
		pg.draw.line(SCREEN, L_GREY, (i, 0), (i, WINDOW_HEIGHT), 1)

	for j in range(0, WINDOW_HEIGHT, TILE_SIZE):
		pg.draw.line(SCREEN, L_GREY, (0, j), (WINDOW_WIDTH, j), 1)

# ---------------------------------- Classes ---------------------------------- #

class Sandbox:

	def __init__(self):

		# Grid array size (WINDOW_HEIGHT / TILE_SIZE) * (WINDOW_WIDHT / TILE_SIZE), enumerate the tiles
		self.grid = [0 for i in range(TILE_Q)]
		# Truncate the position of the mouse in both axes
		self.mouse_x = math.floor(pg.mouse.get_pos()[0])
		self.mouse_y = math.floor(pg.mouse.get_pos()[1])

	def sand(self):
		...

	def water(self):
		...

	def smoke(self):
		...

	def fire(self):
		...


	# Checks if a tile is empty
	def is_empty(self, ix) -> bool:

		# Checks if ix is bigger than the last array index
		if ix > TILE_Q:
			empty = False

		else:
			empty = self.grid[ix] == 0

		return empty

	def update (self):

		# Get mouse coordinates converted to tile coordinates 
		self.mouse_x = pg.mouse.get_pos()[0] // TILE_SIZE
		self.mouse_y = pg.mouse.get_pos()[1] // TILE_SIZE 

	
		# Set tile index
		mouse_tile_index = flatten_index(self.mouse_x, self.mouse_y) 

		if pg.mouse.get_pressed(num_buttons=3)[0]:
			# If the mouse is pressed set that tile to 1
			self.grid[mouse_tile_index] = 1

			# Check the empty places for the sand particles to fall
			# Check if the place below is empty
			# self.go_down = self.is_empty(tile_index + TILE_INDEX_X)
			# Check if the place below to the left is empty
			# self.go_left = self.is_empty(tile_index + TILE_INDEX_X - 1) and self.go_down
			# Check if the place below to the right is empty
			# self.go_right = self.is_empty(tile_index + TILE_INDEX_X + 1) and self.go_down
		
		# If both places (left and right) are empty select a place to fall randomly
		# if self.go_left and self.go_right:
		# 	left = random.randint(0, 9)
		# 	right = random.randint(0, 9)

		# 	if left > right:
		# 		self.go_right = False
		# 	else:
		# 		self.go_left = False 

		for i in reversed(range(len(self.grid))):
			# Get the x and y coordinates to draw the rectangle
			(x, y) = uflattern_index(i)

			# Checks if y + 1 is out of range
			if (y + 1 < TILE_INDEX_Y):
				# Tile number of the tile below
				tile_index_d = flatten_index(x, y + 1)

				# Debug
				# print(tile_index_d)

				if (self.grid[i] == 1) and (self.grid[tile_index_d] == 0):
					self.grid[i] = 0
					self.grid[tile_index_d] = 1
			# elif self.go_left and (i + TILE_INDEX_X < len(self.grid)):
			# 	self.grid[i] = 0
			# 	self.grid[i + TILE_INDEX_X - 1] = 1
			# elif self.go_right and ((i + TILE_INDEX_X + 1) <= len(self.grid)):
			# 	self.grid[i] = 0
			# 	self.grid[i + TILE_INDEX_X + 1] = 1


	def draw (self):

		for i in range(len(self.grid)):

			# Don't unflattern indexes that have no rectangles
			if self.grid[i] == 0:
				continue

			x, y = uflattern_index(i)
			r = Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

			if self.grid[i] == 1:
				pg.draw.rect(SCREEN, YELLOW, r, 0)
			elif self.grid[i] == 2:
				pg.draw.rect(SCREEN, BLUE, r, 0)
			elif self.grid[i] == 3:
				pg.draw.rect(SCREEN, L_GREY, r, 0)
			elif self.grid[i] == 4:
				pg.draw.rect(SCREEN, ORANGE, r, 0)



running = False

sandbox = Sandbox()
running = True
# ---------------------------------- Main loop ---------------------------------- #
while running:
	
	# Checks the events
	for event in pg.event.get():
		# Exits the program
		if event.type == QUIT:
			pg.quit()
			sys.exit()


	pg.display.update()
	# Limit the framerate
	CLOCK.tick(FPS)
	SCREEN.fill(BLACK)
	# draw_grid()
	sandbox.update()
	sandbox.draw()

