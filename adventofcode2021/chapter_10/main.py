
import sys


PART = 2

def part1(lines: list) -> int:
	# Set the result counter to zero initially:
	res = 0
	'''
	): 3 points.
	]: 57 points.
	}: 1197 points.
	>: 25137 points.
	'''
	points = {")":3,"]":57,"}":1197,">":25137} # score lookup

	correct_tags = {"<":">","(":")","[":"]","{":"}"} # these are what the closers should be
	#incomplete_strings = []
	for line in lines:
		assert line[0] not in points.keys() # assume first char is not closing tag
		#invalid = False
		cur_call_stack = [line[0]] # get first character from string
		for char in line[1:]:
			if char in points.keys():
				# we are closing
				if char != correct_tags[cur_call_stack[-1]]:
					# fail
					res += points[char]
					#print("char == "+str(char))
					#invalid = True
					break
				else:
					# we closed correctly so just pop the last thing:
					cur_call_stack.pop(-1)
			else:
				# not a closing character, so append it to the call stack
				cur_call_stack.append(char)
		#if not invalid:
		#	incomplete_strings.append(tuple((line, cur_call_stack)))

	# Now we have gotten rid of the invalid strings.


	return res # placeholder


def get_score_part2(char_list: list) -> int:
	res = 0
	#print("char_list == "+str(char_list))
	points = {")":1,"]":2,"}":3,">":4}
	multiplier = 5
	for char in char_list:
		res *= multiplier
		res += points[char]
	#print(res)
	return res


def part2(lines: list) -> int:
	# Set the result counter to zero initially:
	res = 0
	'''
	): 3 points.
	]: 57 points.
	}: 1197 points.
	>: 25137 points.
	'''
	points = {")":3,"]":57,"}":1197,">":25137} # score lookup

	correct_tags = {"<":">","(":")","[":"]","{":"}"} # these are what the closers should be
	points_keys = points.keys()
	incomplete_strings = []
	for line in lines:
		invalid = False
		cur_call_stack = []
		for char in line:
			if char in points_keys:
				# we are closing
				if char != correct_tags[cur_call_stack[-1]]:
					# fail
					invalid = True
					break
				else:
					# we closed correctly so just pop the last thing:
					cur_call_stack.pop(-1)
			else:
				# not a closing character, so append it to the call stack
				cur_call_stack.append(char)
		if not invalid:
			incomplete_strings.append(cur_call_stack)

	# Now we have gotten rid of the invalid strings and we need to fix them. This is done by just checking the correct 
	
	point_list = []

	for call_stack in incomplete_strings:



		call_stack.reverse() # we need to go from the end to the start, because that way we close them correctly
		completion_string = [correct_tags[x] for x in call_stack]
		#print("completion_string: "+str(completion_string))
		res = get_score_part2(completion_string)
		point_list.append(res)

	point_list = sorted(point_list)
	#assert len(point_list) % 2 == 1 # it must be odd length


	return point_list[len(point_list)//2]
	#return res # placeholder






def parse_input() -> list:

	input_str = sys.stdin.read()
	lines = input_str.split("\n")
	return lines

def main() -> int:
	input_lines = parse_input()
	if PART == 1:

		res = part1(input_lines)
	elif PART == 2:
		res = part2(input_lines)
	else:
		print("Invalid puzzle part number: "+str(PART))
		exit(1)
	print(res)
	return 0

if __name__=="__main__":
	exit(main())
