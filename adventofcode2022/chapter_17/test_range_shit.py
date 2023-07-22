
from tetriswithrangedetection import *



if __name__=="__main__":

	# This file tests the block collision detection mechanism.

	# def update_width_ranges(shape_num, x_coord, y_coord):

	# First add a "shape" to the thing

	shape_num = 0
	
	x_coord = 2
	y_coord = 1




	update_width_ranges(shape_num,x_coord,y_coord)

	shape_num = 1

	update_width_ranges(shape_num,x_coord,y_coord)

	# Now check the actual collision.

	# def check_width_ranges(shape,x_coord,y_coord):

	shape_num = 2

	


	print("check_width_ranges(shape,x_coord,y_coord) == "+str(check_width_ranges(shape_num,x_coord,y_coord)))

