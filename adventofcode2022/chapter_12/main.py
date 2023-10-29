
import numpy as np
import sys

DEBUG = False

def debug(thing):
	if DEBUG:

		print("[DEBUG] "+str(thing))


def show_solution(shit_oof2, end_point, start_point):



	cur_point = end_point
	while cur_point != start_point:
		cur_point = end_point



def get_map() -> np.array:
	global input_lines
	input_stuff = sys.stdin.read()
	lines = input_stuff.split("\n")
	input_lines = lines
	mat_width = len(lines[0])
	mat_height = len(lines)
	out_matrix = np.zeros((mat_height, mat_width))

	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			
			if char == "S":
				start_point = (i,j)
			elif char == "E":
				end_point = (i,j)
				num = ord("z") - 97 # ord('a') = 97

				out_matrix[i][j] = num # Update map
			else:

				num = ord(char) - 97 # ord('a') = 97

				out_matrix[i][j] = num # Update map

	debug(out_matrix)
	return out_matrix, start_point, end_point, mat_width, mat_height



def render_solution(w,h,shit_oof2):
	matrix = np.zeros((h,w))
	for thing in shit_oof2:
		x = thing[1]
		y = thing[0]

		matrix[y][x] = thing[2]

	print(matrix)

	return




def solve() -> int:
	rock_map, start_point, end_point, w, h = get_map()

	step_count = 0
	shit_oof = set({tuple(start_point)})
	to_check = set({tuple(start_point)})
	while tuple(end_point) not in shit_oof:

		to_add = []

		for place in to_check:
			i = place[0]
			j = place[1]

			cur_height = rock_map[i][j]

			neighbours = [[i,j-1], [i,j+1], [i+1,j], [i-1,j]]

			for count, neig in enumerate(neighbours):
				if -1 in neig:
					neighbours[count] = None

				elif neig[1] >= w:
					neighbours[count] = None
				elif neig[0] >= h:
					neighbours[count] = None

			while None in neighbours:
				neighbours.remove(None) # Delete all invalid positions.

			for neig in neighbours:
				if tuple(neig) in shit_oof: # Check if modified
					continue

				y = neig[0]
				x = neig[1]
				other_height = rock_map[y][x]
				if cur_height - other_height >= -1: # The other rock can be one more than current height

					to_add.append(tuple(neig))
		to_check = set()
		for thing in to_add:
			to_check.add(thing)
			shit_oof.add(thing)
			
		step_count += 1

	#render_solution(w,h,shit_oof2)
		
	return step_count

def main():

	min_path_length = solve()
	print(min_path_length)
	return 0


if __name__=="__main__":

	exit(main())

