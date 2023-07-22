



PART = 1
DEBUG = True

UP_SYM = "^"
DOWN_SYM = "v"
LEFT_SYM = "<"
RIGHT_SYM = ">"

DIRS = {UP_SYM: 0, LEFT_SYM: 1, DOWN_SYM: 2, RIGHT_SYM: 3}

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

OFFSETS = {UP: [0,1], LEFT: [-1,0], DOWN: [0,-1], RIGHT:[1,0]}




def fail(msg: str) -> None:
	print("[FAIL] "+str(msg))
	exit(1)

def debug(msg: str) -> None:
	if DEBUG:
		print("[DEBUG] "+str(msg))
	return






def parse_1():

	raw_in = sys.stdin.buffer.read()

	lines = raw_in.split("\n")


	width = len(lines[0]) - 2 # - 2 because first and last are walls.

	height = len(lines) - 2

	#blizzards = []  # a list of lists. first element in sublist is the coordinates as a tuple and the second element is the direction

	blizzards = {} # change of plan. Implement blizzards as a dictionary with the coordinates as key and the move direction as val.


	for y, line in enumerate(lines[1:-1]): # skip first and last lines
		for x, spot in enumerate(line[1:-1]): # skip first and last spot which are walls.
			if spot in DIRS:

				result = [[x,y],DIRS[spot]]

				blizzards[tuple((x,y))] = [[DIRS[spot],0]] # first the direction and then the counter.

	return width, height, blizzards





def parse_input():
	if PART == 1:
		return parse_1()



def update_blizzards(blizzards: dict, width: int, height: int, counter: int) -> list:

	# update blizzards according to the rules.

	for coords in blizzards: # I hope there is a more pythonic way to modify each element in a list. if you try to do for bliz in blizzards: ... then you are not actually modifying the original list, but copies of the objects or something like that.
		
		#move = blizzards[i][1]

		
		#move = blizzards[coords]
		moves = blizzards[coords]


		# Can not do this because we can have multiple blizzards at the same spot.

		# <comment>
		'''
		offset = OFFSETS[move]


		# move blizzard. here we do not need to do collision checking, because two blizzards or more blizzards can be at the same spot.

		#blizzards[i][0][0] += offset[0]
		#blizzards[i][0][1] += offset[1]

		# instead of using a list of lists, lets just use a dictionary with the coordinates as keys. it is a lot faster

		new_coords = [coords[0]+offset[0], coords[1]+offset[1]]

		del blizzards[coords] # delete old position.

		blizzards[new_coords] = move 
		'''

		# </comment>

		#new_stuff = []

		for ind, move in enumerate(moves):
			actual_move = move[0]

			count = move[1]

			if count != counter:


				offset = OFFSETS[actual_move]

				new_coords = [coords[0]+offset[0], coords[1]+offset[1]]

				if new_coords not in blizzards:
					blizzards[new_coords] = [[actual_move, counter]]
				else:
					blizzards[new_coords] += [[actual_move, counter]]



				#new_stuff.append([new_coords, actual_move])

			blizzards[coords].pop(ind) # delete it from the list

		# check if there are any blizzards left at that spot:

		if len(blizzards[coords]) == 0:

			del blizzards[coords]


	return blizzards


def solve_part_one() -> int:

	# init vars

	n = 0
	
	blizzards = {}

	width, height, blizzards = parse_input()

	# Solve path

	while True: # continue until otherwise.



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

