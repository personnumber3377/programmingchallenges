
from naive_part1 import update_blizzards

# def update_blizzards(blizzards: dict, counter: int) -> list:

'''

DIRS = {UP_SYM: 0, LEFT_SYM: 1, DOWN_SYM: 2, RIGHT_SYM: 3}

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

OFFSETS = {UP: [0,1], LEFT: [-1,0], DOWN: [0,-1], RIGHT:[1,0]}

'''












if __name__=="__main__":

	test_bliz = {(3, 6): [[0,0]], (4, 10): [[3,0]], (0,1): [[2,0]]}
	
	correct_after = {(3, 7): [[0, 1]], (5, 10): [[3, 1]], (0, 0): [[2, 1]]}

	print("Before: "+str(test_bliz))
	update_blizzards(test_bliz, 1)

	print("After: "+str(test_bliz))
	# After: {(3, 7): [[0, 1]], (5, 10): [[3, 1]], (0, 0): [[2, 1]]}


	assert test_bliz == correct_after

	print("[+] Passed!")


	exit(0)


