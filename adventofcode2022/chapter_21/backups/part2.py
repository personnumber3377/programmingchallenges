
import sys

PART2 = True

def parse_monkeys() -> dict:
	stdin_input = sys.stdin.read()
	lines = stdin_input.split("\n")
	# Each line represents one monkey.
	# Each monkey name is four characters long. The line is of the format aaaa: bbbb + cccc

	out_dict = {}

	for line in lines:

		monkey_name = line[:4]
		expression = line[6:]
		out_dict[monkey_name] = expression

	return out_dict

def evaluate_monkeys(monkeys: dict, cur_monkey: str) -> int:
	if cur_monkey == "humn" and PART2:
		print("Error!")
		exit(1)
	expression = monkeys[cur_monkey]

	# get tokens
	tokens = expression.split(" ")
	print("tokens == "+str(tokens))
	# check if expression represents a single number or other monkey

	if len(tokens) == 1:
		
		token = tokens[0]
		
		if token.isnumeric():

			return int(token) # plain number

		else:

			# assume monkey name

			return evaluate_monkeys(monkeys, token)

	else:
		# assume three tokens
		assert len(tokens) == 3

		# Judging by the input, it appears that each expression only has monkeys names as parameters, not constants, so we do not need to worry about the other operand being an immediate value. :)

		print("tokens[0] == "+str(tokens[0]))
		print("tokens[1] == "+str(tokens[1]))
		val_1 = evaluate_monkeys(monkeys, tokens[0])
		val_2 = evaluate_monkeys(monkeys, tokens[2])

		op_string = tokens[1]

		match op_string:
			case "+":
				return val_1 + val_2
			case "-":
				return val_1 - val_2
			case "*":
				return val_1 * val_2
			case "/":
				return (val_1 // val_2)
			case _:
				print("Invalid operation for monkey "+str(monkey_name)+" : "+str(op_string))
				exit(1)


all_things = {}

def get_route(monkeys: dict, wanted_monkey: str, moves: list, cur_monkey: str):

	if cur_monkey == wanted_monkey:
		print("Returning moves")
		return moves
	print("start")
	for monkey in monkeys.keys():

		expression = monkeys[monkey]
		print("wanted_monkey == "+str(wanted_monkey))
		print("expression == "+str(expression))
		print("cur_monkey == "+str(cur_monkey))
		print("monkey == "+str(monkey))

		# 
		tokens = expression.split(" ")
		if cur_monkey in expression:
			print("poopooooo")
			#tokens = expression.split(" ")
			if cur_monkey == tokens[0]:
				print("left")
				return get_route(monkeys, wanted_monkey, [0]+moves, monkey)
			elif cur_monkey == tokens[2]:
				return get_route(monkeys, wanted_monkey, [1]+moves, monkey)
				print("shit")
			else:
				print("Fuck!")
				print("wanted_monkey == "+str(wanted_monkey))
				exit(1)
				#return None
	print("end")
	return None

'''
def get_route(monkeys: dict, wanted_monkey: str, moves: list, cur_monkey: str):

	# this is a recursive function which tries to find the route from the root of the tree to a certain node / leaf of the tree.

	# first check if this is the wanted leaf

	if cur_monkey == wanted_monkey:
		return moves # Return the current route which we took to get here.

	expression = monkeys[cur_monkey]
	tokens = expression.split(" ")
	# Check if current leaf is a terminal leaf (aka a number)

	if tokens[0].isnumeric():
		return None # No path found yet
	else:
		assert len(tokens) == 3
		# first check if the left branch (the left operand so to speak) has the wanted leaf.

		left_monkey = tokens[0]
		right_monkey = tokens[2]
		#print("wanted_monkey == "+str(wanted_monkey))
		#print("tokens == "+str(tokens))

		print("moves == "+str(moves))

		#if str(tokens) in all_things:
		#	print("oof")
		#	exit(1)
		all_things[str(tokens)] = 1
		if get_route(monkeys, wanted_monkey, moves, left_monkey) != None:
			#print("(monkeys, wanted_monkey, moves, left_monkey) == "+str((monkeys, wanted_monkey, moves, left_monkey)))
			# We found it in the left branch. Return the current moves list with left appended at the end.
			return get_route(monkeys, wanted_monkey, moves+[0], left_monkey)+[0] # Zero means left
		elif get_route(monkeys, wanted_monkey, moves, right_monkey) != None:
			return get_route(monkeys, wanted_monkey, moves+[1], right_monkey)+[1] # One means right
		else:
			#print("Wanted monkey not found in the binary tree!")
			#exit(1)

			return None
'''

def get_value(monkeys: dict, route: list):
	if route[0] == 0:
		# The humn leaf is on the left so the other value is on the right side.
		value_monkey = monkeys["root"].split(" ")[2]
	else:
		# The humn leaf is on the right side, so the other value is on the left side
		value_monkey = monkeys["root"].split(" ")[0]

	# Calculate lhs

	# def evaluate_monkeys(monkeys: dict, cur_monkey: str) -> int:

	lhs = evaluate_monkeys(monkeys, value_monkey)

	return lhs


def get_monkey_name(monkeys: dict, name: str, move:int):
	expression = monkeys[name]
	if move == 0:
		return expression.split(" ")[0] # left
	else:
		return expression.split(" ")[2] # right

def traverse_backwards(monkeys, route, value):

	# This function traverses the binary tree backwards to get the appropriate value for humn.

	# First get the monkey names which we traverse along to get to humn.

	cur_name = "root"
	monkey_names = ["root"]

	for move in route:
		cur_name = get_monkey_name(monkeys, cur_name, move)
		monkey_names.append(cur_name)

	#print("Monkey names which we traverse to get to humn: "+str(monkey_names))

	# reverse route and the monkey names along that route

	#monkey_names.reverse()
	#route.reverse()

	cur_name = "root"
	counter = 0
	monkey_names.pop(0)
	print("monkey_names == "+str(monkey_names))
	route.pop(0)
	print("monkey_names == "+str(monkey_names))
	print("Initial value: "+str(value))
	while cur_name != "humn":
		cur_name = monkey_names[counter]
		# value is lhs
		#
		if cur_name == "humn":
			print("qqqqqqqqqqqq")
			break
		if route[counter] == 1:
			# humn thing is on the right, so calculate left.
			cor_index = 0
		else:
			# humn is on the left so calculate right
			cor_index = 2

		print("cur_name == "+str(cur_name))

		tokens = monkeys[cur_name].split(" ")
		print("tokens == "+str(tokens))
		other_monkey_name = tokens[cor_index]
		# get the value of the other monkey:
		assert other_monkey_name not in monkey_names
		val_2 = evaluate_monkeys(monkeys, other_monkey_name)

		# Now apply the reverse operation to the left hand side

		print("tokens[1] == "+str(tokens[1]))
		print("value == "+str(value))
		match tokens[1]: # Match operator and apply the reverse operator
			case "+":
				value = value - val_2
			case "-":
				# Same as with division:

				if cor_index == 0:

					# Humn thing is on the right aka value = aaaa - humn => humn = aaaa - value
					value = val_2 - value
				else:
					# Humn thing is on the left, so value = humn - aaaa => humn = value + aaaa

					value = value + val_2
				
			case "*":
				# sanity check
				if value % val_2 != 0:
					print("counter == "+str(counter))
					print("value % val_2 != 0")
					exit(1)
				value = value // val_2
			case "/":

				if cor_index == 0:
					# Left is constant, so the divisor is actually the human thing. value = x / humn => humn = value / x
					value = value / val_2
				else:
					# Right is constant, so just multiply by val_2
					value = (value * val_2)
			case _:
				print("Invalid operation for monkey "+str(monkey_name)+" : "+str(op_string))
				exit(1)
		counter += 1

	return value






'''

cur_name = "root"
	monkey_names = ["root"]

	for move in route:
		cur_name = get_monkey_name(monkeys, cur_name, move)
		monkey_names.append(cur_name)

'''

def get_monkey_names(monkeys: dict, route: list):

	cur_name = "root"
	monkey_names = ["root"]

	for move in route:
		cur_name = get_monkey_name(monkeys, cur_name, move)
		monkey_names.append(cur_name)
	return monkey_names


def solve_equation(monkeys: dict) -> int:
	# First get the route to the humn monkey and reverse it.

	route = get_route(monkeys, "root", [], "humn")
	print("route == "+str(route))
	monkey_names = get_monkey_names(monkeys, route)
	#route.reverse()
	print("="*30)
	print("All of the monkeys: ")
	print(str(monkey_names))
	print("="*30)


	value = get_value(monkeys, route)

	humn_value = traverse_backwards(monkeys, route, value)
	print("humn_value == "+str(humn_value))
	return route

def main() -> int:

	monkeys = parse_monkeys()
	result = solve_equation(monkeys)
	#result = evaluate_monkeys(monkeys, "root") # find value of root.
	print(result)
	return 0

if __name__=="__main__":
	exit(main())
