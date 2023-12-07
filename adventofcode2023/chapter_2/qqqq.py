
import sys

MULTIPLY_COUNT = 1000

def multiply_file() -> None:
	fh = open("longerfile.txt", "w+")
	fhorig = open(sys.argv[1], "r")
	contents = fhorig.read()
	for i in range(MULTIPLY_COUNT):

		fh.write(contents)
	fh.close()
	return

def main() -> int:
	multiply_file()
	return 0

if __name__=="__main__":
	exit(main())
