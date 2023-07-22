
import sys
import numpy as np

def get_line_score(line: np.matrix, cur_height: int, debug=False):
	# go through every element and 

	count = 1
	index = 0
	if debug:
		print("line.shape[1] == " + str(line.shape[1]))
	while line[0,index] < cur_height and index != line.shape[1]:
		if debug:
			print("line[index] == " + str(line[0,index]))
			print("cur_height == " + str(cur_height))
			print("len(line) == " + str(len(line[0])))

		index += 1
		count += 1
	return count


def best_view(trees: np.matrix) -> int:
	shape_of_matrix = trees.shape
	x_max = shape_of_matrix[0]
	y_max = shape_of_matrix[1]
	best_score = 0
	for x in range(x_max):
		for y in range(y_max):
			# check each direction

			if x > 0:
				# current line is trees[y]
				line = trees[x,:y]
				line.reverse()
				score = get_line_score(line, trees[x,y])



def get_best_view(filename: str) -> int:

	fh = open(filename, "r")
	lines = fh.readlines()
	fh.close()

	# first make a matrix of the trees:

	tree_matrix = []

	for line in lines:
		if line[-1] == "\n":
			line = line[:-1] # remove newline if it exists
		tree_matrix.append([int(x) for x in list(line)]) # this assumes that each tree is only one integer which is less than 10 and bigger than -1
	trees_np = np.matrix(tree_matrix)
	best_view_score = best_view(trees_np)
	
	return tot_count









if __name__=="__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 trees.py FILENAME")
		exit(0)
	print(get_best_view(sys.argv[1]))
	exit(0)


