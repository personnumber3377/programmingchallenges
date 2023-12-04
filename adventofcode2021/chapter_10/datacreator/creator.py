
import random

PREFERRED_LENGTH = 1000
CLOSE_CHANCE = 0.2

OPEN_BRACKETS = ["<", "{", "[", "("]
CLOSE_BRACKETS = {"<":">", "{":"}", "[":"]", "(":")"}

def generate_line(length: int) -> str:
	# This generates one test case

	complete_string = ""
	call_stack = []

	while len(complete_string) != length:

		# Check if we should open or close
		if random.random() < CLOSE_CHANCE and complete_string != "" and call_stack != []: # Can not close if the very first thing
			# Close.
			complete_string += call_stack[-1]
			call_stack.pop(-1)
		else:
			# Open new bracket
			thing = random.choice(list(CLOSE_BRACKETS.keys()))
			complete_string += thing
			call_stack.append(CLOSE_BRACKETS[thing])

	#print(complete_string)
	return complete_string


def main() -> int:
	count = 10000
	for _ in range(count):
		print(generate_line(PREFERRED_LENGTH))
	return 0


if __name__=="__main__":

	exit(main())
