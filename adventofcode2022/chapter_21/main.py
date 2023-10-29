
import sys

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
				assert val_1 % val_2 == 0
				return (val_1 // val_2)
			case _:
				print("Invalid operation for monkey "+str(monkey_name)+" : "+str(op_string))
				exit(1)









def main() -> int:

	monkeys = parse_monkeys()

	result = evaluate_monkeys(monkeys, "root") # find value of root.
	print(result)
	return 0

if __name__=="__main__":
	exit(main())
