
import sys
import numpy as np
from PIL import Image



def parse_input():

	# return sys.stdin.buffer.read()#.decode('ascii')

	thing = sys.stdin.buffer.read().decode('ascii')

	thing = thing.split("\n")

	out = []
	max_coord = 0

	for coords in thing:
		poopoo = coords.split(",")

		poopoo = [int(x) for x in poopoo]

		out.append(poopoo)
		maximum = max(poopoo)

		if maximum > max_coord:
			max_coord = maximum

	return out, max_coord



def render_mat(mat):

	print("mat.shape == "+str(mat.shape))

	qr_matrix = np.invert(mat.astype(bool), dtype=bool)
	print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()

def fill_cube(cube, coords):

	for coord in coords:
		cube[coord[0]+1,coord[1]+1,coord[2]+1] = 1
	return cube


def count_area(cube, max_coord):
	count = 0
	size = max_coord+2
	for x in range(1,size):
		for y in range(1,size):
			for z in range(1,size):

				# check if occupied
				
				if cube[x,y,z] == True:
					print("(x,y,z) == "+str("("+str(x)+","+str(y)+","+str(z)+")"))
					if cube[x-1,y,z] == False:
						count += 1

					if cube[x+1,y,z] == False:
						count += 1

					if cube[x,y-1,z] == False:
						count += 1

					if cube[x,y+1,z] == False:
						count += 1

					if cube[x,y,z+1] == False:
						count += 1

					if cube[x,y,z-1] == False:
						count += 1

	return count



def check_stuff(x,y,z,marked_cube,new_marked_stuff,index,cube):


	index_thing = [x,y,z]


	print("marked_cube[*index_thing] == "+str(marked_cube[*index_thing]))

	if index_thing[index] == 0:
		index_thing[index] += 1

		if marked_cube[*index_thing] != 1 and cube[*index_thing] != 1:
			
			new_marked_stuff.append([*index_thing])
			marked_cube[*index_thing] = 1

	elif index_thing[index] == cube.shape[0]-1:
		

		'''
		index_thing[index] += 1
		if marked_cube[*index_thing] != 1 and cube[*index_thing] != 1:
			
			new_marked_stuff.append([*index_thing])
			marked_cube[*index_thing] = 1

		
		'''

		index_thing[index] -= 1



		if marked_cube[*index_thing] != 1 and cube[*index_thing] != 1:
			
			new_marked_stuff.append([x+1,y,z])
			marked_cube[*index_thing] = 1
	
	else:

		index_thing[index] += 1
		if marked_cube[*index_thing] != 1 and cube[*index_thing] != 1:
			
			new_marked_stuff.append([*index_thing])
			marked_cube[*index_thing] = 1

		index_thing[index] -= 2 # -= 2 because we incremented it by one so to get one lower we must subtract two. one to get to the original value and then one to get to the value which is one less than the original value.


		if marked_cube[*index_thing] != 1 and cube[*index_thing] != 1:
			
			new_marked_stuff.append([x+1,y,z])
			marked_cube[*index_thing] = 1

	return marked_cube, new_marked_stuff



def path_find(cube):

	# This returns the outer shape of the shape.

	marked_stuff = [[0,0,0]]

	marked_cube = np.zeros(cube.shape)

	while True:

		if marked_stuff == []:
			break
		
		new_marked_stuff = []
		
		for coordinates in marked_stuff:

			x = coordinates[0]
			y = coordinates[1]
			z = coordinates[2]
			# check neighbours

			marked_cube, new_marked_stuff = check_stuff(x,y,z,marked_cube,new_marked_stuff,0,cube)
			marked_cube, new_marked_stuff = check_stuff(x,y,z,marked_cube,new_marked_stuff,1,cube)
			marked_cube, new_marked_stuff = check_stuff(x,y,z,marked_cube,new_marked_stuff,2,cube)

		marked_stuff = new_marked_stuff


	return marked_cube


def sanity_check(outer_shape, cube_thing):  # Check that the outside and the rock thing do not intersect.
	
	result = outer_shape.astype("bool") & cube_thing.astype("bool")

	if not np.all(result == 0):
		print("FAIL 1")
		exit(1)
	
	'''
	result = rock.astype("bool") | cube_thing.astype("bool")

	if not np.all(result == 1):
		print("FAIL 2")
		exit(1)
	'''


	print("Passed!")
	return



def solve_puzzle():

	coords_list, max_coord = parse_input()
	
	cube_size = max_coord+3

	cube_thing = np.zeros((cube_size,cube_size,cube_size), dtype=bool)

	cube_thing = fill_cube(cube_thing, coords_list)
	print("Cube thing: ")
	print(cube_thing)


	outer_shape = path_find(cube_thing)

	# get the actual shape. the outer_shape is a matrix where the outside is marked

	rock = np.logical_not(outer_shape)
	print("Here is the rock:")
	print(rock)

	# the outer shape and the original cube_thing must not intersect.

	sanity_check(outer_shape, cube_thing)

	cube_slice = cube_thing[10]

	black_cube_slice = np.zeros((cube_slice.shape[0], cube_slice.shape[0], 3))

	for i in range(cube_slice.shape[0]):

		for j in range(cube_slice.shape[1]):

			if not cube_slice[i,j]:

				black_cube_slice[i,j] = 255




	outer_shape_slice = outer_shape[10]

	red_outer_shape_slice = np.zeros((cube_slice.shape[0], cube_slice.shape[0], 3))

	for i in range(outer_shape_slice.shape[0]):

		for j in range(outer_shape_slice.shape[1]):

			if not outer_shape_slice[i,j]:

				red_outer_shape_slice[i,j,0] = 255


	result = red_outer_shape_slice | black_cube_slice

	img = Image.fromarray(result, 'RGB')
	#return img
	img.show()

	#img = Image.fromarray(np_array, 'RGB')
	#return img
	#area = count_area(cube_thing, max_coord)
	area = count_area(rock, max_coord)

	return area



if __name__=="__main__":

	print(solve_puzzle())
	exit(0)
