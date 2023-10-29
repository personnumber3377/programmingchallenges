
import sys
import pstats
import time
import dis
#def f8_alt(x):
#    return "%14.12f" % x
#pstats.f8 = f8_alt
#PART2 = True
RUN_COUNT = 1000
glob_input = None


OPERATOR_INDEX = 2
OTHER_INDEX = 1
def parse_monkeys() -> dict:
	global glob_input
	if glob_input == None:

		glob_input = sys.stdin.read()
	
	lines = glob_input.split("\n")
	# Each line represents one monkey.
	# Each monkey name is four characters long. The line is of the format aaaa: bbbb + cccc

	out_dict = {}
	types = {}
	#child_monkey_dict = {}
	for line in lines:
		#print("line == "+str(line))
		monkey_name = line[:4]
		expression = line[6:]
		#out_dict[monkey_name] = expression.split(" ")
		#print("expression == "+str(expression))
		if expression.isnumeric():
			out_dict[monkey_name] = [expression]
			types[monkey_name] = 1 # one means number, zero means other expression
			continue
		types[monkey_name] = 0
		#out_dict[monkey_name] = [expression[0:4], expression[5], expression[7:]]
		out_dict[monkey_name] = [expression[0:4], expression[7:], expression[5]]

		#child_monkey_dict[monkey_name] = [expression[0:4], expression[7:]]

	return out_dict, types#, child_monkey_dict


'''
def parse_monkeys() -> dict:
	stdin_input = sys.stdin.read()
	lines = stdin_input.split("\n")
	# Each line represents one monkey.
	# Each monkey name is four characters long. The line is of the format aaaa: bbbb + cccc

	out_dict = {}

	for line in lines:

		monkey_name = line[:4]
		expression = line[6:]
		out_dict[monkey_name] = expression.split(" ")

	return out_dict
'''


def evaluate_monkeys(monkeys: dict, cur_monkey: str) -> int:
	#if cur_monkey == "humn" and PART2:
	#	print("Error!")
	#	exit(1)
	#print("cur_monkey == "+str(cur_monkey))
	
	tokens = monkeys[cur_monkey]
	#print("tokens == "+str(tokens) )
	if len(tokens) == 1:
		token = tokens[0]
		if token.isnumeric():
			return int(token) # plain number
		else:
			#print("token == "+str(token))
			return evaluate_monkeys(monkeys, token)
	else:
		val_1 = evaluate_monkeys(monkeys, tokens[0])
		val_2 = evaluate_monkeys(monkeys, tokens[1])
		op_string = tokens[2]
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


def get_route(monkeys: dict, wanted_monkey: str, moves: list, cur_monkey: str, types: dict):

	if cur_monkey == wanted_monkey:
		#print("Returning moves")
		return moves
	#print("start")
	for monkey in monkeys:
		if types[monkey]:
			continue
		expression = monkeys[monkey]
		if cur_monkey in expression:

			if cur_monkey == expression[0]:
				#print("left")
				return get_route(monkeys, wanted_monkey, [0]+moves, monkey, types)
			else:
				return get_route(monkeys, wanted_monkey, [1]+moves, monkey, types)



'''
def get_route(monkeys: dict, wanted_monkey: str, moves: list, cur_monkey: str, types: dict, child_monkey_dict: dict):

	if cur_monkey == wanted_monkey:
		#print("Returning moves")
		return moves
	#print("start")
	for monkey in monkeys:
		if types[monkey]:
			continue
		expression = monkeys[monkey]

		if cur_monkey == expression[0]:
			#print("left")
			return get_route(monkeys, wanted_monkey, [0]+moves, monkey, types)
		elif cur_monkey == expression[2]:
			return get_route(monkeys, wanted_monkey, [1]+moves, monkey, types)
'''



def get_value(monkeys: dict, route: list):
	if route[0] == 0:
		# The humn leaf is on the left so the other value is on the right side.
		#value_monkey = monkeys["root"].split(" ")[2]

		value_monkey = monkeys["root"][1]
	else:
		# The humn leaf is on the right side, so the other value is on the left side
		#value_monkey = monkeys["root"].split(" ")[0]
		value_monkey = monkeys["root"][0]
	# Calculate lhs

	# def evaluate_monkeys(monkeys: dict, cur_monkey: str) -> int:

	lhs = evaluate_monkeys(monkeys, value_monkey)

	return lhs


def get_monkey_name(monkeys: dict, name: str, move:int):
	expression = monkeys[name]
	if move == 0:
		#return expression.split(" ")[0] # left
		return expression[0]
	else:
		#return expression.split(" ")[2] # right
		return expression[1]


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
	#print("monkey_names == "+str(monkey_names))
	route.pop(0)
	#print("monkey_names == "+str(monkey_names))
	#print("Initial value: "+str(value))
	while cur_name != "humn":
		cur_name = monkey_names[counter]
		# value is lhs
		#
		if cur_name == "humn":
			#print("qqqqqqqqqqqq")
			break
		if route[counter] == 1:
			# humn thing is on the right, so calculate left.
			cor_index = 0
		else:
			# humn is on the left so calculate right
			#cor_index = 2
			cor_index = 1
		tokens = monkeys[cur_name]
		other_monkey_name = tokens[cor_index]

		val_2 = evaluate_monkeys(monkeys, other_monkey_name)

		match tokens[2]: # Match operator and apply the reverse operator
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
				#if value % val_2 != 0:
				#	print("counter == "+str(counter))
				#	print("value % val_2 != 0")
				#	exit(1)
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


def get_monkey_names(monkeys: dict, route: list):

	cur_name = "root"
	monkey_names = ["root"]

	for move in route:
		cur_name = get_monkey_name(monkeys, cur_name, move)
		monkey_names.append(cur_name)
	return monkey_names


def solve_equation(monkeys: dict, types: dict) -> int:
	# First get the route to the humn monkey and reverse it.
	#print(dis.dis("get_route(monkeys, \"root\", [], \"humn\", types)"))
	route = get_route(monkeys, "root", [], "humn", types)
	monkey_names = get_monkey_names(monkeys, route)

	value = get_value(monkeys, route)

	humn_value = traverse_backwards(monkeys, route, value)
	#print("humn_value == "+str(humn_value))
	return humn_value

def main() -> int:
	start_time = time.time()
	for _ in range(RUN_COUNT):

		monkeys, types = parse_monkeys()
		result = solve_equation(monkeys, types)
		#result = evaluate_monkeys(monkeys, "root") # find value of root.
		#print(result)
	end_time = time.time()
	tot_time = end_time - start_time
	print(str(RUN_COUNT)+" runs tooks "+str(tot_time)+ " seconds.")
	print("Average run time was "+str(tot_time / RUN_COUNT)+" seconds.")
	#print("Disassembly of get_route : ")
	#print(dis.dis(get_route))
	return 0

if __name__=="__main__":
	exit(main())
