
import sys

def parse_lines() -> list:
	lines = sys.stdin.read().split("\n")
	return lines
def check_num(whole_string: str, index: int) -> bool:
	char = whole_string[index]
	numbers = set("0123456789")
	typed_out_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	assert whole_string != ""
	if char in numbers:
		return char
	for j,string in enumerate(typed_out_numbers):
		if whole_string[index:index+len(string)] == string:
			last_num = str(j+1)
			return last_num
	return False

def get_int(line: str) -> int:
	for i in range(len(line)):
		val = check_num(line, i)
		if val:
			first_num = val
			break
	for i in range(len(line)-1,-1,-1):
		val = check_num(line, i)
		if val:
			last_num = val
			break
	integer = int(first_num+last_num)
	return integer

def solve(lines: list) -> int:
	res = 0
	for line in lines:
		res += get_int(line)
	return res
def main() -> int:
	lines = parse_lines()
	solution = solve(lines)
	print(solution)
	return 0

if __name__=="__main__":
	exit(main())
