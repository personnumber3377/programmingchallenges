

def multiply_file() -> None:
	fh = open("longerfile.txt", "w+")
	fhorig = open("actual.txt", "r")
	contents = fhorig.read()
	for i in range(30):

		fh.write(contents)
	fh.close()
	return

def main() -> int:
	multiply_file()
	return 0

if __name__=="__main__":
	exit(main())
