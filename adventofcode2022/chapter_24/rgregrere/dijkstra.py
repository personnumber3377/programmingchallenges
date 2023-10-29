
import sys
import copy
import time
import math

from heapq import heappush, heappop
#from matplotlib.pyplot import *
import matplotlib.pyplot as plt
SANITY_CHECKS = True # Slows down the program, but makes sure that the program works as intended

PART = 1
#DEBUG = True

DEBUG_DEFAULT = False

DEBUG = DEBUG_DEFAULT

print("Sys.argv: "+str(sys.argv))
if "--debug" in sys.argv and "--debug" != sys.argv[-1]:
	value = sys.argv[sys.argv.index("--debug")+1] # get value 
	if value == "False":
		DEBUG = False
	elif value == "True":
		DEBUG = True
	else:

		print("Value: "+str(value))
		value = bool(int(value))
		print("Value: "+str(value))
		if value:
			print("Setting debug to True.")
			DEBUG = True
		else:
			print("Setting debug to False.")
			DEBUG = False


EXAMPLE_ONE = False

#EXAMPLE_PATH = ["placeholder", [0,0], ] # This is the shortest path which the elf takes in the example. The point of this is to check that these positions appear in the steps taken.
#EXAMPLE_PATH = ["placeholder", [0, 0], [0, 1], [0, 2], [0, 2], [0, 1], [1, 1], [2, 1], [2, 2], [1, 2], [1, 1], [2, 1], [2, 1], [2, 2], [2, 3], [3, 3], [4, 3], [5, 3], [5, 4], [5, 5]]

#EXAMPLE_PATH = ["placeholder", [0, 0], [0, 1], [0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4]]
EXAMPLE_PATH = ["placeholder", [0, 0], [0, 1], [0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4]]
'''
UP_SYM = "^"
DOWN_SYM = "v"
LEFT_SYM = "<"
RIGHT_SYM = ">"
'''


#EXAMPLE_BLIZZARDS = [{(0, 1), (1, 3), (4, 0), (4, 3), (3, 1), (5, 3), (0, 3), (0, 2), (1, 0), (4, 1)}, {(1, 3), (1, 2), (4, 3), (1, 1), (2, 0), (5, 1), (4, 2), (4, 1), (5, 2)}, {(1, 2), (2, 1), (0, 0), (2, 0), (2, 3), (0, 2), (3, 3), (1, 0), (3, 2)}, {(0, 1), (4, 3), (3, 1), (1, 1), (4, 2), (0, 2), (1, 0), (3, 2), (1, 3)}, {(0, 1), (4, 0), (1, 2), (2, 1), (2, 0), (5, 1), (5, 0), (2, 2), (3, 2)}, {(2, 1), (0, 0), (3, 1), (0, 3), (5, 1), (3, 0), (0, 2), (5, 0), (5, 3), (3, 2), (5, 2)}, {(0, 1), (1, 2), (3, 1), (1, 1), (0, 3), (4, 2), (3, 0), (0, 2), (2, 2), (5, 3), (3, 2)}, {(4, 0), (2, 1), (3, 1), (2, 0), (5, 1), (2, 3), (3, 3), (1, 0), (5, 2)}, {(1, 3), (4, 0), (2, 1), (0, 0), (4, 3), (1, 1), (4, 2), (3, 0), (2, 3), (0, 2), (3, 3), (2, 2), (4, 1)}, {(0, 1), (4, 0), (1, 2), (2, 1), (2, 3), (0, 2), (3, 3), (3, 2), (4, 1)}, {(0, 1), (1, 3), (2, 1), (4, 3), (1, 1), (5, 1), (4, 2), (3, 0), (5, 0), (1, 0), (4, 1)}, {(4, 0), (4, 3), (5, 1), (0, 2), (1, 0), (1, 3), (4, 2), (3, 0), (3, 3), (5, 0), (5, 3), (1, 2), (3, 2), (4, 1), (5, 2), (0, 0), (1, 1), (0, 3), (2, 3)}, {(0, 1), (1, 3), (4, 0), (4, 3), (3, 1), (5, 3), (0, 3), (0, 2), (1, 0), (4, 1)}, {(1, 3), (1, 2), (4, 3), (1, 1), (2, 0), (5, 1), (4, 2), (4, 1), (5, 2)}, {(1, 2), (2, 1), (0, 0), (2, 0), (2, 3), (0, 2), (3, 3), (1, 0), (3, 2)}, {(0, 1), (4, 3), (3, 1), (1, 1), (4, 2), (0, 2), (1, 0), (3, 2), (1, 3)}, {(0, 1), (4, 0), (1, 2), (2, 1), (2, 0), (5, 1), (5, 0), (2, 2), (3, 2)}, {(2, 1), (0, 0), (3, 1), (0, 3), (5, 1), (3, 0), (0, 2), (5, 0), (5, 3), (3, 2), (5, 2)}]

EXPECTED_BLIZ_COUNT = None

EXAMPLE_BLIZZARDS = [{(4, 0), (4, 3), (5, 1), (0, 2), (1, 0), (1, 3), (4, 2), (3, 0), (3, 3), (5, 0), (5, 3), (1, 2), (3, 2), (4, 1), (5, 2), (0, 0), (1, 1), (0, 3), (2, 3)}, {(0, 1), (1, 3), (4, 0), (1, 2), (4, 3), (3, 1), (5, 3), (0, 3), (2, 0), (4, 2), (0, 2), (1, 0), (3, 2), (4, 1)}, {(1, 3), (1, 2), (2, 1), (4, 3), (3, 1), (1, 1), (2, 0), (5, 1), (4, 2), (3, 0), (2, 2), (1, 0), (4, 1), (5, 2)}, {(4, 0), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (3, 0), (2, 3), (0, 2), (3, 3), (2, 2), (1, 0), (3, 2), (4, 1)}, {(0, 1), (4, 0), (1, 2), (4, 3), (3, 1), (1, 1), (4, 2), (2, 3), (0, 2), (3, 3), (5, 0), (1, 0), (3, 2), (1, 3)}, {(0, 1), (4, 0), (1, 2), (2, 1), (0, 0), (4, 3), (2, 0), (5, 1), (4, 2), (5, 0), (2, 2), (3, 2), (1, 3), (5, 2)}, {(2, 1), (0, 0), (3, 1), (1, 1), (0, 3), (5, 3), (5, 1), (4, 2), (3, 0), (0, 2), (5, 0), (1, 0), (3, 2), (4, 1), (5, 2)}, {(0, 1), (4, 0), (1, 2), (3, 1), (1, 1), (0, 3), (2, 0), (5, 3), (4, 2), (3, 0), (0, 2), (2, 2), (1, 0), (3, 2), (4, 1)}, {(4, 0), (1, 2), (2, 1), (4, 3), (3, 1), (2, 0), (5, 1), (3, 0), (2, 3), (3, 3), (2, 2), (1, 0), (1, 3), (5, 2)}, {(1, 3), (4, 0), (1, 2), (2, 1), (0, 0), (4, 3), (1, 1), (2, 0), (4, 2), (3, 0), (2, 3), (0, 2), (3, 3), (2, 2), (3, 2), (4, 1)}, {(0, 1), (4, 0), (1, 2), (2, 1), (3, 1), (1, 1), (4, 2), (2, 3), (0, 2), (3, 3), (5, 0), (1, 0), (3, 2), (4, 1)}, {(0, 1), (1, 3), (4, 0), (2, 1), (0, 0), (4, 3), (1, 1), (5, 1), (4, 2), (3, 0), (5, 0), (2, 2), (1, 0), (4, 1), (5, 2)}, {(4, 0), (4, 3), (5, 1), (0, 2), (1, 0), (1, 3), (4, 2), (3, 0), (3, 3), (5, 0), (5, 3), (1, 2), (3, 2), (4, 1), (5, 2), (0, 0), (1, 1), (0, 3), (2, 3)}, {(0, 1), (1, 3), (4, 0), (1, 2), (4, 3), (3, 1), (5, 3), (0, 3), (2, 0), (4, 2), (0, 2), (1, 0), (3, 2), (4, 1)}, {(1, 3), (1, 2), (2, 1), (4, 3), (3, 1), (1, 1), (2, 0), (5, 1), (4, 2), (3, 0), (2, 2), (1, 0), (4, 1), (5, 2)}, {(4, 0), (1, 2), (2, 1), (0, 0), (1, 1), (2, 0), (3, 0), (2, 3), (0, 2), (3, 3), (2, 2), (1, 0), (3, 2), (4, 1)}, {(0, 1), (4, 0), (1, 2), (4, 3), (3, 1), (1, 1), (4, 2), (2, 3), (0, 2), (3, 3), (5, 0), (1, 0), (3, 2), (1, 3)}, {(0, 1), (4, 0), (1, 2), (2, 1), (0, 0), (4, 3), (2, 0), (5, 1), (4, 2), (5, 0), (2, 2), (3, 2), (1, 3), (5, 2)}, {(2, 1), (0, 0), (3, 1), (1, 1), (0, 3), (5, 3), (5, 1), (4, 2), (3, 0), (0, 2), (5, 0), (1, 0), (3, 2), (4, 1), (5, 2)}]

# {(1, 3), (1, 2), (4, 3), (1, 1), (2, 0), (5, 1), (4, 2), (4, 1), (5, 2)}, {(1, 2), (2, 1), (0, 0), (2, 0), (2, 3), (0, 2), (3, 3), (1, 0), (3, 2)}

USE_DIJKSTRA = True

UP_SYM = ord("^")
DOWN_SYM = ord("v")
LEFT_SYM = ord("<")
RIGHT_SYM = ord(">")


DIRS = {UP_SYM: 0, LEFT_SYM: 1, DOWN_SYM: 2, RIGHT_SYM: 3}

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

OFFSETS = {UP: [0,-1], LEFT: [-1,0], DOWN: [0,1], RIGHT:[1,0]}
#OFFSETS = [[0,-1], [-1,0], [0,1], [1,0]]



#OFFSETS = {UP: [0,-1], LEFT: [-1,0], DOWN: [0,1], RIGHT:[1,0]}


def fail(msg: str) -> None:
	print("[FAIL] "+str(msg))
	exit(1)

def debug(msg: str, start=True) -> None:
	if DEBUG:
		if start:

			print("[DEBUG] "+str(msg))
		else:
			print(str(msg))
	return






def parse_1():

	debug("Parsing input.")

	raw_in = sys.stdin.buffer.read()

	lines = raw_in.split(b"\n")

	debug("Lines: "+str(lines))
	width = len(lines[0]) - 2 # - 2 because first and last are walls.

	height = len(lines) - 2

	#blizzards = []  # a list of lists. first element in sublist is the coordinates as a tuple and the second element is the direction

	blizzards = {} # change of plan. Implement blizzards as a dictionary with the coordinates as key and the move direction as val.


	for y, line in enumerate(lines[1:-1]): # skip first and last lines

		debug("Line: "+str(line))

		for x, spot in enumerate(line[1:-1]): # skip first and last spot which are walls.

			debug("Spot: "+str(spot))

			if spot in DIRS:
				debug("Spot: "+str(spot))
				result = [[x,y],DIRS[spot]]

				blizzards[tuple((x,y))] = [[DIRS[spot],0]] # first the direction and then the counter.

	return width, height, blizzards





def parse_input():
	if PART == 1:
		return parse_1()


'''
#def update_blizzards(blizzards: dict, width: int, height: int, counter: int) -> list:
def update_blizzards(blizzards: dict, counter: int, width: int, height: int) -> list:
	# update blizzards according to the rules.

	#for coords in blizzards: # I hope there is a more pythonic way to modify each element in a list. if you try to do for bliz in blizzards: ... then you are not actually modifying the original list, but copies of the objects or something like that.
	#debug("counter: "+str(counter))
	#debug("width: "+str(width))
	#debug("height: "+str(height))

	# NOTE: If we tried the above, then we would get a "RuntimeError: dictionary changed size during iteration" error.

	OFFSETS = {UP: [0,-1], LEFT: [-1,0], DOWN: [0,1], RIGHT:[1,0]}
	#OFFSETS = [[0,-1], [-1,0], [0,1], [1,0]]


	#for coords in tuple(blizzards.keys()):
	#for coords in blizzards:

	for coords in tuple(blizzards.keys()):

		#move = blizzards[i][1]

		
		#move = blizzards[coords]
		moves = blizzards[coords]
		pop_list = []
		#new_list = copy.deepcopy(moves)
		#new_list = moves

		# Can not do this because we can have multiple blizzards at the same spot.

		# <comment>
		

		# </comment>

		#new_stuff = []

		for ind, move in enumerate(moves):
			actual_move = move[0]

			count = move[1]

			if count != counter:


				offset = OFFSETS[actual_move]

				#new_coords = (coords[0]+offset[0], coords[1]+offset[1])
				new_coords = [coords[0]+offset[0], coords[1]+offset[1]]
				# check for loop around.

				if new_coords[0] < 0:
					
					assert new_coords[0] == -1
					new_coords[0] = width - 1 # going left so spawn on the right

				elif new_coords[0] == width:
					
					new_coords[0] = 0 # loop around going to the right and spawn on the left
				
				elif new_coords[1] < 0:
					
					assert new_coords[1] == -1
					new_coords[1] = height - 1
				
				elif new_coords[1] == height:

					new_coords[1] = 0

				new_coords = tuple(new_coords)

				if new_coords not in blizzards:
					blizzards[new_coords] = [[actual_move, counter]]
				else:
					blizzards[new_coords] += [[actual_move, counter]]



				#new_stuff.append([new_coords, actual_move])

				#blizzards[coords].pop(ind) # delete it from the list # another note: we can not do this because it messes up the loop i think
				pop_list.append(ind)
				#blizzards[coords].remove(move)
				#new_list.remove(move)
		offset = 0
		for pop_ind in pop_list:

			blizzards[coords].pop(pop_ind - offset)

			offset += 1
		
		# check if there are any blizzards left at that spot:

		if len(blizzards[coords]) == 0:

			del blizzards[coords]

	return blizzards
'''

ooftime = 0

#def update_blizzards(blizzards: dict, width: int, height: int, counter: int) -> list:
def update_blizzards(blizzards: dict, counter: int, width: int, height: int) -> list:
	# update blizzards according to the rules.
	global ooftime
	OFFSETS = {UP: [0,-1], LEFT: [-1,0], DOWN: [0,1], RIGHT:[1,0]}

	for coords in tuple(blizzards.keys()):

		moves = blizzards[coords]
		pop_list = []

		for ind, move in enumerate(moves):
			actual_move = move[0]

			count = move[1]
			if count != counter:

				offset = OFFSETS[actual_move]
				new_coords = [coords[0]+offset[0], coords[1]+offset[1]]

				if new_coords[0] < 0:
					
					assert new_coords[0] == -1
					new_coords[0] = width - 1 # going left so spawn on the right
				elif new_coords[0] == width:
					new_coords[0] = 0 # loop around going to the right and spawn on the left
				elif new_coords[1] < 0:
					assert new_coords[1] == -1
					new_coords[1] = height - 1
				elif new_coords[1] == height:
					new_coords[1] = 0
				new_coords = tuple(new_coords)
				if new_coords not in blizzards:
					blizzards[new_coords] = [[actual_move, counter]]
				else:
					blizzards[new_coords] += [[actual_move, counter]]

				pop_list.append(ind)

		offset = 0
		start = time.time()
		for pop_ind in pop_list:
			blizzards[coords].pop(pop_ind - offset)
			offset += 1
		end = time.time()

		ooftime += (end - start)

		if len(blizzards[coords]) == 0:
			del blizzards[coords]
	debug("Returning this from update_blizzards: "+str(blizzards))
	return blizzards

def generate_new_positions(prev_pos: set) -> set:

	# Generates all of the possible positions based on the previous possible positions.

	#new_pos = []

	new_pos = set()

	for pos in prev_pos:
		'''
		new_pos.append((pos[0],pos[1])) # stay in place
		new_pos.append((pos[0],pos[1]+1)) # up
		new_pos.append((pos[0],pos[1]-1)) # down
		new_pos.append((pos[0]-1,pos[1])) # left
		new_pos.append((pos[0]+1,pos[1])) # right
		'''
		#print("pos == "+str(pos))
		new_pos.add((pos[0],pos[1])) # stay in place
		new_pos.add((pos[0],pos[1]+1)) # up
		new_pos.add((pos[0],pos[1]-1)) # down
		new_pos.add((pos[0]-1,pos[1])) # left
		new_pos.add((pos[0]+1,pos[1])) # right


	# Delete the previous position list to improve memory performance

	del prev_pos

	return new_pos

# This is used for the dijkstra's algorithm

def generate_neighbours(pos: tuple) -> list:

	# Generates all of the possible positions based on the previous possible positions.

	#new_pos = []

	#new_pos = set()
	neighbours = []
	#for pos in prev_pos:

	'''
	new_pos.append((pos[0],pos[1])) # stay in place
	new_pos.append((pos[0],pos[1]+1)) # up
	new_pos.append((pos[0],pos[1]-1)) # down
	new_pos.append((pos[0]-1,pos[1])) # left
	new_pos.append((pos[0]+1,pos[1])) # right
	'''
	#print("pos == "+str(pos))
	neighbours.append((pos[0],pos[1])) # stay in place
	neighbours.append((pos[0],pos[1]+1)) # up
	neighbours.append((pos[0],pos[1]-1)) # down
	neighbours.append((pos[0]-1,pos[1])) # left
	neighbours.append((pos[0]+1,pos[1])) # right


	# Delete the previous position list to improve memory performance

	#del prev_pos

	return neighbours

import numpy as np
from PIL import Image



def render_mat(mat, step=None):

	qr_matrix = np.invert(mat.astype(bool), dtype=bool).T
	print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show(title="Current step: "+str(step))

def render_stuff(things, size, step=None):
	return

	matrix = np.zeros((size,size))

	for thing in things:

		matrix[thing[0],thing[1]] = 1

	render_mat(matrix, step)

	return


# all_possible_positions = cut_blizzards(all_possible_positions, blizzards)

def cut_blizzards(positions: list, blizzards: list) -> list:

	#assert isinstance(positions, list)
	debug("Type of \"positions\" == "+str(type(positions)))

	#for pos in list(positions):
	for pos in list(positions):
		if pos in blizzards:
			positions.remove(pos)
	return positions



def bounds_check(positions: list, width: int, height: int) -> list:



	for pos in list(positions):
		
		if pos == tuple((0,-1)):
			continue

		if pos[0] < 0:
			positions.remove(pos)
		elif pos[0] > width - 1:
			positions.remove(pos)
		elif pos[1] < 0:
			positions.remove(pos)
		elif pos[1] > height - 1:
			positions.remove(pos)

	return positions


def bounds_check_lst(positions: list, width: int, height: int) -> list:



	for pos in list(positions):
		
		if pos == tuple((0,-1)):
			continue

		if pos[0] < 0:
			positions.remove(pos)
		elif pos[0] > width - 1:
			positions.remove(pos)
		elif pos[1] < 0:
			positions.remove(pos)
		elif pos[1] > height - 1:
			positions.remove(pos)

	return positions

def check_bliz(correct_blizzards, blizzards):

	f = False
	debug("="*30)
	debug("Correct blizzards: "+str(correct_blizzards))
	debug("Our blizzards: "+str(blizzards))
	for bliz in blizzards:
		if bliz not in correct_blizzards:

			f = True

			debug("Blizzard "+str(bliz)+" is in blizzards, but should not be!")

	for bliz in correct_blizzards:
		if bliz not in blizzards:
			debug("Blizzard "+str(bliz)+" not in blizzards, when it should be!")

	if f:
		debug("="*30)
		fail("Blizzard check failed!")



	debug("="*30)
	debug("Blizzard check passed!")

	return



def check_bliz_num(blizzards, bliz_num=EXPECTED_BLIZ_COUNT):
	count = 0
	
	for bliz in blizzards:
		count += len(blizzards[bliz])

	if count != bliz_num:
		fail("Expected amount of blizzards not found in dictionary!")

	return

def get_bliz_num(blizzards):
	count = 0
	
	for bliz in blizzards:
		count += len(blizzards[bliz])
	return count





def render_bliz(blizzards, width_orig, height_orig):

	# add two because the width and height are width and height of the inner area not including walls
	if not DEBUG:
		return
	width = width_orig + 2

	height = height_orig + 2



	start = "#."+"#" * (width - 2)
	#start[1] = "."

	
	end = "#" * (width - 2) + ".#"

	#end[-2] = "."

	debug("="*50+"\n\n", start=False)

	debug(start, start=False)


	for y in range(height_orig):
		
		new_str = list("."*width_orig)

		for x in range(width_orig):
			pos_tup = tuple((x,y))
			if pos_tup in blizzards:

				if len(blizzards[pos_tup]) > 1:
					
					assert len(blizzards[pos_tup]) < 10

					new_str[x] = str(len(blizzards[pos_tup]))

				else:

					# print direction
					# DIRS = {UP_SYM: 0, LEFT_SYM: 1, DOWN_SYM: 2, RIGHT_SYM: 3}
					#debug("blizzards in render_bliz: "+str(blizzards))
					#debug("pos_tup == "+str(pos_tup))
					direction = blizzards[pos_tup][0][0] # the first element is the direction

					if direction == 0:
						new_str[x] = "^"
					elif direction == 1:
						new_str[x] = "<"
					elif direction == 2:
						new_str[x] = "v"
					elif direction == 3:
						new_str[x] = ">"
					else:
						fail("Invalid direction number: "+str(direction))

		# print line
		debug("#"+"".join(new_str)+"#", start=False)




	debug(end, start=False)

	debug("\n\n"+"="*50, start=False)

	return






def solve_part_one() -> int:

	# init vars




	n = 0
	
	blizzards = {}

	width, height, blizzards = parse_input()

	num_of_blizzards = get_bliz_num(blizzards)
	print("Original amount of blizzards: "+str(num_of_blizzards))

	# Skip forward until very first tile is available in the top left.
	debug("Blizzards: "+str(blizzards)+" .")
	#debug("Showing blizzards.")

	#render_stuff(blizzards, 10)

	debug("Rendering stuff initial:")
	render_bliz(blizzards,width,height)


	print("Skipping:")
	debug("Skipping forward:")
	while True:

		if (0,0) not in blizzards:
			break
		n += 1
		update_blizzards(blizzards, n, width, height)

	debug("Skipped "+str(n)+" steps!")

	# Now that the very first space is empty, we can actually start.

	#all_possible_positions = [(0,0)]
	all_possible_positions = set({tuple((0,0))})

	end = tuple((width-1, height-1))

	
	# Solve path
	selected_n = 16

	while True: # continue until end has been reached.
		#print("Start of loop.")
		#return
		#debug("n == "+str(n))
		# First generate all the possible positions from the all of the previous possible positions. (Aka the number of previous positions multiplied by 5).

		all_possible_positions = generate_new_positions(all_possible_positions)

		debug("All possible steps before blizzards: "+str(all_possible_positions))

		# Check for done
		#debug("")
		if end in all_possible_positions:
			break

		# Update blizzards
		
		blizzards = update_blizzards(blizzards, n, width, height)
		if n == selected_n:

			render_stuff(blizzards, 300, n)
		# Cut out unwanted positions

		# First take out positions which are now in blizzards
		all_possible_positions = bounds_check(all_possible_positions, width, height)
		debug("All possible positions after bounds: "+str(all_possible_positions))


		all_possible_positions = cut_blizzards(all_possible_positions, blizzards)
		debug("After blizzards: "+str(all_possible_positions))
		#debug("Blizzards: "+str(blizzards))
		# Take out positions which are out of bounds.

		debug("Rendering stuff:")
		render_bliz(blizzards,width,height)

		debug("tuple((0,0)) not in blizzards == "+str(tuple((0,0)) not in blizzards))

		if all_possible_positions == set():
			fail("No path available!")


		debug("Testing blizzard count:")
		check_bliz_num(blizzards, num_of_blizzards)

		#print("New amount of blizzards: "+str(get_bliz_num(blizzards)))
		# Check example path.



		if EXAMPLE_ONE:


			debug("Testing blizzards")


			correct_blizzards = EXAMPLE_BLIZZARDS[n]

			check_bliz(correct_blizzards, blizzards)


			debug("poopoo")
			if n >= len(EXAMPLE_PATH) - 1:
				continue
			correct_move = EXAMPLE_PATH[n]
			debug("Correct thing: "+str(correct_move))
			if tuple(correct_move) not in all_possible_positions:
				debug("Correct move: "+str(correct_move))
				print("All possible positions: "+str(all_possible_positions))
				fail("OOF!")
			debug("Passed move test!")
		n += 1
		#print("n: "+str(n))
		#if n % 100 == 0:
		#	print("n == "+str(n))

		if n == 1000:
			debug("Timed out!")
			break
	return n + 1 # +1 because we need to account for the final step.

def solve_part_two() -> int:
	# placeholder
	return 0



'''

# This next function is basically just a reimplementation of this:  https://github.com/wleftwich/aoc/blob/main/2022/24-blizzard-basin.ipynb

def dijkstra(data, start=(0, 0), finish=None, initial_state=0):
    states = blizzard_list(data)
    if finish is None:
        h, w = states[0].shape
        finish = (h-1, w-1)
    visited = {(start, initial_state): 0}
    pq = []
    heappush(pq, (0, start, initial_state))
    while pq:
        (d, p, s) = heappop(pq)
        if p == finish:
            return d
        next_s = (s + 1) % len(states)
        next_d = d + 1
        for spot in open_spots(p, states[next_s]):
            v = visited.get((spot, next_s))
            if v is None or v > next_d:
                visited[(spot, next_s)] = next_d
                heappush(pq, (next_d, spot, next_s))


'''




def get_all_pos_bliz_states(init_bliz, width, height):

	# the amount of all possible states is lcm(width, height)

	# count = lcm(width, height)
	count = math.lcm(height, width)
	#blizzards = [init_bliz]

	all_blizzards = []

	orig_bliz_count = get_bliz_num(init_bliz)

	for i in range(count):



		#all_blizzards.append((init_bliz).copy())

		all_blizzards.append(copy.deepcopy(init_bliz))

		#debug("Init bliz: "+str(init_bliz))
		#debug("Rendering now: ")
		render_bliz(init_bliz, width, height)
		init_bliz = update_blizzards(init_bliz, i+1, width, height)
		check_bliz_num(init_bliz, bliz_num=orig_bliz_count)
	#assert all_blizzards[0] != all_blizzards[1]

	assert len(all_blizzards) == count
	debug("Returning this from get_all_pos_bliz_states: "+str(all_blizzards))
	return all_blizzards



#all_blizzards.append(copy.deepcopy(init_bliz))

def generate_possible_positions(position, blizzards, width, height):
	# first generate neighbours:

	neighbours = generate_neighbours(position)

	# collision check

	neighbours = bounds_check_lst(neighbours, width, height)

	# check blizzards

	# all_possible_positions = cut_blizzards(all_possible_positions, blizzards)

	neighbours = cut_blizzards(neighbours, blizzards)

	# sanity check:
	debug("neighbours: "+str(neighbours))
	assert len(neighbours) <= 5 # 5 because there is also the option of staying in place


	for neig in neighbours:
		assert neig[0] >= 0
		assert neig[1] >= -1

	for neig in neighbours:
		assert neig not in blizzards

	return neighbours


#fig = plt.figure()
#ax = fig.add_subplot(cmap='gray', vmin=0, vmax=255)

#hl, = plt.plot()


IMAGE_SIZE = 500
import numpy as np
import matplotlib.pyplot as plt


plt.ion()

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

# In order to solve this, one needs to set the color scale with vmin/vman
# I found this, thanks to @jettero's comment.
#array = np.zeros(shape=(IMAGE_SIZE, IMAGE_SIZE), dtype=np.uint8)
#axim2 = ax2.imshow(array, vmin=0, vmax=255)
import time as timelib

def show_visited(visited, width, height, max_step, last_pos=tuple((0,0))):

	# Shows the visited nodes. Darker means more time and lighter means less time.
	print("Called show_visited.")
	matrix = np.zeros((width,height,3))

	for thing in visited:

		pos = thing[0]
		time = thing[1]

		#matrix[pos[0],pos[1],0] = round(( time / max_step ) * 255)
		#matrix[pos[0],pos[1],1] = round(( time / max_step ) * 255)
		#matrix[pos[0],pos[1],2] = round(( time / max_step ) * 255)
		assert time / max_step <= 1.0 and time / max_step >= 0
		matrix[pos[0],pos[1],0] = ( time / max_step )
		matrix[pos[0],pos[1],1] = ( time / max_step )
		matrix[pos[0],pos[1],2] = ( time / max_step )

	#render_mat(matrix)
	print("Showing matrix")
	#thing = ax2.imshow(matrix, cmap='gray', vmin=0, vmax=255)

	red_intensity = 1.0

	matrix[last_pos[0],last_pos[1],0] = red_intensity # mark as red
	matrix[last_pos[0],last_pos[1],1] = 0.0
	matrix[last_pos[0],last_pos[1],2] = 0.0


	if last_pos[0] != width - 1:
		matrix[last_pos[0]+1,last_pos[1],0] = red_intensity
		matrix[last_pos[0]+1,last_pos[1],1] = 0.0
		matrix[last_pos[0]+1,last_pos[1],2] = 0.0

	if last_pos[1] != height - 1:
		matrix[last_pos[0],last_pos[1]+1,0] = red_intensity
		matrix[last_pos[0],last_pos[1]+1,1] = 0.0
		matrix[last_pos[0],last_pos[1]+1,2] = 0.0
	
	if last_pos[0] != width - 1 and last_pos[1] != height - 1:
		matrix[last_pos[0]+1,last_pos[1]+1,0] = red_intensity
		matrix[last_pos[0]+1,last_pos[1]+1,1] = 0.0
		matrix[last_pos[0]+1,last_pos[1]+1,2] = 0.0

	#thing = ax2.imshow(matrix, cmap='RGB', vmin=0, vmax=255)
	thing = ax2.imshow(matrix, vmin=0, vmax=255)
	#ax.set_data(matrix)
	#hl.set_data(matrix)
	#hl.draw()
	thing.set_data(matrix)
	plt.draw()
	fig2.canvas.flush_events()
	#plt.show()
	print("Done!")
	#timelib.sleep(0.1)

	return


#global thingtime

thingtime = 0
starttime = 0
endtottime = 0
def solve_part_one_dijkstra():
	global thingtime
	# First parse the blizzards
	global starttime
	global endtottime

	width, height, blizzards = parse_input()
	starttime = time.time()
	# create all possible states for blizzards:
	print("Getting all possible blizzards...")
	pos_bliz_states = get_all_pos_bliz_states(blizzards, width, height)
	print("Done!")
	end = tuple((width-1, height-1))

	start = tuple((0,-1))

	visited = {(start, 0): 0}

	queue = []

	step_count = 0

	state_counter = 0

	heappush(queue, (step_count, start, state_counter))
	n = 0

	timeout_count = 4000

	print_count = 1000
	max_step = 0
	while queue:

		if n % print_count == 0:
			#print("Length of the heap thing : "+str(len(queue)))
			print("n == "+str(n))
		#debug("n == "+str(n))
		#print("n == "+str(n))
		#if n == timeout_count:
		#	break

		(step_count, pos, state_counter) = heappop(queue)
		#debug("(step_count, pos, state_counter) == "+str(tuple((step_count, pos, state_counter))))
		if pos == end:
			return step_count + 1

		# increment state

		#debug("len(pos_bliz_states) == "+str(len(pos_bliz_states)))

		new_state = (state_counter + 1) % len(pos_bliz_states)

		new_step_counter = step_count + 1

		if new_step_counter > max_step:
			max_step = new_step_counter
		# generate_neighbours

		#print("Deepcopy stage: ")
		#pos_bliz_states_before = copy.deepcopy(pos_bliz_states)
		#debug("Possible bliz states before: "+str(pos_bliz_states_before))

		#print("generate_possible_positions stage: ")
		#start = time.time()
		neighbours = generate_possible_positions(pos, pos_bliz_states[new_state], width, height)
		#end = time.time()


		assert len(neighbours) <= 5

		
		start = time.time()
		for neig in neighbours:
			#assert pos_bliz_states_before == pos_bliz_states
			#debug("New state: "+str(new_state))

			#debug("pos_bliz_states[new_state] == "+str(pos_bliz_states[new_state]))

			#render_bliz(pos_bliz_states[new_state], width, height)

			
			v = visited.get((neig, new_state))



			if v is None or v > new_step_counter:
				visited[(neig, new_state)] = new_step_counter
				#show_visited(visited, width, height, max_step, last_pos=neig)
				heappush(queue, (new_step_counter, neig, new_state))

		end = time.time()
		thingtime += (end - start)
		
		#print("Queue length: "+str(len(queue)))

		#if len(queue) > 100:
		#	print("Length of queue[100] == "+str(len(queue[100])))
		#	#print("Length of queue[100][1] == "+str(len(queue[100][1])))

		

		n += 1


	#fail("No path found with dijkstra's algorithm!")
	debug("No path found!")

	endtottime = time.time()

	print("Total loop time: "+str(endtottime - starttime))

	return n


def solve_puzzle() -> int:
	if PART==1:
		if USE_DIJKSTRA:
			return solve_part_one_dijkstra()
		else:
			return solve_part_one()
	elif PART==2:
		return solve_part_two()
	else:
		fail("Invalid puzzle part number ("+str(PART)+") .")



if __name__=="__main__":
	#global thingtime
	print("Solution to puzzle: "+str(solve_puzzle()))
	print("Time spent in selected location: "+str(thingtime))

