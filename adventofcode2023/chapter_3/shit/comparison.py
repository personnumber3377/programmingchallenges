
def compare():
	fh = open("2.txt", "r")
	contents1 = fh.read()
	fh.close()
	fh = open("1.txt", "r")
	contents2 = fh.read()
	fh.close()
	contents1 = contents1[1:-1]
	contents2 = contents2[1:-1]
	shit1 = contents1.split(", ")
	shit2 = contents2.split(", ")
	for thing in shit2:
		if thing not in shit1:
			print(str(thing) + " is not in our numbers.")

	for thing in shit1:
		if thing not in shit2:
			#print("FAIL!")
			#exit(1)
			print(str(thing) + " is in our numbers, but not in the actual numbers.")

	return 

def main() -> int:
	compare()
	return 0

if __name__=="__main__":
	exit(main())
