
import sys
import numpy as np

def count_visible_trees(filename: str) -> int:

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
	tot_count = 0
	marked = np.zeros(trees_np.shape)
	for j in range(4): # rotate the vector by 90 degrees by each cycle
		# go through every list in the numpy array
		
		for i in range(len(trees_np)): # for every list in array:
			print("len(trees_np) == " + str(len(trees_np)))
			maximum = -1
			for k in range(np.size(trees_np[i])):

				cur_integer = trees_np[i,k] # current integer
				print("Current integer: " + str(cur_integer))

				if maximum < cur_integer:
					
					maximum = cur_integer
					if not marked[i,k]: # we can not mark as zero because then it interferes with the counting from the other sides
						tot_count += 1
						marked[i,k] = 1

					#trees_np[i,k] = 0 # we need to do this such that we do not count the same tree multiple times
		print("Matrix after rotation number: " + str(j))
		print(trees_np)
		print("Marked matrix:")
		print(marked)
		marked = np.rot90(marked)
		trees_np = np.rot90(trees_np)
	return tot_count



			# current integer is cur_list[0]








if __name__=="__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 trees.py FILENAME")
		exit(0)
	print(count_visible_trees(sys.argv[1]))
	exit(0)


