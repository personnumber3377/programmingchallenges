
import sys
import os







if __name__=="__main__":
	if len(sys.argv) < 2:
		print("Usage: python3.8 "+str(sys.argv[0])+" PYTHONSCRIPT")
		print("Example: python3.8 "+str(sys.argv[0])+" tetriswithrangedetection.py")
		exit(1)
	command = "python3.8 -m cProfile "+str(sys.argv[1])+" < actual.txt > profile.txt"

	n = 20
	tot_time = 0
	for i in range(n):
		print("i == "+str(i))
		os.system(command)

		fh = open("profile.txt", "r")

		lines = fh.readlines()

		fh.close()

		speed_line = lines[1] # second line in file has the time which it took to complete execution

		things = speed_line.split(" ")

		speed = float(things[-2])



		tot_time += speed

	print("Average time took "+str(tot_time/n)+" seconds.")
	exit(0)

