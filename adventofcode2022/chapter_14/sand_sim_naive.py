
#from convenience import *
import sys
import numpy as np


def handle_input():
	lines = sys.stdin.readlines()
	# Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point.

	# For example: 
	# 498,4 -> 498,6 -> 496,6
	# 503,4 -> 502,4 -> 502,9 -> 494,9

	out_list = []

	for line in lines:
		
		# each line corresponds to one "pattern"

		coords = line.split("->")
		coord_list = [[int(x) for x in coord.split(",")] for coord in coords]
		
		#debug("coord_list == "+str(coord_list))

		out_list.append(coord_list)

	#debug("out_list == "+str(out_list))

	return out_list




def draw_line(matrix, p0, p1):

	# Draw a straight line

	assert p0[0] == p1[0] or p0[1] == p1[1]


	y_start = min([p0[1], p1[1]])
	x_start = min([p0[0], p1[0]])

	y_end = max([p0[1], p1[1]])
	x_end = max([p0[0], p1[0]])

	print("(x_start, x_end) == ("+str(x_start)+","+str(x_end)+")")
	print("(y_start, y_end) == ("+str(y_start)+","+str(y_end)+")")


	if x_start == x_end:


		matrix[x_start, y_start:y_end+1] = 1
	else:
		matrix[x_start:x_end+1, y_end] = 1




	return matrix



def construct_matrix(coordinates):

	# Generate a numpy matrix from the coordinate list

	# First figure out the shape of the matrix:

	x_coord_max = 0
	y_coord_max = 0

	for line_thing in coordinates:
		for coord in line_thing:
			if coord[0] > x_coord_max:
				x_coord_max = coord[0]
			if coord[1] > y_coord_max:
				y_coord_max = coord[1]

	print("x_coord_max == "+str(x_coord_max))
	print("y_coord_max == "+str(y_coord_max))

	matrix = np.zeros((x_coord_max+2, y_coord_max+2)) # +1 , because if we do not add one we maybe get an edge case where the sand "falls" out of bounds of the matrix. This ensures that we should stay in bounds.
	#matrix = matrix.T
	# Place lines.

	for line_thing in coordinates:

		for i in range(len(line_thing)-1):

			matrix = draw_line(matrix, line_thing[i], line_thing[i+1]) # Draw line

	return matrix

def sim_sand(mat):


	# Simulate sand and count the number of placed sand blocks.

	print("mat == "+str(mat))

	print("Current sand matrix at the start: ")

	print(mat[494:500,0:])


	n = 0




	abyss = False

	while True:
		sand_coord = [500,0] # reset coordinates

		# check abyss:

		if abyss:
			break


		print("Current sand matrix: ")

		print(mat[494:503,0:].T)


		# Nested while loop . Eww

		while True:

			# check abyss

			if sand_coord[1] == mat.shape[1]-1:
				abyss = True
				break

			# check first before moving

			print("Sand coordinates: "+str(sand_coord[0])+", "+str(sand_coord[1]))
			print("mat["+str(sand_coord[0])+", "+str(sand_coord[1]+1)+"] == "+str(mat[sand_coord[0], sand_coord[1]+1]))
			if mat[sand_coord[0], sand_coord[1]+1]: # check if occupied

				# "If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left."

				if mat[sand_coord[0]-1, sand_coord[1]+1]:

					print("sand_coord[0] == "+str(sand_coord[0]))
					print("sand_coord[1] == "+str(sand_coord[1]))

					if mat[sand_coord[0]+1, sand_coord[1]+1]:

						# place sand block
						print("Placed sand block at "+str(tuple((sand_coord[0], sand_coord[1]))))

						mat[sand_coord[0], sand_coord[1]] = 1

						# increment block counter:

						n += 1

						# break out of sand loop

						break

					else:

						# Move to the right

						sand_coord[0] += 1

				else:

					# Move to the left

					sand_coord[0] -= 1

			sand_coord[1] += 1 # move down one block

	return n





def solve_puzzle():

	#terr_mat = handle_input()
	coord_list = handle_input()

	mat = construct_matrix(coord_list)

	sand_count = sim_sand(mat)


	return sand_count


if __name__=="__main__":
	#good("Solution to puzzle is this: "+str(solve_puzzle()))
	print("Solution to puzzle is this: "+str(solve_puzzle()))
	exit(0)
