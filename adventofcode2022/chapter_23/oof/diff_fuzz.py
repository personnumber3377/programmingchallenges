
import numpy as np
from PIL import Image
import random





N = [0,-1]
S = [0,1]
W = [-1,0]
E = [1,0]
NW = [-1,-1]
NE = [1,-1]
SW = [-1,1]
SE = [1,1]

'''
def check_collision1(place, move_offset, other_elves):

	offsets = [[N,NE,NW],   [S,SE,SW],   [W,NW,SW],  [E,NE,SE]] # the rules
	count = 0
	#print("Checking collision with place == "+str(place)+" move_offset== "+str(move_offset)+" other_elves == "+str(other_elves))
	for i, thing in enumerate(offsets):
		oof = True
		#print("Thing: "+str(thing))
		for offset_count in range(len(thing)):
			#print("thing == "+str(thing))

			#print("(offset_count+move_offset) == "+str((offset_count+move_offset)))
			print("move_offset inside one : "+str(move_offset))
			offset = thing[(offset_count+move_offset) % 3]
			##print("offset[0] == "+str(offset[0]))
			##print("offset[1] == "+str(offset[1]))
			#print("offset: "+str(offset))
			if tuple([place[0]+offset[0], place[1]+offset[1]]) in other_elves:
				oof = False
		if oof:

			#print("Proposed move for position "+str(place)+" is "+str(i))


			return i
			#return (i+move_offset) % 4
	return None
	assert False



'''

def check_collision1(place, move_offset, other_elves):

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

'''


def check_collision2(place, move_offset, other_elves):

	#offsets = [[[0,-1],[1,-1],[-1,-1]],   [[0,1],[1,1],[-1,1]],   [[-1,0],[-1,-1],[-1,1]],  [[1,0],[1,-1],[1,1]]] # the rules
	
	offsets = [[0,-1],[1,-1],[-1,-1],   [0,1],[1,1],[-1,1],   [-1,0],[-1,-1],[-1,1],  [1,0],[1,-1],[1,1]]
	oof = True
	for i in range(len(offsets)):
		print("i == "+str(i))

		thing = offsets[(i+move_offset) % 12]

		if tuple([place[0]+thing[0],place[1]+thing[1]]) in other_elves:
			print("Collision with "+str(tuple([place[0]+thing[0],place[1]+thing[1]])))
			oof = False

		if ((i+1) % 3) == 0:
			if oof and i != 0:
				print("i == "+str(i))
				print("Proposed move for place "+str(place)+" is "+str(((i+move_offset) % 12)//3))
				return ((i+move_offset) % 12)//3
			oof = True
	

	return None
'''



def check_collision2(place, move_offset, other_elves):
	offsets = [N,NE,NW,   S,SE,SW,   W,NW,SW,  E,NE,SE]
	for _ in range(move_offset):
		thing = offsets.pop(0)
		offsets.append(thing)
	#print("offsets == "+str(offsets))
	i = 0
	while i != 12:
		index = i
		thing = offsets[index]
		#print("indexpoopoo == "+str(index))
		if tuple([place[0]+thing[0],place[1]+thing[1]]) in other_elves:
			#print("tuple([place[0]+thing[0],place[1]+thing[1]]) == "+str(tuple([place[0]+thing[0],place[1]+thing[1]])))
			i = ((i//3)+1)*3
			if i == 12:
				break
			index = i
			#print("index == "+str(index))
			thing = offsets[index]
			
			continue
		if ((i+1) % 3) == 0:
			#print("final index == "+str(index))
			#print("move_offset == "+str(move_offset))
			#print("returning this: "+str(((index+move_offset) % 12)//3))
			return ((index+move_offset) % 12)//3
			#print("i == "+str(i))
			#print()
			#return ((i) % 12)//3
		i += 1
	return None

def render_mat(mat):

	qr_matrix = np.invert(mat.astype(bool).T, dtype=bool)
	#print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()

def render_matrix(coords,width,height):
	#return

	#min_x = min([k[0] for k in coords])
	#min_y = min([k[1] for k in coords])

	#max_x = max([k[0] for k in coords])
	#max_y = max([k[1] for k in coords])

	max_x = width
	max_y = height

	min_x = 0
	min_y = 0

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

def generate_elves(width,height,chance):

	out_list = {}
	
	count = 0

	for x in range(width+1):
		for y in range(height+1):

			if random.random() < chance:

				out_list[tuple((x,y))] = count

				count += 1

	return out_list

if __name__=="__main__":


	width = 4000

	height = 4000

	random_input = generate_elves(width,height,0.3)

	random_place = tuple((random.randrange(0,width), random.randrange(0,height)))

	# place, move_offset, other_elves

	move_count = 0


	for place in random_input:
		if move_count//3 % 10000 == 0:
			print(move_count//3)
		proposed_move1 = check_collision1(place, move_count//3,random_input)
		proposed_move2 = check_collision2(place, move_count,random_input)


		if proposed_move2 != proposed_move1:
			print("Differing outputs for place == "+str(place)+", move_count == "+str(move_count)+", random_input == "+str(random_input)+" .")
			print("Old output: "+str(proposed_move1))
			print("New output: "+str(proposed_move2))
			print("Move offset: "+str(move_count))
			print("Rendering matrix: ")

			render_matrix(random_input, width, height)

			exit(1)
		move_count += 3

	print("Passed!")

	exit(0)

