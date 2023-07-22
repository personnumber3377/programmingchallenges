import sys

def solve(filename: str) -> str:

	fh = open(filename, "r")
	lines = fh.readlines()
	fh.close()
	line = lines[0]
	if line[-1] == "\n":
		line = line[:-1] # get rid of newline

	if len(line) < 4:
		print("Error. Length of packet can not be less than 4.")
		exit(1)
	count = 0
	while count <= len(line)-4:
		thing = line[count:count+4]
		#chars = []

		if len(thing) == len(set(thing)):
			print(line[count:count+4])
			return len(line[:count])+4
		count += 1
	print("Error. No header found in this string: " + str(line))
	exit(1)




if __name__=="__main__":
	print(solve(sys.argv[1]))
	exit()



