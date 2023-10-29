
import sys
import copy
import time


PART = 1
DEBUG = True


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



def solve_puzzle() -> int:
	if PART==1:
		return solve_part_one()
	elif PART==2:
		return solve_part_two()
	else:
		fail("Invalid puzzle part number ("+str(PART)+") .")



if __name__=="__main__":

	print("Solution to puzzle: "+str(solve_puzzle()))
	print("Time spent in selected location: "+str(ooftime))

