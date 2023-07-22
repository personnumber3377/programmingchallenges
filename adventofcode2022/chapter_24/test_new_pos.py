
from naive_part1 import generate_new_positions
import numpy as np
from PIL import Image



def render_mat(mat):

	qr_matrix = np.invert(mat.astype(bool), dtype=bool)
	print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()

def render_stuff(things, size):

	matrix = np.zeros((size,size))

	for thing in things:

		matrix[thing[0],thing[1]] = 1

	render_mat(matrix)

	return


if __name__=="__main__":

	old_pos = {(3,3)}

	# generate_new_positions

	new_stuff = generate_new_positions(old_pos)

	print("Result: "+str(new_stuff))
	new_shit = generate_new_positions(new_stuff)

	print("Result #2 : "+str(new_shit))
	
	#assert len(new_shit) == 25
	
	render_stuff(new_shit, 10)


	exit(0)
