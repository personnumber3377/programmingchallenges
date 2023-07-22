
import sys
from colorist import Color
import ast
from functools import cmp_to_key, reduce
import copy



# Do you want to enable debug mode?

DEBUG = True

def good(string):
	print(f"{Color.GREEN}[+] {string}{Color.OFF}")

def fatal(string, exit_code=1):
	print(f"{Color.RED}[!] {string}{Color.OFF}")
	exit(exit_code)

def info(string):
	print(f"{Color.BLUE}[*] {string}{Color.OFF}")
	

def debug(string):
	if DEBUG:
		print(f"{Color.YELLOW}[?] {string}{Color.OFF}")


def handle_input():

	# sys.stdin.readlines() reads all lines supplied to stdin to a singular string.

	lines = sys.stdin.readlines()

	# sanity check. every third line should be an empty line (aka just a newline)

	assert len(lines) % 3 == 2 # last newline does not exist therefore this is two


	while "\n" in lines:
		lines.remove("\n")

	assert "\n" not in lines # empty lines should not be in lines

	return_list = []

	assert len(lines) % 2 == 0


	for i in range(len(lines)//2):

		new_list = [ast.literal_eval(lines[i*2]), ast.literal_eval(lines[i*2+1])]
		return_list.append(new_list)

	debug("return_list == "+str(return_list))

	return return_list

def handle_input2():

	# sys.stdin.readlines() reads all lines supplied to stdin to a singular string.

	lines = sys.stdin.readlines()

	# sanity check. every third line should be an empty line (aka just a newline)

	assert len(lines) % 3 == 2 # last newline does not exist therefore this is two


	while "\n" in lines:
		lines.remove("\n")

	assert "\n" not in lines # empty lines should not be in lines

	return_list = []

	assert len(lines) % 2 == 0


	for i in range(len(lines)):

		new_list = [ast.literal_eval(lines[i])]
		return_list.append(new_list)

	debug("return_list == "+str(return_list))
	debug("len(return_list) == "+str(len(return_list)))
	return return_list

def in_order_wrapper(x1,x2):
	res = in_order([x1,x2])
	if res == None:
		fatal("in_order somehow returned None?")
	if res == True:
		return 1
	elif res == False:
		return -1
	return res

def in_order(pair):

	# If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
	
	l1 = pair[0]
	l2 = pair[1]

	if isinstance(l1, int) and isinstance(l2, int):
		debug("int, int")
		if l1 < l2: # If the left integer is lower than the right integer, the inputs are in the right order.
			return True
		elif l1 > l2:
			return False
		else:
			return None # continue

	'''
	If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
	'''

	debug("l1 == "+str(l1))
	debug("l2 == "+str(l2))

	if isinstance(l1, list) and isinstance(l2, list):
		debug("list, list")
		if len(l2) < len(l1):
			for i in range(len(l2)):
				result = in_order([l1[i], l2[i]])
				if result != None:
					return result
			return False # automatically out of order. No need to even compare. "If the right list runs out of items first, the inputs are not in the right order."
		
		elif len(l1) < len(l2):
			# "If the left list runs out of items first, the inputs are in the right order."
			for i in range(len(l1)):
				result = in_order([l1[i], l2[i]])
				if result != None:
					return result
			return True

		else:
			# If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
			for i in range(len(l1)):
				result = in_order([l1[i], l2[i]])
				if result != None:
					return result
			return None

	# If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].

	if isinstance(l1, list) and isinstance(l2, int):
		debug("list, int")
		return in_order([l1, [l2]])

	if isinstance(l1, int) and isinstance(l2, list):
		debug("int, list")
		return in_order([[l1], l2])

	fatal("Does not match any case!")

def solve(list_pairs):
	x = 0
	for index, pair in enumerate(list_pairs):
		if in_order(pair):
			debug("Index "+str(index+1)+" is in order.")
			x += index+1
	return x


def check_sorted(list_thing):
	for i in range(len(list_thing)-1):
		if not in_order_wrapper(list_thing[i], list_thing[i+1]):
			return False
	return True

'''

def bin_sort(list_thing):


	while not check_sorted(list_thing):

'''




def solve2(list_thing):
	#list_thing.sort()
	
	list_thing += [[[2]], [[6]]]

	debug("List thing before: "+str(list_thing))

	orig_list = copy.deepcopy(list_thing)

	list_thing.sort(key=cmp_to_key(in_order_wrapper), reverse=True)
	if not check_sorted(list_thing):
		fatal("List thing not sorted after sorting!")
	x = 1
	for i, k in enumerate(list_thing):
		if k == [[2]] or k == [[6]]:
			debug("Index "+str(i+1)+" is marker!")
			x *= i+1


	debug("List thing after: "+str(list_thing))

	if list_thing == orig_list:
		fatal("Original list is somehow same as sorted list!")


	return x

def solve_puzzle1():
	
	list_stuff = handle_input()

	good("Handled input succesfully!")

	answer = solve(list_stuff)

	return answer

def solve_puzzle2():
	
	list_stuff = handle_input2()

	good("Handled input succesfully!")

	answer = solve2(list_stuff)

	return answer


if __name__=="__main__":
	#print(solve_puzzle())
	#good("Solution to puzzle is: "+str(solve_puzzle1())+" !")
	good("Solution to puzzle is: "+str(solve_puzzle2())+" !")
	exit(0)

