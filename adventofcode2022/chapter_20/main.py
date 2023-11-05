
import sys
import copy
import pickle

TEST = False

COUNTER = 0







shit = """
2, 1, -3, 3, -2, 0, 4
1, -3, 2, 3, -2, 0, 4
1, 2, 3, -2, -3, 0, 4
1, 2, -2, -3, 0, 3, 4
1, 2, -3, 0, 3, 4, -2
1, 2, -3, 0, 3, 4, -2
1, 2, -3, 4, 0, 3, -2
"""

out_thing = shit.split("\n")

poopoo = []

for thing in out_thing:
	poopoo.append([int(x) if x != "" else "" for x in thing.split(", ")])

test_out = poopoo
print("fgewgreg")
print(test_out)



'''
def swap(in_list:list, ind_a: int, ind_b: int) -> None:
	a,b = in_list[ind_a], in_list[ind_b]
	in_list[ind_a], in_list[ind_b] = b, a
	return
'''
def place(in_list: list, ind_a: int, ind_b) -> None: # numbers = place(numbers, a_index, b_index, quotient, num)
	global COUNTER
	global test_out
	# This is here to take care of the loop-around.
	#if in_list[ind_a] == 0:
	#	return in_list
	#print("in_list before: "+str([x[1] for x in in_list]))
	#print("ind_a before == "+str(ind_a))
	#print("ind_b before == "+str(ind_b))
	ind_a = ind_a % (len(in_list) - 1)
	
	#elif ind_b == len(in_list) - 1:
	#	ind_b = 0

	element = in_list.pop(ind_a) # get the element

	ind_b = ind_b % (len(in_list))
	if ind_b == 0:
		ind_b = len(in_list)
	#if ind_b == len(in_list) - 1:
	#	ind_b = 0
	#if ind_b > ind_a: # if the target index is larger than the index where it took it from, then we need to decrement the target index, because the elements shift.
	#	ind_b -= 1

	#if ind_b < 0:
	#	exit(1)
	in_list.insert(ind_b,element)

	#print(str(in_list)[1:-1])
	#print("ind_a == "+str(ind_a))
	#print("ind_b == "+str(ind_b))
	#print("in_list after: "+str([x[1] for x in in_list]))

	if TEST:
		if [x[1] for x in in_list] != test_out[COUNTER+1]:
			print("fuck!")
			print("test_out[COUNTER] == "+str(", ".join([str(x) for x in test_out[COUNTER+1]])))
			print("[x[1] for x in in_list] == "+str([x[1] for x in in_list]))
			exit(1)

	COUNTER += 1
	#print("in_list == "+str(in_list))
	return in_list



def parse_input() -> list:
	return [(i, int(x)) for i, x in enumerate(sys.stdin.read().split("\n"))]


def get_numbers(numbers: list):
	number_vals = [x[1] for x in numbers]
	assert isinstance(numbers, list)

	index_zero = [x[1] for x in numbers].index(0) # get index of zero
	#print("index_zero == "+str(index_zero))
	res = 0
	for i in range(1,4):
		#print("i == "+str(i))
		#print("numbers[(1000*i) % (len(numbers))] == "+str(numbers[(1000*i+index_zero) % (len(numbers))]))
		print("number_vals[(1000*i+index_zero) % (len(numbers))] == "+str(number_vals[(1000*i+index_zero) % (len(numbers))]))
		res += number_vals[(1000*i+index_zero) % (len(numbers))]
	return res


def solve_puzzle(puzzle_input: list) -> int:



	#print("puzzle_input == "+str(puzzle_input))

	if len(puzzle_input) == len(set(puzzle_input)):
		print("The numbers only appear once!!!")
	else:
		print("poop")
		print("len(puzzle_input) == "+str(len(puzzle_input)))
		print("len(set(puzzle_input)) == "+str(len(set(puzzle_input))))
		exit(1)

	orig_numbers = copy.deepcopy(puzzle_input)
	numbers = puzzle_input


	nums = [numbers[i][1] for i in range(len(numbers))]

	indexes = [x[0] for x in numbers]

	for i, ind_num_pair in enumerate(orig_numbers):

		wanted_index = i

		a_index = indexes.index(wanted_index) # get the numbers index

		#num = numbers[a_index][1] # the actual value
		num = nums[a_index]
		#if numbers[i] != num:

		#a_index = numbers.index(num)

		#else:
		#	a_index = i # assume that the element is not moved.

		b_index = a_index + num

		# swap


		numbers = place(indexes, a_index, b_index)



		#print("The numbers array after mixing: "+str(numbers))

	fh = open("binary.bin", "wb+")
	pickle.dump(numbers, fh)
	fh.close()

	result = get_numbers(numbers)

	print("result == "+str(result))

	return 0
	

def main() -> int:
	puzzle_input = parse_input()
	result = solve_puzzle(puzzle_input)
	print("Solution: "+str(result))
	return 0

if __name__=="__main__":

	exit(main())
