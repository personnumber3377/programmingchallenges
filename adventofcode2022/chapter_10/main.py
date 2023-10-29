
import sys
import numpy as np
#from PIL import Image



'''

Thanks to https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image

from PIL import Image
import numpy as np

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()


'''

def render_matrix(matrix: np.array) -> None:

	#w = matrix.shape[0]
	#h = matrix.shape[1]
	# Thanks to https://pillow.readthedocs.io/en/stable/handbook/concepts.html ! 
	# array = ((array) * 255).astype(np.uint8)
	print("Matrix inside render_matrix: "+str(matrix))
	matrix = (matrix).astype(bool)
	matrix = ((matrix) * 255).astype(np.uint8)

	img = Image.fromarray(matrix)
	#display(img)
	img.show()



DEBUG= True
TEST_1 = False
def debug(string: str):
	if DEBUG:
		print("[DEBUG] "+str(string))


def parse_input() -> list:

	stdin_input = sys.stdin.read()
	lines = stdin_input.split("\n")
	
	out = []

	for line in lines:
		if line[0] == "n":
			# nop
			out.append([0])
		else:
			# assume addx
			#print("line.split(" ") == "+str(line.split(" ")))
			#print("line == "+str(line))
			out.append([1, int(line.split(" ")[1])])
	return out



def check_cycle(x,cur_cycle, result, rip=None): # This is if we want to add to the result.
	if (cur_cycle - 20) % 40 == 0:

		return cur_cycle + 1, result + (cur_cycle * x)
	else:
		return cur_cycle + 1, result


def run_program(program: list) -> int:

	rip = 0

	x = 1

	#result_list = []
	result = 0
	cur_cycle = 1

	while rip != len(program):

		instruction = program[rip] # Fetch

		if instruction[0]:

			# addx instruction
			cur_cycle,result = check_cycle(x,cur_cycle,result,rip=rip)
			cur_cycle,result = check_cycle(x,cur_cycle,result,rip=rip) # x is unmodified for the first two clock cycles, then gets incremented.
			x += instruction[1]

			
		else:
			# assume nop
			cur_cycle,result = check_cycle(x,cur_cycle,result,rip=rip)
			#cur_cycle,result = check_cycle(x,cur_cycle,result) # advance the clock for two cycles.

		rip += 1

	if TEST_1:
		assert x == -1


	return result




def check_cycle_part2(x, cur_cycle, screen_mat, scan_x, scan_y): # This is if we want to add to the result.
	
	# screen_mat, cur_cycle = check_cycle_part2(x,cur_cycle,screen_mat)


	# First draw.

	#pixel = 0

	#if abs(x - scan_x) < 2:
	#	pixel = 1
	#	#debug("poopoo")

	#pixel = x in range(scan_x-1, scan_x+2)
	pixel = abs(x - scan_x) < 2
	#print("x == "+str(x))
	#print("scan_x == "+str(scan_x))
	screen_mat[scan_y][scan_x] = pixel

	#assert scan_y < 7
	#assert scan_x < 41
	#print("scan_y == "+str(scan_y))
	#print("scan_x == "+str(scan_x))
	#debug("screen_mat == "+str(screen_mat))
	#cur_cycle += 1

	scan_x += 1
	if scan_x == 40:
		scan_x = 0
		scan_y += 1

	return screen_mat, cur_cycle + 1, scan_x, scan_y


def run_program_part2(program: list) -> int:
	rip = 0
	x = 1
	screen_mat = np.zeros((6,40)) # 40px wide and 6px high
	scan_y = 0
	scan_x = 0
	cur_cycle = 1
	length = len(program)

	for instruction in program:
		#screen_mat, cur_cycle, scan_x, scan_y = check_cycle_part2(x,cur_cycle,screen_mat, scan_x, scan_y)
		pixel = abs(x - scan_x) < 2
		#pixel = scan_x in range(x-1, x+2)
		screen_mat[scan_y][scan_x] = pixel
		if scan_x == 39:
			scan_x = 0
			scan_y += 1
		else:
			scan_x += 1
		cur_cycle += 1
		#return screen_mat, cur_cycle + 1, scan_x, scan_y

		if instruction[0]:
			#screen_mat, cur_cycle, scan_x, scan_y = check_cycle_part2(x,cur_cycle,screen_mat, scan_x, scan_y)

			pixel = abs(x - scan_x) < 2
			#pixel = (x)&(0xffffffff >> 1) < 2
			#pixel = scan_x in range(x-1, x+2)
			screen_mat[scan_y][scan_x] = pixel
			#scan_x += 1
			if scan_x == 39:
				scan_x = 0
				scan_y += 1
			else:
				scan_x += 1

			cur_cycle += 1

			x += instruction[1]	

	return screen_mat

RUN_COUNT = 10000

def solve_puzzle() -> int:

	program = parse_input()
	#debug("program == "+str(program))
	for _ in range(RUN_COUNT):
		res = run_program_part2(program)

	return res


def main() -> int:

	solution = solve_puzzle()
	#print("Solution")
	#print(str(solution))

	#render_matrix(solution)
	return 0


if __name__=="__main__":

	exit(main())
