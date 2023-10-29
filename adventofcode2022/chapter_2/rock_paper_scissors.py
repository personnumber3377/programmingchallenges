
import sys

def generate_move_tuples() -> dict:
	# Precomputed moves and scores:
	output = { ("A","X"): 1+3, ("A","Y"): 2+6, ("A", "Z"): 3+0, ("B", "X"): 1+0, ("B","Y"): 2+3, ("B","Z"): 3+6, ("C","X"): 1+6, ("C","Y"): 2+0, ("C","Z"): 3+3 }
	return output





def rps_one() -> int:
	lines = sys.stdin.buffer.read().decode("ascii").split("\n")
	move_dict = generate_move_tuples()
	score = 0
	for line in lines:
		moves = tuple(line.split(" "))
		score += move_dict[moves]
	return score

def rps_two() -> int:
	lines = sys.stdin.buffer.read().decode("ascii").split("\n")
	tot_score = 0
	for line in lines:
		a,b = line.split(" ")
		a = ord(a)-65 # 65 is the ascii code for "A"
		b = ord(b)-88 # 88 is the ascii code for "X"
		# Here are the equations which we came up with.
		tot_score += (( a + 2 + b ) % 3 + 1) + 3 * b
	return tot_score

if __name__=="__main__":
	print("Solution to part two: "+str(rps_two()))
	exit(0)
