
from tetrisfinal import *


WIDTH = 7

HEIGHT = 30

if __name__=="__main__":

	# This tries to use the update_col_heights function and see if it works properly.

	# def update_col_heights(shape, x_coord, y_coord):

	selected_shape = 0
	
	x_coord = 1

	y_coord = 2


	update_col_heights(selected_shape, x_coord, y_coord)

	print("Column heights after: "+str(col_heights))

	# This is just to observe the matrix

	#place_block()
	#poopooshit = copy.deepcopy(game_map)
	poopooshit = np.zeros((7,30)).astype("bool")
	poopooshit = place_block(shapes[selected_shape], x_coord, y_coord, poopooshit)
	for i in range(WIDTH):
		h = 0
		for j in range(HEIGHT):

			if poopooshit[i][j] == 1:
				h = j

		print("Height for i == "+str(i)+" : "+str(h))



	render_mat(poopooshit)
	exit(0)

