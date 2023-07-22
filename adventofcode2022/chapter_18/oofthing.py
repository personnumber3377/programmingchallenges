
import sys
import numpy as np

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

			if x == 0:
				
				if marked_cube[x+1,y,z] != 1 and cube[x+1,y,z] != 1:
					
					new_marked_stuff.append([x+1,y,z])
					marked_cube[x+1,y,z] = 1

			else:

				if marked_cube[x+1,y,z] != 1 and cube[x+1,y,z] != 1:
					
					new_marked_stuff.append([x+1,y,z])
					marked_cube[x+1,y,z] = 1

				if marked_cube[x-1,y,z] != 1 and cube[x-1,y,z] != 1:
					
					new_marked_stuff.append([x+1,y,z])
					marked_cube[x-1,y,z] = 1


	return marked_cube




def solve_puzzle():

	coords_list, max_coord = parse_input()
	
	cube_size = max_coord+3

	cube_thing = np.zeros((cube_size,cube_size,cube_size), dtype=bool)

	cube_thing = fill_cube(cube_thing, coords_list)
	print(cube_thing)


	outer_shape = path_find(cube_thing)


	#area = count_area(cube_thing, max_coord)

	return area



if __name__=="__main__":

	print(solve_puzzle())
	exit(0)
