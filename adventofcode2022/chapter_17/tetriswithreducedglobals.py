
import sys
import numpy as np
from PIL import Image
import copy

MAX_BLOCK_COUNT = 1000000000000
MAP_WIDTH = 7

MAP_HEIGHT = 100000


width_ranges = {}
#AMOUNT_SHAPES = len(shapes)
AMOUNT_SHAPES = 5
dx_for_moves = {60: -1, 62: 1}
shape_widths = [4,3,3,1,2]

heights = [1,3,3,4,2]

block_col_heights = {0: [1,1,1,1],1: [2,3,2], 2:[3,1,1], 3: [4], 4: [2,2]} # the heights of the blocks at each column.

states = {}

loop_found = False

col_heights = [0]*MAP_WIDTH

def check_col(shape, x_coord, y_coord, game_map):
	shape_shape = shape.shape
	x_diff = shape_shape[1]
	y_diff = shape_shape[0]
	game_map_section = game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff]
	for i in range(x_diff):
		for j in range(y_diff):
			if game_map_section[i,j] == 1 and shape[j,i]:
				return True
	return False

def place_block(shape, x_coord, y_coord, game_map):
	shape_shape = shape.shape
	x_diff = shape_shape[1]
	y_diff = shape_shape[0]
	game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff] |= shape.T

	return game_map

def update_col_heights(shape_num, x_coord, y_coord, shapes):
	# This updates the column heights so we do not need to check them later.
	for i in range(x_coord, shapes[shape_num].shape[1]+x_coord):
		h = block_col_heights[shape_num][i-x_coord]
		if col_heights[i] < h + y_coord-1:
			col_heights[i] = h + y_coord-1

# Check the actual height of the block tower.
# actual_height = check_height(game_map)


def check_height(game_map):
	h = 0
	shitoof = copy.deepcopy(game_map)
	shitoof = shitoof.T
	oof = shitoof[h]

	while not np.all(oof == 0):
		h += 1
		oof = shitoof[h]

	return h


def update_width_ranges(shape_num, x_coord, y_coord, shapes):

	# width_ranges is a list of ranges where all of the possible collision zones are stored in.
	shape = shapes[shape_num]
	shape_width = shape.shape[1] # width of the shape
	shape_height = shape.shape[0] # height of the shape
	new_range = [x_coord,x_coord+shape_width]

	for i in range(shape_height):

		for j in range(new_range[0], new_range[1]):

			if y_coord+i not in width_ranges:

				width_ranges[y_coord+i] = {j:1}

			else:

				width_ranges[y_coord+i][j] = 1

	return

def check_width_ranges(shape,x_coord,y_coord):

	width = shape.shape[1]
	height = shape.shape[0]

	for h in range(height):
		y = y_coord + h
		if y in width_ranges:
			x_occupied = width_ranges[y]
			for w in range(width):
				x = x_coord + w
				if x in x_occupied:
					return True
	return False

def main_loop(game_map,moves):

	SHAPE_1 = np.array([[1,1,1,1]],dtype=bool)

	SHAPE_2 = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=bool)

	SHAPE_3 = np.array([[1,1,1],[0,0,1],[0,0,1]],dtype=bool)

	SHAPE_4 = np.array([[1],[1],[1],[1]],dtype=bool)

	SHAPE_5 = np.array([[1,1],[1,1]],dtype=bool)

	shapes = [SHAPE_1, SHAPE_2, SHAPE_3, SHAPE_4, SHAPE_5]


	n = 0
	loop_counter = 0
	tower_height = 0
	rendering = False
	render_oof = True
	loop_found = False
	render_shit = 0

	while n < MAX_BLOCK_COUNT:

		x_coord = 2
		x_coord_prev = 2
		skipcount = 3
		
		cur_height = heights[n % AMOUNT_SHAPES]

		y_coord = tower_height + 3


		shape = shapes[n % AMOUNT_SHAPES]



		if n == 6:
			rendering = True

		else:
			if rendering:
				rendering = False


		while True:
			if loop_counter == len(moves):
				loop_counter = 0

			cur_move = moves[loop_counter]

			dx = dx_for_moves[cur_move]
			x_coord += dx
			blocked = False
			if x_coord < 0:
				x_coord -= dx
				blocked = True

			
			if x_coord + shape_widths[n % AMOUNT_SHAPES] > MAP_WIDTH:
				if not blocked:

					x_coord -= dx
					blocked = True


			if check_col(shape, x_coord, y_coord, game_map):


				if not blocked:

					x_coord -= dx
					blocked = True




			x_coord_prev = x_coord

			y_coord -= 1

			loop_counter = (loop_counter + 1) % len(moves)

			if y_coord == -1:

				y_coord += 1

				place_block(shape, x_coord, y_coord, game_map)
				update_col_heights(n % AMOUNT_SHAPES, x_coord,y_coord, shapes)
				update_width_ranges(n % AMOUNT_SHAPES, x_coord, y_coord, shapes)
				n += 1
				if y_coord+cur_height > tower_height: # no need to check for ones in the shape matrix because the first line always contains atleast one "1" .
					tower_height = y_coord+cur_height
				break

			if skipcount > 0:
				skipcount -= 1
			elif check_width_ranges(shape,x_coord,y_coord):
				if check_col(shape, x_coord, y_coord, game_map):

					y_coord += 1

					place_block(shape, x_coord, y_coord, game_map)
					update_col_heights(n % AMOUNT_SHAPES, x_coord,y_coord, shapes)
					update_width_ranges(n % AMOUNT_SHAPES, x_coord, y_coord, shapes)
					n += 1
					if y_coord+cur_height > tower_height: # no need to check for ones in the shape matrix because the first line always contains atleast one "1" .
						tower_height = y_coord+cur_height

					break

		if not loop_found:

			new_state = []
			lowest = 10000
			for i in range(MAP_WIDTH):
				h = 0

				new_state.append(col_heights[i])
				if col_heights[i] < lowest:
					lowest = col_heights[i]

			state = [x - lowest for x in new_state] # The difference between shit.
			state += [(n-1)%AMOUNT_SHAPES, loop_counter] # current 

			state = tuple(state)

			if state in states:

				height_gain = tower_height - states[state][0]

				rock_num = n - states[state][1]

				skipped = (MAX_BLOCK_COUNT - n) // rock_num

				n += skipped * rock_num

				loop_found = True
			else:
				states[state] = [tower_height, n]
		




	if not loop_found:

		return tower_height
	else:

		return tower_height + (skipped * height_gain)



def parse_input():

	return sys.stdin.buffer.read()#.decode('ascii')


def solve_puzzle():

	moves = parse_input()

	game_map = np.zeros((MAP_WIDTH, MAP_HEIGHT),dtype=bool)       #.astype("bool")



	height = main_loop(game_map,moves)

	#result = get_height(game_map)

	return height






if __name__=="__main__":
	print("Solution to puzzle: "+str(solve_puzzle()))
	exit(0)
