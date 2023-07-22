


ex_string = '''Initial state:
#E######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#

Minute 1, move down:
#.######
#E>3.<.#
#<..<<.#
#>2.22.#
#>v..^<#
######.#

Minute 2, move down:
#.######
#.2>2..#
#E^22^<#
#.>2.^>#
#.>..<.#
######.#

Minute 3, wait:
#.######
#<^<22.#
#E2<.2.#
#><2>..#
#..><..#
######.#

Minute 4, move up:
#.######
#E<..22#
#<<.<..#
#<2.>>.#
#.^22^.#
######.#

Minute 5, move right:
#.######
#2Ev.<>#
#<.<..<#
#.^>^22#
#.2..2.#
######.#

Minute 6, move right:
#.######
#>2E<.<#
#.2v^2<#
#>..>2>#
#<....>#
######.#

Minute 7, move down:
#.######
#.22^2.#
#<vE<2.#
#>>v<>.#
#>....<#
######.#

Minute 8, move left:
#.######
#.<>2^.#
#.E<<.<#
#.22..>#
#.2v^2.#
######.#

Minute 9, move up:
#.######
#<E2>>.#
#.<<.<.#
#>2>2^.#
#.v><^.#
######.#

Minute 10, move right:
#.######
#.2E.>2#
#<2v2^.#
#<>.>2.#
#..<>..#
######.#

Minute 11, wait:
#.######
#2^E^2>#
#<v<.^<#
#..2.>2#
#.<..>.#
######.#

Minute 12, move down:
#.######
#>>.<^<#
#.<E.<<#
#>v.><>#
#<^v^^>#
######.#

Minute 13, move down:
#.######
#.>3.<.#
#<..<<.#
#>2E22.#
#>v..^<#
######.#

Minute 14, move right:
#.######
#.2>2..#
#.^22^<#
#.>2E^>#
#.>..<.#
######.#

Minute 15, move right:
#.######
#<^<22.#
#.2<.2.#
#><2>E.#
#..><..#
######.#

Minute 16, move right:
#.######
#.<..22#
#<<.<..#
#<2.>>E#
#.^22^.#
######.#

Minute 17, move down:
#.######
#2.v.<>#
#<.<..<#
#.^>^22#
#.2..2E#
######.#

Minute 18, move down:
#.######
#>2.<.<#
#.2v^2<#
#>..>2>#
#<....>#
######E#'''


import numpy as np
from PIL import Image



def render_mat(mat):

	qr_matrix = np.invert(mat.astype(bool), dtype=bool)
	print(qr_matrix.astype(int))
	qr_matrix = qr_matrix.astype(np.uint8)
	im = Image.fromarray(qr_matrix * 255)
	im.show()

def render_stuff(things, size):

	matrix = np.zeros((size,size))

	for thing in things:
		print("thing == "+str(thing))
		matrix[thing[1],thing[0]] = 1

	render_mat(matrix)

	return


if __name__=="__main__":

	shits = ex_string.split("\n\n")

	print(shits)
	print(len(shits))
	path = []

	oof = [str(x) for x in range(10)]

	chars = ["<", ">", "v", "^"] + oof
	print("Chars == "+str(chars))

	ex_bliz = []

	for thing in shits:
		
		new_bliz = set()

		y = 0 # first line is basically almost all wall.

		lines = thing.split("\n")

		print("Lines: "+str(lines))

		for line in lines[2:]: # first line is the "Minute ..." line and the second line is the wall line

			x = -1 # first char is always wall
			
			#x = 0
			print("Processing line == "+str(line))
			for char in line:
				if char in chars:
					# x,y is blizzard
					print("Found char at "+str(tuple((x,y))))
					new_bliz.add(tuple((x,y)))



				x += 1

			y += 1

		ex_bliz.append(new_bliz)

	print(ex_bliz)

	render_stuff(ex_bliz[1],10)

	exit(0)


