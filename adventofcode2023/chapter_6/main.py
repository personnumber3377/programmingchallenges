import sys
import math

PART = 2

def parse_input() -> list:
	if PART == 1:

		stdin_lines = sys.stdin.read().split("\n")
		# Thanks to https://stackoverflow.com/a/4289557
		times = [int(s) for s in stdin_lines[0].split() if s.isdigit()]
		distances = [int(s) for s in stdin_lines[1].split() if s.isdigit()]
	elif PART == 2:
		nums = set("0123456789")
		stdin_lines = sys.stdin.read().split("\n")
		time_string = [x for x in stdin_lines[0] if x in nums]
		distance_string = [x for x in stdin_lines[1] if x in nums]
		return [int(''.join(time_string))], [int(''.join(distance_string))]
	else:
		print("Invalid puzzle part number: "+str(PART)+"!")
		exit(1)

	return times, distances

def get_sols(distance: int, time: int) -> tuple:
	sol1 = 1/2*(time - math.sqrt(time**2 - 4*distance)) # see https://www.wolframalpha.com/input?i=solve+c+*+%28t+-+c%29+%3D+d+for+c
	sol2 = 1/2*(time + math.sqrt(time**2 - 4*distance))
	print("sol1 == "+str(sol1))
	print("sol2 == "+str(sol2))
	if sol1.is_integer():
		sol1 += 1
	if sol2.is_integer():
		sol2 -= 1
	return math.ceil(sol1), math.floor(sol2)

def get_possible_charge_times(times: list, distances: list) -> tuple:
	# Dummy
	out = 1
	for time, distance in zip(times, distances):
		# Get min time and max time.
		min_time, max_time = get_sols(distance, time)
		# Now multiply the output, by the amount of integer solutions.
		print("amount of solutions: "+str(max_time - min_time + 1))
		out *= max_time - min_time + 1

	return out
		

def main() -> None:
	times, distances = parse_input()
	solution = get_possible_charge_times(times, distances)
	print(solution)
	return 0
if __name__=="__main__":
	exit(main())