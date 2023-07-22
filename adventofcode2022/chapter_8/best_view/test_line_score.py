
from trees_view import *




if __name__=="__main__":

	cur_height = 7
	tree_line = np.matrix([[1,2,3,4,8,7,6]])
	# get_line_score(tree_line, cur_height)
	print(get_line_score(tree_line, cur_height, debug=True))

	#return 0