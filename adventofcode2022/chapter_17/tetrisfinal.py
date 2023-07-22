
import sys
import numpy as np
from PIL import Image
import copy

#MAX_BLOCK_COUNT = 2022

MAX_BLOCK_COUNT = 1000000000000
#MAX_BLOCK_COUNT = 100

MAP_WIDTH = 7

#MAP_HEIGHT = 10
#MAP_HEIGHT = 100000
MAP_HEIGHT = 10000000
SHAPE_1 = np.array([[1,1,1,1]],dtype=bool)

SHAPE_2 = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=bool)

#SHAPE_3 = np.array([[0,0,1],[0,0,1],[1,1,1]])

SHAPE_3 = np.array([[1,1,1],[0,0,1],[0,0,1]],dtype=bool)

SHAPE_4 = np.array([[1],[1],[1],[1]],dtype=bool)

SHAPE_5 = np.array([[1,1],[1,1]],dtype=bool)

shapes = [SHAPE_1, SHAPE_2, SHAPE_3, SHAPE_4, SHAPE_5]


#width_ranges = [ [] for _ in range(MAP_HEIGHT) ]


AMOUNT_SHAPES = len(shapes)

dx_for_moves = {"<": -1, ">": 1}

shape_widths = [4,3,3,1,2]

heights = [1,3,3,4,2]

#block_col_heights = {SHAPE_1: [1,1,1,1],SHAPE_2: [2,3,2], SHAPE_3:[3,1,1], SHAPE_4: [4], SHAPE_5: [2,2]} # the heights of the blocks at each column.
block_col_heights = {0: [1,1,1,1],1: [2,3,2], 2:[3,1,1], 3: [4], 4: [2,2]} # the heights of the blocks at each column.

states = {}

loop_found = False

col_heights = [0]*MAP_WIDTH

def render_mat(mat):
	return
	qr_matrix = np.invert(mat.astype(bool), dtype=bool)
	##print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()
	#input()





def check_col(shape, x_coord, y_coord, game_map):

	shape_shape = shape.shape
	x_diff = shape_shape[1]
	y_diff = shape_shape[0]
	#thing = shape.astype("float64")
	#thing = shape.astype("bool")
	###print("x_diff: "+str(x_diff))
	###print("y_diff: "+str(y_diff))

	#game_map_section = game_map[y_coord:y_coord+y_diff,x_coord:x_coord+x_diff]
	#game_map_section = game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff]

	#game_map_section = game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff]


	#game_map_section = game_map[y_coord:y_coord+y_diff,x_coord:x_coord+x_diff]

	game_map_section = game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff]


	# check with binary and operation for intersection.

	###print("type(game_map) == "+str(type(game_map)))
	###print("type(thing) == "+str(type(thing)))
	###print("type(game_map_section) == "+str(type(game_map_section)))
	
	###print("game_map_section == "+str(game_map_section))
	###print("thing == "+str(thing))

	# This method is inefficient because it does more operations than strictly necessary.

	#intersect = (game_map_section.astype("bool") & thing.T)


	# Go through each of the elements and then break if an intersection is found.

	#for i in range(game_map_section.shape[0]):
	for i in range(x_diff):
		
		#for j in range(game_map_section.shape[1]):
		for j in range(y_diff):
			if game_map_section[i,j] == 1 and shape[j,i]:

				return True

	return False



	# if all are zeroes, then an intersection did not occur so when np.all(intersect == 0) returns false then we must return true and vice versa.

	#return not np.all(intersect == 0)


def place_block(shape, x_coord, y_coord, game_map):
	##print("Placed block!")
	shape_shape = shape.shape
	x_diff = shape_shape[1]
	y_diff = shape_shape[0]

	#thing = shape.astype("bool")

	##print("Placed block at y coord: "+str(y_coord))
	##print("Placed block at x coord: "+str(x_coord))

	##print("x_diff: "+str(x_diff))
	##print("y_diff: "+str(y_diff))

	#game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff] |= thing.T

	game_map[x_coord:x_coord+x_diff,y_coord:y_coord+y_diff] |= shape.T

	#game_map[y_coord:y_coord+y_diff,x_coord:x_coord+x_diff] = thing.T
	return game_map


# update_col_heights(shape, x_coord,y_coord)

def update_col_heights(shape_num, x_coord, y_coord):

	# This updates the column heights so we do not need to check them later.
	# block_col_heights
	#print("x_coord: "+str(x_coord))
	#print("shape_num: "+str(shape_num))

	#print("shapes[shape_num]: "+str(shapes[shape_num]))
	#print("shapes[shape_num].shape[1]+x_coord: "+str(shapes[shape_num].shape[1]+x_coord))
	#print("shapes[shape_num].shape[1] == "+str(shapes[shape_num].shape[1]))
	for i in range(x_coord, shapes[shape_num].shape[1]+x_coord):
		# Get the blocks height at that column.
		
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
		###print("Game map:"+str(shitoof))
	##print("Returned height: "+str(h))
	return h




def main_loop(game_map,moves):

	n = 0

	loop_counter = 0
	tower_height = 0

	rendering = False
	render_oof = True
	
	loop_found = False

	#print_count = 1000

	while n < MAX_BLOCK_COUNT:
		#if n % print_count == 0:
			#print(n)
		#print(n)
		##print("tower_height == "+str(tower_height))
		x_coord = 2
		x_coord_prev = 2
		skipcount = 3
		##print("n == "+str(n))
		cur_height = heights[n % AMOUNT_SHAPES]

		y_coord = tower_height + 3# + heights[n % AMOUNT_SHAPES]

		#shape = shapes[n % AMOUNT_SHAPES] # get the shape for this block placement.
		#shape = copy.deepcopy(shapes[n % AMOUNT_SHAPES]) # get the shape for this block placement.

		shape = shapes[n % AMOUNT_SHAPES]

		##print("loop_counter == "+str(loop_counter))
		##print("moves: "+str(moves))
		if n == 8:
			rendering = True
			##print("poopoo")
			#render_oof = True
			#render_mat(game_map)
		else:
			if rendering:
				rendering = False


		while True:
			if loop_counter == len(moves):
				loop_counter = 0
			# This is a loop to place the blocks.
			##print("x_coord at the start of the loop: "+str(x_coord))
			##print("y_coord: "+str(y_coord))
			# Get move
			##print("loop_countergregrege == "+str(loop_counter))
			cur_move = moves[loop_counter]

			# Apply move.
			##print("cur_move == "+str(cur_move))
			dx = dx_for_moves[cur_move]
			##print("dx: "+str(dx))
			x_coord += dx
			blocked = False
			if x_coord < 0:
				#x_coord = 0
				x_coord -= dx
				blocked = True
				#loop_counter -= 1
			##print("shit")
			##print("x_coord: "+str(x_coord))
			##print("shape_widths[n % AMOUNT_SHAPES] == "+str(shape_widths[loop_counter % AMOUNT_SHAPES]))

			##print("n % AMOUNT_SHAPES == "+str(n % AMOUNT_SHAPES))
			##print("MAP_WIDTH == "+str(MAP_WIDTH))
			
			if x_coord + shape_widths[n % AMOUNT_SHAPES] > MAP_WIDTH:
				#x_coord = MAP_WIDTH-1
				##print("Move blocked.")
				#loop_counter -= 1
				if not blocked:

					x_coord -= dx
					blocked = True

			
			# check collision against already placed blocks.

			if check_col(shape, x_coord, y_coord, game_map):


				if not blocked:

					x_coord -= dx
					blocked = True
				#x_coord -= dx # go back.
				#loop_counter -= 1
				#blocked = True

			# fall
			
			#if rendering and render_oof:
			#	poopooshit = copy.deepcopy(game_map)
			#	poopooshit = place_block(shape, x_coord, y_coord, poopooshit)
			#	render_mat(poopooshit)
				##print("Rendering")
				#render_oof = False


			#if cur_move == "<":
			#	assert x_coord <= x_coord_prev

			#if cur_move == ">":
			#	assert x_coord >= x_coord_prev

			x_coord_prev = x_coord

			y_coord -= 1
			##print("y_coord after decrement: "+str(y_coord))
			# check collision

			# dx = dx_for_moves[cur_move]

			# check collision against floor:
			loop_counter = (loop_counter + 1) % len(moves)

			if y_coord == -1:

				y_coord += 1

				# Place block
				#if not blocked:
				#	x_coord -= dx
				#game_map = place_block(shape, x_coord, y_coord, game_map)
				place_block(shape, x_coord, y_coord, game_map)
				#update_col_heights(shape, x_coord,y_coord)

				# n % AMOUNT_SHAPES

				update_col_heights(n % AMOUNT_SHAPES, x_coord,y_coord)

				# increment placed block counter

				n += 1

				# update tower height
				##print("Y coord in checking:"+str(y_coord))
				if y_coord+cur_height > tower_height: # no need to check for ones in the shape matrix because the first line always contains atleast one "1" .
					tower_height = y_coord+cur_height

				# Start new block loop.

				break


			# check skipcount . skipcount tells the height to the top of the stack so we do not need to check the collision against the tower for skipcount steps.

			if skipcount > 0:
				skipcount -= 1
			elif check_col(shape, x_coord, y_coord, game_map):

				# Go back up one space.

				y_coord += 1

				# Place block
				#if not blocked:
				#	x_coord -= dx
				#game_map = place_block(shape, x_coord, y_coord, game_map)

				place_block(shape, x_coord, y_coord, game_map)

				update_col_heights(n % AMOUNT_SHAPES, x_coord,y_coord)
				# increment placed block counter

				n += 1

				# update tower height
				##print("Y coord in checking:"+str(y_coord))
				if y_coord+cur_height > tower_height: # no need to check for ones in the shape matrix because the first line always contains atleast one "1" .
					tower_height = y_coord+cur_height

				# Start new block loop.

				break

		# Placed a block so now add a state to states 

		# Check for looped elements.

		#print("Saving state")

		if not loop_found:

			new_state = []

			# Get the height at each point.


			#print("Sorting shit.")
			lowest = 10000
			for i in range(MAP_WIDTH):

				# Now just go through all the shit.

				h = 0

				#for j in range(MAP_HEIGHT):
				#	if game_map[i][j] == 1:
				#		h = j

				#new_state.append(h)
				new_state.append(col_heights[i])
				if col_heights[i] < lowest:
					lowest = col_heights[i]

				'''
				if h != col_heights[i]:
					#print("h != col_heights[i]!!!!")
					#print("h: "+str(h))
					#print("col_heights[i] == "+str(col_heights[i]))
					assert False
					exit(1)
				'''


			#lowest = min(new_state)

			#print("Finished sorting shit.")

			state = [x - lowest for x in new_state] # The difference between shit.
			# n % AMOUNT_SHAPES
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



	render_mat(game_map)

	# sanity check

	#actual_height = check_height(game_map)

	##print("check_height output: "+str(actual_height))
	##print("tower_height: "+str(tower_height))
	#assert actual_height == tower_height
	if not loop_found:

		return tower_height
	else:

		return tower_height + (skipped * height_gain)



def parse_input():

	return sys.stdin.buffer.read().decode('ascii')


def solve_puzzle():

	moves = parse_input()

	game_map = np.zeros((MAP_WIDTH, MAP_HEIGHT),dtype=bool)       #.astype("bool")



	height = main_loop(game_map,moves)

	#result = get_height(game_map)

	return height






if __name__=="__main__":
	print("Solution to puzzle: "+str(solve_puzzle()))
	exit(0)
