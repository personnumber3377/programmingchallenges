

from naive_part1 import *




if __name__=="__main__":

	bliz = {(1, 2): [[3, 2]], (4, 2): [[0, 2]], (2, 0): [[3, 2]], (2, 2): [[1, 2], [2, 3]], (1, 0): [[1, 3]], (3, 0): [[1, 2]], (2, 1): [[1, 2], [1, 3]], (3, 1): [[0, 3]], (1, 1): [[0, 3], [2, 3]], (4, 1): [[0, 3], [1, 3]], (3, 2): [[3, 3]], (0, 2): [[3, 3]], (3, 3): [[1, 3]], (4, 0): [[3, 3]], (2, 3): [[3, 3]]}

	# def update_blizzards(blizzards: dict, counter: int, width: int, height: int) -> list:
	render_stuff(bliz,10)
	update_blizzards(bliz, 5,6,4)


	render_stuff(bliz,10)
	exit(0)

	'''

	counter: 4
width: 6
height: 4

	'''
