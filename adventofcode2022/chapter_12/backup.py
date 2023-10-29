
import numpy as np
import sys

DEBUG = True

def debug(thing):
	if DEBUG:

		print("[DEBUG] "+str(thing))


def get_map() -> np.array:
	input_stuff = sys.stdin.read()
	lines = input_stuff.split("\n")

	mat_width = len(lines[0])
	mat_height = len(lines)
	out_matrix = np.zeros((mat_height, mat_width))

	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			
			if char == "S":
				start_point = (i,j)
			elif char == "E":
				end_point = (i,j)
			else:

				num = ord(char) - 97 # ord('a') = 97

				out_matrix[i][j] = num # Update map

	debug(out_matrix)
	return out_matrix, start_point, end_point, mat_width, mat_height


def solve() -> int:
	rock_map, start_point, end_point, w, h = get_map()
	debug("rock_map == "+str(rock_map))

	flood_map = np.zeros(rock_map.shape)

	flood_map[start_point[0], start_point[1]] = 1 # Set the start for pathfinding.

	step_count = 0
	important = False
	shit_oof = set()
	while tuple(end_point) not in shit_oof:
		print("New step!")
		# First update the flood map.
		#modified = set()
		for i in range(h):
			for j in range(w):
				integer = flood_map[i][j]
				#print("integer flood_map[i][j] == "+str(flood_map[i][j]))
				#print("flood_map[i] == "+str(flood_map[i]))
				#print("flood_map[i][j] == "+str(flood_map[i][j]))
				print("i == "+str(i))
				print("j == "+str(j))
				#print("flood_map == "+str(flood_map))
				#print("flood_map[0] == "+str(flood_map[0]))
				#print("flood_map[3] == "+str(flood_map[3]))

				cur_coordinates = [i,j]


				#if i == 1 and j == 1:
				#	print("IMPORTANT")

				if integer >= 1:
					#print("line == "+str(line))
					# Now check neighbours and increment.

					cur_height = rock_map[i][j]

					neighbours = [[i,j-1], [i,j+1], [i+1,j], [i-1,j]]

					if i == 3 and j == 2:
						print("IMPORTANT")
						debug("neighbours == "+str(neighbours))
						important = True
					# bounds check neighbours.
					# 2, 4


					for count, neig in enumerate(neighbours):
						if -1 in neig:
							neighbours[count] = None

						elif neig[1] >= w:
							neighbours[count] = None
						elif neig[0] >= h:
							neighbours[count] = None

					while None in neighbours:
						neighbours.remove(None) # Delete all invalid positions.
					#if important:
					#	print("neighbours after == "+str(neighbours))

					print("w == "+str(w))
					print("h == "+str(h))
					print("neighbours after == "+str(neighbours))
					for neig in neighbours:
						if tuple(neig) in shit_oof: # Check if modified
							continue

						#modified.add(tuple(neig))
						y = neig[0]
						x = neig[1]
						print("x == "+str(x))
						print("y == "+str(y))
						other_height = rock_map[y][x]
						if important:
							print("x == "+str(x))
							print("y == "+str(y))
							if x == 4 and y == 2:
								print("cur_height == "+str(cur_height))
								print("other_height == "+str(other_height))
						#print("cur_height == "+str(cur_height))
						#print("other_height == "+str(other_height))
						if cur_height - other_height >= -1: # The other rock can be one more than current height

							#print("Incrementing!")
							#print("[i,j] == "+str([i,j]))
							#print("flood_map[i,j] == "+str(flood_map[i][j]))
							#print("flood_map before increment: "+str(flood_map))
							#flood_map[i][j] += 1
							#print("pooopooooo")

							#flood_map[y][x] += 1 # instead of adding to the flood map, we just add this position to the set

							shit_oof.add(tuple(neig))
							#print("flood_map[y][x] == "+str(flood_map[y][x]))
							#print("after: "+str(flood_map))
				#elif integer > 1:
				#	flood_map[cur_coordinates[0]][cur_coordinates[1]] += 1
				
				important = False
		#debug("flood_map == "+str(flood_map))
		print("shit_oof == "+str(shit_oof))

		step_count += 1
		
	return step_count

def main():

	min_path_length = solve()
	print(min_path_length)
	return 0


if __name__=="__main__":

	exit(main())

