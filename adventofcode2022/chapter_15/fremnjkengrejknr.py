
import numpy as np
import sys

PUZZLE_NUM = 2

negative_count = 0

'''

               1    1    2    2
     0    5    0    5    0    5
-2 ..........#.................
-1 .........###................
 0 ....S...#####...............
 1 .......#######........S.....
 2 ......#########S............
 3 .....###########SB..........
 4 ....#############...........
 5 ...###############..........
 6 ..#################.........
 7 .#########S#######S#........
 8 ..#################.........
 9 ...###############..........
10 ....B############...........
11 ..S..###########............
12 ......#########.............
13 .......#######..............
14 ........#####.S.......S.....
15 B........###................
16 ..........#SB...............
17 ................S..........B
18 ....S.......................
19 ............................
20 ............S......S........
21 ............................
22 .......................B....


'''


def check_if_inside(point, radius, point2):
	# returns true if point2 is inside the circle described by point and radius

	return manhattan_dist(point, point2) <= radius



def print_line(line):
	print("".join(["#" if x == 1 else "." for x in line]))
	return


def parse_input()-> list:

	# This function creates a list of sensor coordinates and the coordinates of the nearest beacon.

	stuff = sys.stdin.buffer.read().decode('ascii')
	lines = stuff.split("\n")

	print(lines)
	max_x = 0
	for line in lines:

		words = line.split(" ")

		sensor_x = int(words[2][2:-1]) # Cut out the "x=" and the ","
		sensor_y = int(words[3][2:-1]) # Cut out the "y=" and the ":"

		beac_x = int(words[8][2:-1]) # Cut out the "x=" and the ","
		beac_y = int(words[9][2:]) # Cut out the "y="

		if sensor_x > max_x:
			max_x = sensor_x
		if beac_x > max_x:
			max_x = beac_x

		yield [[sensor_x, sensor_y], [beac_x, beac_y]]

	yield max_x

def parse_input2()-> list:

	# This function creates a list of sensor coordinates and the coordinates of the nearest beacon.

	stuff = sys.stdin.buffer.read().decode('ascii')
	lines = stuff.split("\n")

	print(lines)
	max_x = 0
	max_y = 0
	min_x = 9999999999999999999999999999
	min_y = 9999999999999999999999999999
	for line in lines:

		words = line.split(" ")

		sensor_x = int(words[2][2:-1]) # Cut out the "x=" and the ","
		sensor_y = int(words[3][2:-1]) # Cut out the "y=" and the ":"

		beac_x = int(words[8][2:-1]) # Cut out the "x=" and the ","
		beac_y = int(words[9][2:]) # Cut out the "y="

		if sensor_x > max_x:
			max_x = sensor_x
		if beac_x > max_x:
			max_x = beac_x

		if max(sensor_y, beac_y) > max_y:
			max_y = max(sensor_y, beac_y)

		if min(sensor_x, beac_x) < min_x:
			min_x = min(sensor_x, beac_x)
		
		if min(sensor_y, beac_y) < min_y:
			min_y = min(sensor_y, beac_y)

		yield [[sensor_x, sensor_y], [beac_x, beac_y]]

	yield max_x
	yield min_x
	yield max_y
	yield min_y


def manhattan_dist(p0,p1):
	# thanks wikipedia https://en.wikipedia.org/wiki/Taxicab_geometry    "For example, in R2, the taxicab distance between p=(p1,p2) and q=(q1,q2) is |p1 - q1| + |p2 - q2| ."

	# |p1 - q1| + |p2 - q2|
	#print("Manhattan distance: "+str(abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])))

	#print("p0: "+str(p0))

	#print("p1: "+str(p1))

	return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])

def line_dist(p,y0):
	
	# returns the manhattan distance from the point p to the line y=y0

	return abs(p[1]-y0) # the distance is simply the absolute value of the difference in the y coordinates


def write_line(line, sens_to_beac, sens_to_line, y_line, sensor, beacon):

	global negative_count

	# This actually writes to the line
	x_coord = sensor[0]

	y_coord = sensor[1]

	print("Line == "+str(line))
	print("len(line) == "+str(len(line)))
	print("sens_to_beac == "+str(sens_to_beac))
	print("sens_to_line == "+str(sens_to_line))
	print("x_coord == "+str(x_coord))

	# first is to get the "width" of the shape at the line y=2000000
	if sens_to_beac < sens_to_line:
		print("Does not intersect")
		# The shape does not intersect with the line
		return line



	width = sens_to_beac - sens_to_line
	
	assert width >= 0
	

	offset_thing = 10000000

	print("width == "+str(width))
	start_index = x_coord - width
	end_index = x_coord + width + 1 # + 1 because the range does not include the end index.
	#start_index += 5
	#end_index += 5
	start_index += 1000000
	end_index += 1000000
	assert start_index >= 0
	assert end_index >= 0
	assert end_index >= start_index
	print("start_index: "+str(start_index))
	print("end_index: "+str(end_index))
	line[start_index:end_index] = 1 # mark the line

	#if y_coord == y_line or beacon[1] == y_line:
		#negative_count += 1
		#print("Incremented negative_count!")

	return line 





def calculate_line(sensors_and_beacons: list) -> list:


	global negative_count
	max_x = sensors_and_beacons[-1]
	
	sensors_and_beacons.pop(-1) # the last element is the maximum x coordinate .

	line = np.array([0]*10000000) # I don't know how to create flat lists without doing this. If you do np.zeros((1,10)) you will get a matrix with one column instead of a list.
	#line = np.array([0]*100)
	#print(line)

	y_line = 2000000

	#y_line = 10

	# this next part is the core of the program. It fills in the spots where the beacon can not be, by calculating the Manhattan distance and then using that to mark the line.

	# we need the distance to the closest beacon and the distance to the line y=2000000
	count = 0

	for sens_and_beac in sensors_and_beacons:
		
		sens = sens_and_beac[0]
		closest_beac = sens_and_beac[1]

		dist_sens_to_beac = manhattan_dist(sens, closest_beac)

		dist_sens_to_line = line_dist(sens, y_line)
		#print("Dist sens_to_line : "+str(dist_sens_to_line))
		#print("dist_sens_to_beac : "+str(dist_sens_to_beac))

		line = write_line(line, dist_sens_to_beac, dist_sens_to_line,y_line, sens, closest_beac)
		#print("Line: "+str(line))
		#print("Line: ")
		#print_line(line)
	
	#return count

	# account for shit which is on the line itself

	distinct_sensors_y_coords = {thing[0][1] for thing in sensors_and_beacons}

	distinct_beacons_y_coords = {thing[1][1] for thing in sensors_and_beacons}

	for sens in distinct_sensors_y_coords:
		if sens == y_line:
			negative_count += 1

	for beac in distinct_beacons_y_coords:
		if beac == y_line:
			negative_count += 1



	return line

def solve_puzzle_part1():
	sensors_and_beacons = list(parse_input())


	result = calculate_line(sensors_and_beacons)
	print(result[100000-2:100000+30])
	result = sum(result) # the marked spaces where the beacon can not be is marked with ones and the rest are zeroes so the amount of spaces where it can not be is just the sum of this list.



	return result



def check_no_overlap(list_stuff):

	# This returns True if the list of ranges are non-overlapping . Otherwise returns false. The indexes of the ranges are both start- and end-inclusive.

	for i in range(len(list_stuff)):
		list_to_be_checked = list_stuff[i]
		for j in range(list_stuff):
			if i==j:
				# current checking list
				continue
			other_list = list_stuff[j]

			#range_1 = range(list_to_be_checked[0], list_to_be_checked[1]+1)

			#range_2 = range(other_list[0], other_list[1]+1)

			x = range(list_to_be_checked[0], list_to_be_checked[1]+1)

			y = range(other_list[0], other_list[1]+1)

			# range(max(x[0], y[0]), min(x[-1], y[-1])+1)

			if list(range(max(x[0], y[0]), min(x[-1], y[-1])+1)) != []:
				
				# Overlap exists!

				return False

	return True





def merge_ranges(range_list):

	# This function merges two ranges for example let range_list be [[1,2],[4,5]] and new_range be [2,4] then this function will output [[1,5]] .
	# Similarly if range_list is [[1,2],[4,5]] and new_range is [5,7]



	# This function basically implements the below rust snippet.

	'''


	        ranges.sort_by_key(|r| *r.start());

        ranges.into_iter().coalesce(|a, b| {
            if b.start() - 1 <= *a.end() {
                if b.end() > a.end() {
                    Ok(*a.start()..=*b.end())
                } else {
                    Ok(a)
                }
            } else {
                Err((a, b))
            }
        })

	'''

	# list_thing.sort(key=lambda x: x[0])

	# Sort ranges .

	range_list.sort(key=lambda x: x[0])

	# Now coalesce.


	final_thing = []

	for i in range(len(range_list)-1):
		a = range_list[i]
		b = range_list[i+1]

		if b[0] -1 <= a[1]:
			if b[1] > a[1]:
				final_thing.append([a[0], b[1]])
			else:
				final_thing.append(a)
		else:
			print("Error!")
			exit(1)







	'''

	add_range = True # assume that we will have to add it to the list until proven otherwise.

	for range_thing in range_list:

		start = new_range[0]
		end = new_range[1]

		if range_thing[0] <= start and range_thing[1] >= end:

			# This range is contained entirely withing the other range and because no other range has elements of this bigger range as a part of it then we can already break here
			
			add_range = False
		
			break
		
		if range_thing[0] > start and range_thing[1] >= end: # Here the left side of new_range is smaller than the start of the list and the end is smaller than the end of the other list so we need to extend the range from the start.

			range_thing[0] = start

			add_range = False

	'''



	assert check_no_overlap(final_thing)

	return final_thing


def fill_in_range(ranges, sensor, beacon):

	rad = manhattan_dist(sensor, beacon)

	assert rad >= 0

	# the range is basically center-y_coord to center+y_coord+1

	y_coord_sens = sensor[1]
	x_coord_sens = sensor[0]
	width = 0
	
	for y in range(y_coord_sens-rad, y_coord_sens):
		
		ranges[y_coord_sens].append([x_coord_sens-width,x_coord_sens+width+1]) # start, end
		width += 1

	return ranges




def check_spaces(sensors_and_beacons):
	
	'''
	yield max_x
	yield min_x
	yield max_y
	yield min_y
	'''

	min_y = sensors_and_beacons.pop(-1)
	max_y = sensors_and_beacons.pop(-1)
	min_x = sensors_and_beacons.pop(-1)
	max_x = sensors_and_beacons.pop(-1)


	assert all(isinstance(x, int) for x in [min_x, min_y, max_x, max_y])

	assert min_x <= max_x

	print("min_y == "+str(min_y))
	print("max_y == "+str(max_y))

	assert min_y <= max_y
	# but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.


	#for x in range(min_x, max_x+1):
	#	for y in range(min_y, max_y+1):
	
	count = 0
	
	ranges = [[]]*4000000




	# fill in the ranges from the sensors and beacons.
	print("len(sensors_and_beacons) == "+str(len(sensors_and_beacons)))
	print("Filling in ranges: ")

	for sensor, beacon in sensors_and_beacons:

		ranges = fill_in_range(ranges, sensor, beacon)

	# def merge_ranges(range_list, new_range):
	print("Merging ranges:")
	for i in range(len(ranges)):

		ranges[i] = merge_ranges(ranges[i]) # merge all of the ranges of the x axis

	print("ranges == "+str(ranges))






	'''

	for x in range(0, 4000000+1):
		
		for y in range(0, 4000000+1):
			count += 1
			# def check_if_inside(point, radius, point2):
			
			if count % 1000 == 0:
				print(count)

			point = [x,y]

			is_right_space = True

			for sens, beac in sensors_and_beacons:
				
				rad = manhattan_dist(sens, beac)

				if check_if_inside(point,rad,sens):
		
					is_right_space = False

			if is_right_space:
		
				return point
	print("Could not find hidden beacon")

	'''






def solve_puzzle_part2():

	sensors_and_beacons = list(parse_input2())
	result = check_spaces(sensors_and_beacons)
	return result


if __name__=="__main__":
	if PUZZLE_NUM == 1:
		print("Solution to puzzle: "+str(solve_puzzle_part1()-negative_count))
		#print("negative_count == "+str(negative_count))
	elif PUZZLE_NUM == 2:
		print("Solution to puzzle: "+str(solve_puzzle_part2()))
	else:
		print("Invalid puzzle number!")
		exit(1)
	exit(0)