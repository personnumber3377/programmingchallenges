
import sys
import numpy as np
from PIL import Image

def parse_input():
	stdin = sys.stdin.buffer.read().decode('ascii')
	lines = stdin.split("\n")
	# max_x, max_y, min_x, min_y
	coords = {}
	count = 0

	max_y = len(lines)
	max_x = len(lines[0])

	for y, line in enumerate(lines):
		for x, spot in enumerate(line):
			if spot == "#":

				coords[(x,y)] = count
				count += 1

	return coords, max_x, max_y, 0, 0



N = [0,-1]
S = [0,1]
W = [-1,0]
E = [1,0]
NW = [-1,-1]
NE = [1,-1]
SW = [-1,1]
SE = [1,1]



def generate_neighbours(place):

	offsets = [[1,0],[1,-1],[1,1],  # E , NE , SE
	[0,1],[0,-1], # N, S
	[-1,0],[-1,1],[-1,-1]] # W , SW, NW

	for off in offsets:
		yield [place[0]+off[0], place[1]+off[1]]

'''
def check_collision(place, move_offset, other_elves):

	offsets = [N,NE,NW,   S,SE,SW,   W,NW,SW,  E,NE,SE] # the rules
	count = 0
	
	while True:

		cur_offset = offsets[(move_offset+count)%12]

		if tuple([place[0]+cur_offset[0], place[1]+cur_offset[1]]) in other_elves:

			#print("Proposed move for position "+str(place)+" is "+str(((move_offset+count) % 12)//3))

			return ((move_offset+count) % 12)//3
		count += 1
'''


'''
def check_collision(place, move_offset, other_elves):

	offsets = [[N,NE,NW],   [S,SE,SW],   [W,NW,SW],  [E,NE,SE]] # the rules
	count = 0
	#print("Checking collision with place == "+str(place)+" move_offset== "+str(move_offset)+" other_elves == "+str(other_elves))
	for i, thing in enumerate(offsets):
		oof = True
		#print("Thing: "+str(thing))
		for offset in thing:
			##print("offset[0] == "+str(offset[0]))
			##print("offset[1] == "+str(offset[1]))
			#print("offset: "+str(offset))
			if tuple([place[0]+offset[0], place[1]+offset[1]]) in other_elves:
				oof = False
		if oof:

			#print("Proposed move for position "+str(place)+" is "+str(i))


			return i
	return None
	assert False
'''

'''
def check_collision(place, move_offset, other_elves):

	offsets = [[N,NE,NW],   [S,SE,SW],   [W,NW,SW],  [E,NE,SE]] # the rules
	count = 0
	#print("Checking collision with place == "+str(place)+" move_offset== "+str(move_offset)+" other_elves == "+str(other_elves))
	for i, thing in enumerate(offsets):
		oof = True
		#print("Thing: "+str(thing))
		for offset_count in range(len(thing)):
			#print("thing == "+str(thing))

			#print("(offset_count+move_offset) == "+str((offset_count+move_offset)))
			offset = thing[(offset_count+move_offset) % 3]
			##print("offset[0] == "+str(offset[0]))
			##print("offset[1] == "+str(offset[1]))
			#print("offset: "+str(offset))
			if tuple([place[0]+offset[0], place[1]+offset[1]]) in other_elves:
				oof = False
		if oof:

			#print("Proposed move for position "+str(place)+" is "+str(i))


			return i
	return None
	assert False
'''


def check_collision(place, move_offset, other_elves):

	offsets = [[N,NE,NW],   [S,SE,SW],   [W,NW,SW],  [E,NE,SE]] # the rules
	count = 0
	#print("Checking collision with place == "+str(place)+" move_offset== "+str(move_offset)+" other_elves == "+str(other_elves))
	for i in range(len(offsets)):
		oof = True

		thing = offsets[(i+move_offset) % 4]

		#print("Thing: "+str(thing))
		for offset_count in range(len(thing)):
			#print("thing == "+str(thing))

			#print("(offset_count+move_offset) == "+str((offset_count+move_offset)))
			offset = thing[offset_count]
			##print("offset[0] == "+str(offset[0]))
			##print("offset[1] == "+str(offset[1]))
			#print("offset: "+str(offset))
			if tuple([place[0]+offset[0], place[1]+offset[1]]) in other_elves:
				oof = False
		if oof:

			#print("Proposed move for position "+str(place)+" is "+str(i))


			#return i

			return (i+move_offset) % 4

	return None
	assert False



def check_moving(cur_place, other_elves):

	# Check if the elf can move (checks the eight directional) .
	#print("Called check_moving with cur_place "+str(cur_place))
	neighbours = list(generate_neighbours(cur_place))

	#print("Neighbours: "+str(list(neighbours)))

	count = 0

	for neig in neighbours:
		#print("Tuple of neighbour: "+str(tuple(neig)))
		if tuple(neig) in other_elves:
			return 1 # move

		count += 1
	return 0 # do not move


def get_new_place(place, cur_move):
	'''
	match cur_move:
		case 0:
			return [place[0]+N[0], place[1]+N[1]]
		case 1:
			return [place[0]+S[0], place[1]+S[1]]
		case 2:
			return [place[0]+W[0], place[1]+W[1]]
		case 3:
			return [place[0]+E[0], place[1]+E[1]]
		case _:
			#print("Invalid proposed move index: "+str(cur_move))
			exit(1)
	'''

	if cur_move == 0:

		return [place[0]+N[0], place[1]+N[1]]

	elif cur_move == 1:

		return [place[0]+S[0], place[1]+S[1]]

	elif cur_move == 2:

		return [place[0]+W[0], place[1]+W[1]]

	elif cur_move == 3:

		return [place[0]+E[0], place[1]+E[1]]

	else:
		#print("Invalid proposed move index: "+str(cur_move))
		exit(1)

def render_mat(mat):

	qr_matrix = np.invert(mat.astype(bool).T, dtype=bool)
	#print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()

def render_matrix(coords):
	#return

	min_x = min([k[0] for k in coords])
	min_y = min([k[1] for k in coords])

	max_x = max([k[0] for k in coords])
	max_y = max([k[1] for k in coords])

	print("max_y: "+str(max_y))
	print("max_x: "+str(max_x))

	print("min_y: "+str(min_y))
	print("min_x: "+str(min_x))

	print("coords == "+str(coords))

	x_shape = max_x-min_x
	y_shape = max_y-min_y

	matrix = np.zeros((x_shape+1, y_shape+1))
	#matrix = np.zeros((20, 20))
	for coord in coords:

		matrix[coord[0]-min_x,coord[1]-min_y] = 1

	render_mat(matrix)

	return



def main_loop(n, coords, max_x, max_y, min_x, min_y):

	rule_counter = 0

	# -1 for y is up and +1 for y is down. +1 for x is right and -1 for x is left

	dodge_rules = [[[0,-1],[-1,-1],[1,-1]],
	[[0,1],[-1,1],[1,1]],
	[[1,0],[1,-1],[1,1]],
	[[-1,0],[-1,-1],[-1,1]]]   # [[[dx1,dy1]]]  this is a list of lists and each of these lists has a list of offsets where to check   ..
	selected_num = -1
	move_count = 0
	for i in range(n):
		#print("Loop number: "+str(i))
		#print("Move count: "+str(move_count))
		# First half:

		# Check moving.

		moved_places = {}

		

		banlist = {}
		if i == selected_num:

			render_matrix(coords)

		for place in coords:
			#print("coords == "+str(coords))

			if check_moving(place, coords) == 0:
				# do not move
				#print("Place "+str(place)+" does not move.")
				continue

			# get the proposed move
			# def check_collision(place, move_offset, other_elves):
			#print("Checking collision:")

			#proposed_move = check_collision(place, move_count*3,coords)
			
			proposed_move = check_collision(place, move_count,coords)

			if proposed_move == None: # Can not move
				
				continue

			##print("Proposed move for position "+str(place)+" is "+str(proposed_move))
			cur_index = coords[place] # get index of current elf.
			#print("Get new place:")
			new_place = get_new_place(place, proposed_move)

			# add the index into the new dictionary. This dictionary will be used to check for blocked moves.

			if tuple(new_place) not in moved_places:


				moved_places[tuple(new_place)] = ([tuple((cur_index, place))])
			else:
				moved_places[tuple(new_place)].append(tuple((cur_index, place)))

				#banlist.append()
				for pair in moved_places[tuple(new_place)]:
					banlist[pair[0]] = 1


		# Stage two


		#print("==== 2 =====")
		#print("Moved places: "+str(moved_places))


		for new_place in moved_places:
			element = moved_places[new_place]



			for thing in element:

				#print("moved_places == "+str(moved_places))
				#print("element == "+str(element))
				old_place = thing[1]

				index = thing[0]

				# check for blocked move

				if index in banlist:
					continue

				# move
				assert isinstance(old_place, tuple)
				assert old_place in coords

				assert coords[old_place] == index
				#coords[old_place] = new_place # replace coordinates with the new coordinates


				# replace coordinates with the new coordinates

				coords.pop(old_place)

				coords[new_place] = index
		rule_counter += 3


		move_count += 1
	#print("Final coords: "+str(coords))
	render_matrix(coords)
	return coords


def calculate_area(coords):

	# Get the min x coord and min y coord

	min_x = min([k[0] for k in coords])
	min_y = min([k[1] for k in coords])

	max_x = max([k[0] for k in coords])
	max_y = max([k[1] for k in coords])
	
	print("min_x: "+str(min_x))
	print("min_y: "+str(min_y))
	print("max_x: "+str(max_x))
	print("max_y: "+str(max_y))
	area = 0

	for x in range(min_x, max_x+1):
		for y in range(min_y, max_y+1):
			if (x,y) not in coords:
				area += 1
	print("Assert check:")		
	assert area == ((max_x-min_x+1)*(max_y-min_y+1))-len(coords)
	print("passed")
	return area

def solve_puzzle():
	coordinates, max_x, max_y, min_x, min_y = parse_input()
	#print("coordinates == "+str(coordinates))

	# max_x, max_y, min_x, min_y

	final_coordinates = main_loop(10, coordinates,max_x, max_y, min_x, min_y)
	area = calculate_area(final_coordinates)
	return area


if __name__=="__main__":

	print("Solution to puzzle: "+str(solve_puzzle()))
