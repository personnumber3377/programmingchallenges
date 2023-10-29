
import subprocess

RUN_COUNT = 1000

def run_once() -> float:

	output = subprocess.check_output("./cprof.sh", stderr=subprocess.STDOUT, shell=True)

	lines = output.split(b"\n")

	count = 0

	for line in lines:
		if b"ncalls" in line:
			break
		count += 1

	count += 1
	
	out_time = 0.0
	
	for line in lines[count:]:
		#print("line == "+str(line))
		#print("line.split(b\" \") == "+str(line.split(b" ")))
		thing_count = 0
		poopoo = line.split(b" ")
		if poopoo == [b'']:
			break
		while poopoo[thing_count] == b'':
			thing_count += 1
		thing_count += 1

		out_time += float(line.split(b" ")[thing_count])
	print("This run took "+str(out_time)+" seconds.")
	return out_time


def main() -> int:
	# ./cprof.sh
	tot_time = 0.0

	for _ in range(RUN_COUNT):

		tot_time += run_once()

	return tot_time / RUN_COUNT


if __name__=="__main__":
	exit(main())
