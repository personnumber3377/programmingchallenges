
from part2 import *
import numpy as np
from PIL import Image

def render_mat(mat):

	print("mat.shape == "+str(mat.shape))

	qr_matrix = np.invert(mat.astype(bool), dtype=bool)
	print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()


def to_mat(ranges, range_min, range_max):


	matrix = np.zeros((range_max-range_min, range_max-range_min))

	for i, range_thing in enumerate(ranges):
		
		# each range_thing is the ranges on the x_axis
		
		for range_thing2 in range_thing:

			start = range_thing2[0]-range_min

			end = range_thing2[1] - range_min

			assert start >= 0
			assert end >= 0
			#print("matrix[i] == "+str(matrix[i]))
			matrix[i][start:end+1] = 1

			debug("start, end == "+str(start)+", "+str(end))

	# render

	#render_mat(matrix)



	return matrix


def thing(stuff,range_min,range_max):

	matrix = to_mat(stuff, range_min, range_max)

	render_mat(matrix)

	return




if __name__=="__main__":

	# def fill_in_range(ranges, sensor, beacon):
	'''
	ranges = []

	for i in range(10):
		ranges.append([])

	# ranges = fill_in_range(ranges, sensor, beacon)

	sensor = [5,5]

	beacon = [5,7]
	print("ranges == "+str(ranges))
	ranges = fill_in_range(ranges, sensor, beacon)

	print(ranges)
	
	thing(ranges, 0, 10)
	'''

	# def coalesce_thing(range_list):

	thing = []

	for i in range(1,10):
		thing.append([i,i+1]) # create a list of lists of length two where the second element is one bigger than the last

	print("thing == "+str(thing))

	#result1 = coalesce_thing(thing)
	result2 = coalesce_thing([[1,5],[4,7],[10,13],[13,14]])
	#print("result1: "+str(result1))
	print("result2: "+str(result2))
	exit(0)






