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

# ---------------------------------- Variables ---------------------------------- #



# ---------------------------------- Classes ---------------------------------- #

class Sandbox:

	def __init__(self, val=0):

		# Grid array size (WINDOW_HEIGHT / TILE_SIZE) * (WINDOW_WIDHT / TILE_SIZE), enumerate the tiles
		self.grid = [0 for i in range(TILE_Q)]
		# Truncate the position of the mouse in both axes
		self.mouse_x = math.floor(pg.mouse.get_pos()[0])
		self.mouse_y = math.floor(pg.mouse.get_pos()[1])
		self.sand = 1
		self.water = 2
		self.smoke = 3
		self.fire = 4
		self.acid = 5
		self.val = val

	def update (self, val):

		# Get mouse coordinates converted to tile coordinates 
		self.mouse_x = pg.mouse.get_pos()[0] // TILE_SIZE
		self.mouse_y = pg.mouse.get_pos()[1] // TILE_SIZE 

	
		# Set tile index
		mouse_tile_index = flatten_index(self.mouse_x, self.mouse_y) 

		# If the mouse is pressed set that tile to val if the value of the tile is 0
		if pg.mouse.get_pressed(num_buttons=3)[0] and self.grid[mouse_tile_index] == 0:
			self.grid[mouse_tile_index] = val

		

		for i in range(len(self.grid), 0, -1):
			# Get the x and y coordinates to draw the rectangle
			x, y = uflattern_index(i)

			# If both places (left and right) are empty select a place to go randomly
			left = random.randint(0, 9)
			right = random.randint(0, 9)


			# Index of the above tile
			tile_index_u = flatten_index(x, y - 1)
			# Index of the tile tile above to the left
			tile_index_ul = flatten_index(x - 1, y - 1)
			# Index of the tile above to the right
			tile_index_ur = flatten_index(x + 1, y - 1)
			# Tile number of the tile below
			tile_index_d = flatten_index(x, y + 1)
			# Index below to the left
			tile_index_dl = flatten_index(x - 1, y + 1)
			# Index below to the rigth
			tile_index_dr = flatten_index(x + 1, y + 1)
			# Index of the tile to the left
			tile_index_l = flatten_index(x - 1, y)
			# Index of the tile to the rigth
			tile_index_r = flatten_index(x + 1, y)


# ------------------------------------- Sand physics ------------------------------------- #

			if tile_index_d < len(self.grid) and (val == self.sand):

				# If the space below is empty "fall"
				if (self.grid[i] == self.sand) and (self.grid[tile_index_d] == 0):
					self.grid[i] = 0
					self.grid[tile_index_d] = self.sand

				# If the space below is not empty fall to the sides
				# Prevents (x + 1) or (x -1) are out of range
				elif (self.grid[i] == self.sand) and (self.grid[tile_index_d] != 0) and tile_index_dl < len(self.grid) and tile_index_dr < len(self.grid):
					
					# If the space down is taken, fall left or right
					if (left > right) and (self.grid[tile_index_dl] == 0) and (self.grid[tile_index_l] == 0):
						self.grid[i] = 0
						self.grid[tile_index_dl] = self.sand

					elif self.grid[tile_index_dr] == 0 and (self.grid[tile_index_r] == 0):
						self.grid[i] = 0
						self.grid[tile_index_dr] = self.sand

# ------------------------------------- Water physics ------------------------------------- #	

			if tile_index_d < len(self.grid) and (val == self.water):

				# If the space below is empty "fall"
				if (self.grid[i] == self.water) and (self.grid[tile_index_d] == 0):
					self.grid[i] = 0
					self.grid[tile_index_d] = self.water

				# If the space below is not empty fall to the sides
				# Prevents (x + 1) or (x -1) are out of range
				elif (self.grid[i] == self.water) and (self.grid[tile_index_d] != 0):

					# If the space down is taken, fall left or right
					if (left > right) and (self.grid[tile_index_l] == 0) and tile_index_l < len(self.grid):
						self.grid[i] = 0
						self.grid[tile_index_l] = self.water

					elif (self.grid[tile_index_r] == 0) and tile_index_r < len(self.grid):
						self.grid[i] = 0
						self.grid[tile_index_r] = self.water

					# elif (self.grid[tile_index_dl] == )


# ------------------------------------- Smoke physics ------------------------------------- #

			if tile_index_u > len(self.grid) and val == self.smoke:
				print("**********Step one: enter if statement, works!**********")
				# If the space above is empty "fly"
				if (self.grid[i] == self.smoke) and (self.grid[tile_index_u] == 0):
					self.grid[i] = 0
					self.grid[tile_index_u] = self.smoke
					print("**********Step two: Fly, works!**********")

				# If the space above is not empty 'fly' to the sides
				# Prevents (x + 1) or (x -1) are out of range
				elif (self.grid[i] == self.smoke) and (self.grid[tile_index_u] != 0) and tile_index_ul < len(self.grid) and tile_index_ur < len(self.grid):
					
					if (left > right) and (self.grid[tile_index_ul] == 0):
						self.grid[i] = 0
						self.grid[tile_index_ul] = self.smoke
						print("**********Step three: Go left, works!**********")

					elif self.grid[tile_index_ur] == 0:
						self.grid[i] = 0
						self.grid[tile_index_ur] = self.smoke
						print("**********Step four: Go rigth, works!**********")



	def draw (self):

		for i in range(len(self.grid)):

			# Don't unflattern indexes that have no rectangles
			if self.grid[i] == 0:
				continue

			x, y = uflattern_index(i)
			r = Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

			if self.grid[i] == self.sand:
				pg.draw.rect(SCREEN, YELLOW, r, 0)
			elif self.grid[i] == self.water:
				pg.draw.rect(SCREEN, BLUE, r, 0)
			elif self.grid[i] == self.smoke:
				pg.draw.rect(SCREEN, L_GREY, r, 0)
			elif self.grid[i] == self.fire:
				pg.draw.rect(SCREEN, ORANGE, r, 0)
			elif self.grid[i] == self.acid:
				pg.draw.rect(SCREEN, GREEN, r, 0)

	def erase(self):
		self.grid = [0 for i in range(TILE_Q)]



class Button():

	def __init__(self, color, color_txt, x, y, font_size, text=''):
		self.color = color
		self.x = x
		self.y = y
		self.width = BUT_WIDTH
		self.height = BUT_HEIGHT
		self.text = text
		self.color_txt = color_txt
		self.font_size = font_size

	def is_over(self, pos):
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		
		return False 

	def draw(self, SCREEN):
            
		pg.draw.rect(SCREEN, self.color, (self.x,self.y,self.width,self.height),0)
        
		if self.text != '':
			font = pg.font.SysFont('comicsans', self.font_size)
			text = font.render(self.text, 1, self.color_txt)
			# Center the text in the middle of the rectangle
			SCREEN.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
 

sandbox = Sandbox()
erase_button = Button(BLACK, WHITE, WINDOW_WIDTH - BUT_WIDTH - 10, 10, 30, "E")
sand_button = Button(YELLOW, WHITE, WINDOW_WIDTH - BUT_WIDTH - 10, BUT_HEIGHT + 20, 30, "S")
water_button = Button(BLUE, WHITE, WINDOW_WIDTH - BUT_WIDTH - 10, BUT_HEIGHT + 60, 30, "W")
smoke_button = Button(L_GREY, BLACK, WINDOW_WIDTH - BUT_WIDTH - 10, BUT_HEIGHT + 100, 30, "K")
fire_button = Button(ORANGE, WHITE, WINDOW_WIDTH - BUT_WIDTH - 10, BUT_HEIGHT + 140, 30, "F")
acid_button = Button(GREEN, WHITE, WINDOW_WIDTH - BUT_WIDTH - 10, BUT_HEIGHT + 180, 30, "A")

# Initial value of val (sand)
val = 1
running = True
# ---------------------------------- Main loop ---------------------------------- #
while running:
	
	# Checks the events
	for event in pg.event.get():
		# Exits the program
		if event.type == QUIT:
			pg.quit()
			sys.exit()

		# Select the type of particle
		pos = pg.mouse.get_pos()
		if event.type == pg.MOUSEBUTTONDOWN:
			if erase_button.is_over(pos):
				val = 0
				sandbox.erase()
			elif sand_button.is_over(pos):
				val = 1
			elif water_button.is_over(pos):
				val = 2
			elif smoke_button.is_over(pos):
				val = 3
			elif fire_button.is_over(pos):
				val = 4
			elif acid_button.is_over(pos):
				val = 5
				
		# If the mouse is over a button, change color of the button
		if event.type == pg.MOUSEMOTION:
			if erase_button.is_over(pos):
				erase_button.color = L_GREY
			else:
				erase_button.color = BLACK

			if sand_button.is_over(pos):
				sand_button.color = YELLOW
			else:
				sand_button.color = D_YELLOW

			if water_button.is_over(pos):
				water_button.color = BLUE
			else:
				water_button.color = D_BLUE

			if smoke_button.is_over(pos):
				smoke_button.color = L_GREY
			else:
				smoke_button.color = GREY

			if fire_button.is_over(pos):
				fire_button.color = ORANGE
			else:
				fire_button.color = D_ORANGE

			if acid_button.is_over(pos):
				acid_button.color = GREEN
			else:
				acid_button.color = D_GREEN



	pg.display.update()
	# Limit the framerate
	CLOCK.tick(FPS)
	SCREEN.fill(BGCOLOR)
	# draw_grid()
	sandbox.update(val)
	sandbox.draw()
	erase_button.draw(SCREEN)
	sand_button.draw(SCREEN)
	water_button.draw(SCREEN)
	smoke_button.draw(SCREEN)
	fire_button.draw(SCREEN)
	acid_button.draw(SCREEN)
