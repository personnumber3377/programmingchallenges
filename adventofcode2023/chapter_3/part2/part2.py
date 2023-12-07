
import sys

all_nums = set()

def parse_input() -> list:
	# -1 means a special character
	lines = sys.stdin.read().split("\n")
	out_matrix = []
	not_special_chars = ".0123456789"
	#for line in lines:
	#	cur_out_line = []
	#	for char in line:
	#		if char not in not_special_chars:
	#			# Special character
	#			cur_out_line.append(-1)
	return lines


def get_neighbours(input_matrix: list, x: int, y: int) -> list:

	max_x = len(input_matrix[0]) - 1
	max_y = len(input_matrix) - 1
	not_special_chars = ".0123456789"
	neighbours = [[x,y-1], [x,y+1], [x+1,y], [x-1,y], [x-1,y-1], [x-1,y+1], [x+1,y+1], [x+1,y-1]]
	#for i, neig in enumerate(neighbours):
	i = 0
	while i < len(neighbours):
		neig = neighbours[i]
		if neig[0] > max_x:
			neighbours.pop(i)
			i -= 1
		elif neig[0] < 0:
			neighbours.pop(i)
			i -= 1

		if neig[1] > max_y:
			neighbours.pop(i)
			i -= 1
		elif neig[1] < 0:
			neighbours.pop(i)
			i -= 1
		i += 1
	return neighbours


def check_neighbours(input_matrix: list, x: int, y: int) -> bool:
	max_x = len(input_matrix[0]) - 1
	max_y = len(input_matrix) - 1
	not_special_chars = ".0123456789"
	neighbours = [[x,y-1], [x,y+1], [x+1,y], [x-1,y], [x-1,y-1], [x-1,y+1], [x+1,y+1], [x+1,y-1]]
	#for i, neig in enumerate(neighbours):
	i = 0
	while i < len(neighbours):
		neig = neighbours[i]
		if neig[0] > max_x:
			neighbours.pop(i)
			i -= 1
		elif neig[0] < 0:
			neighbours.pop(i)
			i -= 1

		if neig[1] > max_y:
			neighbours.pop(i)
			i -= 1
		elif neig[1] < 0:
			neighbours.pop(i)
			i -= 1
		i += 1

	# Now actually check for special chars.
	for neig in neighbours:
		char = input_matrix[neig[1]][neig[0]]
		if char not in not_special_chars:
			return True # This place has a neighbour which is a special character

	return False


def check_neighbours_nums(input_matrix: list, x: int, y: int) -> bool:
	# Counts the number of numbers near x,y .
	print("="*20)
	print("Called check_neighbours_nums")
	global all_nums
	neighbours = get_neighbours(input_matrix, x, y)
	# Now check for the numbers.
	out = []
	already_checked = [] # These are the spots which we have already checked. This is used to prevent reading numbers which we have already read.
	numbers = "0123456789"
	for neig in neighbours:
		print("already_checked: "+str(already_checked))
		print("neig: "+str(neig))
		if neig in already_checked:
			continue
		if input_matrix[neig[1]][neig[0]] in numbers: # We are adjacent to a number.
			#out.append(neig)
			x_diff = 0

			#while input_matrix[neig[1]][neig[0] - x_diff] in numbers and neig[0] - x_diff != len(input_matrix[neig[1]]): # Check if the number continues.
			# neig[0] - x_diff
			while input_matrix[neig[1]][neig[0] - x_diff] in numbers and neig[0] - x_diff >= 0:
				x_diff += 1
				already_checked.append([neig[0] - x_diff, neig[1]])

			num_min_x = neig[0] - x_diff + 1
			helper_string = input_matrix[neig[1]][num_min_x:]
			x_diff = 0

			print("poopoo already_checked == "+str(already_checked))
			print("helper_string == "+str(helper_string))
			print("helper_string[x_diff] == "+str(helper_string[x_diff]))
			while x_diff != len(helper_string) and helper_string[x_diff] in numbers: # Check if the number continues.
				#x_diff += 1
				print("[neig[0] + x_diff, neig[1]] == "+str([neig[0] + x_diff, neig[1]]))
				print("input_matrix[neig[1]][num_min_x + x_diff] == "+str(input_matrix[neig[1]][num_min_x + x_diff]))
				already_checked.append([num_min_x + x_diff, neig[1]])
				x_diff += 1

			final_num = helper_string[:x_diff]
			print("Final num: "+str(final_num))
			all_nums.add(int(final_num))
			out.append(int(final_num))
			if len(out) > 2:
				return []

	return out



def get_nums(input_matrix: list) -> int:
	# Now check all of the characters and check if they are a special character.
	tot = 0



	for y in range(len(input_matrix)):
		for x in range(len(input_matrix[0])):
			print("("+str(x)+", "+str(y)+")")
			# Now, search for "*"
			char = input_matrix[y][x]
			if char == "*": # We have a gear.
				# Now search for adjacent numbers.
				adjacent_numbers = check_neighbours_nums(input_matrix, x, y)
				print("adjacent_numbers == "+str(adjacent_numbers))
				if len(adjacent_numbers) == 2:
					tot += adjacent_numbers[0] * adjacent_numbers[1]



	'''
	for y in range(len(input_matrix)):
		num_index = None
		#for x in range(len(input_matrix[0])):
		x = 0
		while x != len(input_matrix[0]):
			cur_char = input_matrix[y][x]
			#print("cur_char == "+str(cur_char))
			if cur_char in numbers:
				if num_index == None:

					num_index = x # Mark the start of the number
				# We encountered a number, check the neighbours.
				if check_neighbours(input_matrix, x, y):
					# We have a special character, so convert the number to an integer and add it to the total
					num_thing = input_matrix[y][num_index:]
					if "." in num_thing:
						#print("num_thing == "+str(num_thing))
						for i, char in enumerate(num_thing):
							#print("char == "+str(char))
							if char not in numbers:
								end_index = i
								break
						oof = num_thing[:end_index]
						x = end_index+num_index
						num_thing = int(oof) # Cut off the integer.
					else:
						# We are at the end of the line, so there isn't a "." character so convert the rest of the string to an integer.
						x = len(input_matrix[0])-1
						num_thing = int(num_thing)
					num_index = None
					#print("Number: "+str(num_thing))
					tot += num_thing
			else:
				num_index = None
			#print("x == "+str(x))

			x += 1
	'''

	return tot
def main() -> int:
	input_matrix = parse_input()
	solution = get_nums(input_matrix)
	print("solution: "+str(solution))
	print("all_nums == "+str(all_nums))
	print("531 in all_nums: "+str(531 in all_nums))
	return 0

if __name__=="__main__":
	exit(main())
