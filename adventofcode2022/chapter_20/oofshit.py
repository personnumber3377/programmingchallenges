
import sys
import copy
import pickle

TEST = False

COUNTER = 0

DEC_KEY = 811589153


'''


shit = """
1, 2, -3, 3, -2, 0, 4
2, 1, -3, 3, -2, 0, 4
1, -3, 2, 3, -2, 0, 4
1, 2, 3, -2, -3, 0, 4
1, 2, -2, -3, 0, 3, 4
1, 2, -3, 0, 3, 4, -2
1, 2, -3, 0, 3, 4, -2
1, 2, -3, 4, 0, 3, -2
"""
'''



shit = '''
811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612
0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153
0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153
0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459
0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306
0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459
0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459
0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612
0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306
0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306
'''


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
def place(in_list: list, ind_a: int, ind_b, num) -> None: # numbers = place(numbers, a_index, b_index, quotient, num)
	global COUNTER
	global test_out
	# This is here to take care of the loop-around.
	#if in_list[ind_a] == 0:
	#	return in_list
	#print("in_list before: "+str([x[1] for x in in_list]))
	#print("ind_a before == "+str(ind_a))
	#print("ind_b before == "+str(ind_b))
	ind_a = ind_a % (len(in_list))
	
	#elif ind_b == len(in_list) - 1:
	#	ind_b = 0
	#print("in_list[ind_a][1] == "+str(in_list[ind_a][1]))
	if num == 0:

		COUNTER += 1
		#print("poop!")
		#print("poop in_list[ind_a][1] == "+str(in_list[ind_a][1]))
		return in_list
	#print("in_list[ind_a] == "+str(in_list[ind_a]))
	element = in_list.pop(ind_a) # get the element

	ind_b = ind_b % (len(in_list))
	if ind_b == 0:
		ind_b = len(in_list)
	#print("b_index == "+str(ind_b))

	#if ind_b == len(in_list):
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

	#if TEST:
	#	if [x[1] for x in in_list] != test_out[COUNTER+1]:
	#		print("fuck!")
	#		print("test_out[COUNTER] == "+str(", ".join([str(x) for x in test_out[COUNTER+1]])))
	#		print("[x[1] for x in in_list] == "+str([x[1] for x in in_list]))
	#		exit(1)

	COUNTER += 1
	#print("in_list == "+str(in_list))
	#print("in_list == "+str([int(x[1]) for x in in_list]))
	return in_list



def parse_input() -> list:
	return [(i, int(x)*DEC_KEY) for i, x in enumerate(sys.stdin.read().split("\n"))]
	#return [(i, int(x)) for i, x in enumerate(sys.stdin.read().split("\n"))]

def get_numbers(numbers: list):
	#number_vals = [x[1] for x in numbers]
	assert isinstance(numbers, list)

	index_zero = numbers.index(0) # get index of zero
	#print("index_zero == "+str(index_zero))
	res = 0
	for i in range(1,4):
		#print("i == "+str(i))
		#print("numbers[(1000*i) % (len(numbers))] == "+str(numbers[(1000*i+index_zero) % (len(numbers))]))
		#print("numbers[(1000*i+index_zero) % (len(numbers))] == "+str(numbers[(1000*i+index_zero) % (len(numbers))]))
		res += numbers[(1000*i+index_zero) % (len(numbers))]
	return res



def mix(indexes: list, orig_numbers: list) -> list:

	# mixes, but does not take the integers.

	#if len(puzzle_input) == len(set(puzzle_input)):
	#	#print("The numbers only appear once!!!")
	#else:
	#	print("poop")
	#	print("len(puzzle_input) == "+str(len(puzzle_input)))
	#	print("len(set(puzzle_input)) == "+str(len(set(puzzle_input))))
	#	exit(1)

	#orig_numbers = copy.deepcopy(puzzle_input)
	#orig_numbers = copy.deepcopy(puzzle_input)
	#numbers = puzzle_input


	#nums = [numbers[i][1] for i in range(len(numbers))]
	nums = orig_numbers

	#indexes = [x[0] for x in numbers]
	
	#print("1 in indexes == "+str(1 in indexes))
	#print("indexes == "+str(indexes))
	for i, ind_num_pair in enumerate(orig_numbers):

		wanted_index = i
		#print("tag == "+str(wanted_index))


		a_index = indexes.index(wanted_index) # get the numbers index
		num = nums[i]
		#print("n == "+str(num))
		#print("a_index == "+str(a_index))
		#print("indexes == "+str(indexes))
		b_index = a_index + num

		indexes = place(indexes, a_index, b_index, num)


	return indexes


def solve_puzzle(puzzle_input: list) -> int:



	#print("puzzle_input == "+str(puzzle_input))
	orig_numbers = [x[1] for x in puzzle_input] # copy.deepcopy(puzzle_input)
	indexes = [x[0] for x in puzzle_input]
	for i in range(10):
		#print([x[1] for x in puzzle_input])
		if TEST:
			print("Testing!")
			if [orig_numbers[x] for x in indexes] != test_out[i+1]:
				print("Fuck!")
				print("correct: "+str(test_out[i+1]))
				#print("our: "+str([x[1] for x in puzzle_input]))
				print("our: "+str([orig_numbers[x] for x in indexes]))
				exit(1)

		indexes = mix(indexes, orig_numbers)
		

	#print()
	numbers_list = [orig_numbers[x] for x in indexes]
	#print("numbers list final: "+str(numbers_list))
	result = get_numbers(numbers_list)

	#print("result == "+str(result))

	return result
	

def main() -> int:
	puzzle_input = parse_input()
	result = solve_puzzle(puzzle_input)
	print("Solution: "+str(result))
	return 0

if __name__=="__main__":

	exit(main())
