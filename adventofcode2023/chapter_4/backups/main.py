
import sys

def parse_input() -> list:
	# Get the scratchcards. (the numbers on the left of "|" are the winning numbers)
	stdin_input_lines = sys.stdin.read().split("\n")
	out = []
	for line in stdin_input_lines:
		numbers = line[line.index(":")+2:]
		#winning_numbers, our_numbers = [(int(y) if y != "" for y in x.split(" ")) for x in numbers.split("|")]
		
		winning_stuff, our_numbers_stuff = numbers.split("|")

		#print(list(winning_stuff))
		#print(list(our_numbers_stuff))
		winning_numbers = winning_stuff[:-1].split(" ")
		our_numbers = our_numbers_stuff[1:].split(" ")
		#print(winning_numbers)
		#print(our_numbers)
		our_numbers = set(our_numbers)

		out.append([winning_numbers, our_numbers])

	return out

def solve(scratchcards: list) -> int:
	# Now get the winning amounts of numbers for each line.
	
	tot_score = 0
	print("scratchcards == "+str(scratchcards))
	for winning_numbers, actual_numbers in scratchcards:
		power = 0
		# Now just get how many of the winning numbers are in the actual_numbers and that is the score basically.
		for num in winning_numbers:
			if num == "":
				continue
			if num in actual_numbers:
				power += 1
				print("num == "+str(num))
		if power != 0:
			score = 2**(power-1)
			print("score == "+str(score))
			tot_score += score
	return tot_score

def main() -> int:
	scratchcards = parse_input()
	result = solve(scratchcards)
	print(result)
	return 0

if __name__=="__main__":
	exit(main())
