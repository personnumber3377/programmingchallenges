import sys

def solve(filename: str) -> str:
	fh = open(filename, "r")
	lines = fh.readlines()
	fh.close()
	line = lines[0]
	if line[-1] == "\n":
		line = line[:-1] # get rid of newline
	distinct_chars = 14
	if len(line) < distinct_chars:
		print("Error. Length of packet can not be less than {}.", distinct_chars)
		exit(1)
	count = 0
	while count <= len(line)-distinct_chars:
		thing = line[count:count+distinct_chars]
		if len(thing) == len(set(thing)):
			print(line[count:count+distinct_chars])
			return len(line[:count])+distinct_chars
		count += 1
	print("Error. No header found in this string: " + str(line))
	exit(1)



def solvestr(line: str, distinct_chars: int) -> str:
	#fh = open(filename, "r")
	#lines = fh.readlines()
	#fh.close()
	#line = lines[0]
	#if line[-1] == "\n":
	#	line = line[:-1] # get rid of newline
	#distinct_chars = 14
	if len(line) < distinct_chars:
		print("Error. Length of packet can not be less than {}.", distinct_chars)
		exit(1)
	count = 0
	while count <= len(line)-distinct_chars:
		thing = line[count:count+distinct_chars]
		if len(thing) == len(set(thing)):
			#print(line[count:count+distinct_chars])
			return len(line[:count])+distinct_chars
		count += 1
	print("Error. No header found in this string: " + str(line))
	exit(1)

if __name__=="__main__":
	print(solve(sys.argv[1]))
	exit()
