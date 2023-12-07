
import sys
from functools import reduce
from operator import mul

def parse_input() -> list:
	contents = sys.stdin.read()
	if contents[-1] == "\n":
		contents = contents[:-1]
	lines = contents.split("\n")
	# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
	output = []

	color_order = ["red", "green", "blue"]
	#print("Here are the lines")
	for line in lines:
		#print(line)
		line = line[line.index(":")+2:] # Skip the "Game #: " part. This should work for the toy input, but doesn't work when the Game number exceeds nine.
		showed_cubes_groups = line.split("; ") # get the cubes which were showed at one time
		#print(showed_cubes_groups)
		showed_cubes_stuff = []
		for showed_cubes in showed_cubes_groups:
			cubes_of_distinct_color = showed_cubes.split(", ")
			#print(cubes_of_distinct_color)
			new_cubes = [0,0,0]
			for cube_amount_of_color_certain in cubes_of_distinct_color:
				#print("cube_amount_of_color_certain == "+str(cube_amount_of_color_certain))
				integer, color = cube_amount_of_color_certain.split(" ")
				integer = int(integer)
				#print(str(integer)+":"+color)
				index = color_order.index(color)
				new_cubes[index] = integer
			showed_cubes_stuff.append(new_cubes)
		output.append(showed_cubes_stuff)
	#print(output)

	return output

def get_min(game: list) -> bool:
	# Here are the maximum number of each color encountered in the game so far.
	max_cubes = [0,0,0]
	for shown_cubes_round in game:
		# Check if we show more cubes of a certain color, than there are in the bag.
		max_cubes = [max_cubes[i] if max_cubes[i] >= shown_cubes_round[i] else shown_cubes_round[i] for i in range(len(shown_cubes_round))]	
	# Multiply the amounts together
	res = reduce(mul, max_cubes, 1)
	return res


def get_possible_count(games: list):
	val = 0
	for i, game in enumerate(games): # Each element in the games list is a list of lists, each of which has the amount of colored cubes shown for each color.
		res = get_min(game)
		val += res
	return val


def main() -> int:
	game_integers = parse_input()
	result = get_possible_count(game_integers)
	print(result)
	return 0

if __name__=="__main__":
	exit(main())
