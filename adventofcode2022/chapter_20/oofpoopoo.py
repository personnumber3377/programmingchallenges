
import sys
import copy
'''
def swap(in_list:list, ind_a: int, ind_b: int) -> None:
	a,b = in_list[ind_a], in_list[ind_b]
	in_list[ind_a], in_list[ind_b] = b, a
	return
'''
def place(in_list: list, ind_a: int, ind_b: int, over_reach: int) -> None: # numbers = place(numbers, a_index, b_index, quotient, num)
	#elem = in_list.pop(ind_a)
	elem = in_list[ind_a]
	# if the index where we put the element is larger than ind_a, then the index where we want to put this element is decremented by one, because the elements shifted one to the left during the pop.
	#print("elem == "+str(elem))
	print("list before: "+str(in_list))
	print("ind_a == "+str(ind_a))
	print("ind_b == "+str(ind_b))

	'''
	if ind_a < ind_b:

		in_list.insert(ind_b, elem)

	else:

		# if the index is less, then just do it the typical way.

		in_list.insert(ind_b, elem)
	'''

	if ind_b == 0:
		ind_b = len(in_list)-1
	print("in_list[:ind_b+1] == "+str(in_list[:ind_b+1]))
	print("in_list[ind_b+1:] == "+str(in_list[ind_b+1:]))
	print("elem == "+str(elem))
	in_list = in_list[:ind_b+1]+[elem]+in_list[ind_b+1:]
	print("in_list == "+str(in_list))
	print("ind_b % (len(in_list)-1) == "+str(ind_b % (len(in_list)-1)))
	if ind_b % (len(in_list)-1) > ind_a:
		# The index where we placed the element is larger than the place where we took it from so we can safely remove the original index
		assert in_list[ind_a] == elem
		print("in_list 3333 == "+str(in_list))
		print("ind_a == "+str(ind_a))
		in_list.pop(ind_a)
		assert in_list[ind_b] == elem
	else:
		assert in_list[ind_a+1] == elem
		in_list.pop(ind_a+1)
		assert in_list[ind_b] == elem

	print("list after: "+str(in_list))

	return in_list



def parse_input() -> list:
	return [int(x) for x in sys.stdin.read().split("\n")]

def solve_puzzle(puzzle_input: list) -> int:



	print("puzzle_input == "+str(puzzle_input))

	if len(puzzle_input) == len(set(puzzle_input)):
		print("The numbers only appear once!!!")

	orig_numbers = copy.deepcopy(puzzle_input)
	numbers = puzzle_input
	length = len(orig_numbers)
	for i, num in enumerate(orig_numbers):

		if numbers[i] != num:
			a_index = numbers.index(num)
		else:
			a_index = i # assume that the element is not moved.

		b_index = (a_index + num) % (length - 1)

		# swap


		numbers = place(numbers, a_index, b_index)



		print("The numbers array after mixing: "+str(numbers))

	return 0
	

def main() -> int:
	puzzle_input = parse_input()
	result = solve_puzzle(puzzle_input)
	print("Solution: "+str(result))
	return 0

if __name__=="__main__":

	exit(main())
