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
		self.sand = 1
		self.water = 2
		self.smoke = 3
		self.fire = 4
		self.explotion = 5

	def update (self):

		# Get mouse coordinates converted to tile coordinates 
		self.mouse_x = pg.mouse.get_pos()[0] // TILE_SIZE
		self.mouse_y = pg.mouse.get_pos()[1] // TILE_SIZE 

	
		# Set tile index
		mouse_tile_index = flatten_index(self.mouse_x, self.mouse_y) 

		if pg.mouse.get_pressed(num_buttons=3)[0]:
			# If the mouse is pressed set that tile to 1
			self.grid[mouse_tile_index] = 1
		

		for i in range(len(self.grid), 0, -1):
			# Get the x and y coordinates to draw the rectangle
			(x, y) = uflattern_index(i)

			# If both places (left and right) are empty select a place to fall randomly
			left = random.randint(0, 9)
			right = random.randint(0, 9)

			# Checks if y + 1 is out of range
			if (y + 1 < TILE_INDEX_Y):
				# Tile number of the tile below
				tile_index_d = flatten_index(x, y + 1)
				# Index down to the left
				tile_index_dl = flatten_index(x - 1, y + 1)

				# If the space below is empty "fall"
				if (self.grid[i] == 1) and (self.grid[tile_index_d] == 0):
					self.grid[i] = 0
					self.grid[tile_index_d] = 1

				# If the space below is not empty fall to the sides
				# Prevents (x + 1) or (x -1) are out of range
				elif (self.grid[tile_index_d] == 1) and (x - 1) > 0 and (x + 1) < TILE_INDEX_X:
					
					# If the space down is taken, fall left or right
					if (left > right) and (self.grid[tile_index_dl] == 0):
						self.grid[i] = 0
						self.grid[tile_index_dl] = 1
						# print(tile_index_dl)

					# else: 
					# 	# Index down to the right
					# 	tile_index_dr = flatten_index(x + 1, y)

					# 	if (left <= right) and self.grid[tile_index_dr] == 0:
					# 		self.grid[i] = 0
					# 		self.grid[tile_index_dr] = 1


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

# class Button:
 
#     def __init__(self, text, bg="BLACK", feedback=""):
#         self.pos = (0, 0)
#         self.font = pg.font.SysFont("Arial", font)
#         if feedback == "":
#             self.feedback = "text"
#         else:
#             self.feedback = feedback
#         self.change_text(text, bg)
 
#     def change_text(self, text, bg="BLACK"):
#         """Change the text whe you click"""
#         self.text = self.font.render(text, 1, pg.Color("WHITE"))
#         self.size = self.text.get_size()
#         self.surface = pg.Surface(self.size)
#         self.surface.fill(bg)
#         self.surface.blit(self.text, (0, 0))
#         self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
 
#     def show(self):
#         screen.blit(button1.surface, (self.x, self.y))
 
#     def click(self, event):
#         x, y = pg.mouse.get_pos()
#         if event.type == pg.MOUSEBUTTONDOWN:
#             if pg.mouse.get_pressed()[0]:
#                 if self.rect.collidepoint(x, y):
#                     self.change_text(self.feedback, bg="RED")


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

		if event.type == pg.K_e:
			print("E pressed")

	pg.display.update()
	# Limit the framerate
	CLOCK.tick(FPS)
	SCREEN.fill(BLACK)
	# draw_grid()
	sandbox.update()
	sandbox.draw()

