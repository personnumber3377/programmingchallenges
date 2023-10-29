
import time
RUN_COUNT = 100000000



if __name__=="__main__":
	scan_x = 0
	scan_y = 0
	start = time.time()


	

	for _ in range(RUN_COUNT):

		if scan_x == 39:
			scan_x = 0
			scan_y += 1
		else:
			scan_x += 1

	print("First part took "+str(time.time() - start)+ "seconds.")
	scan_x = 0
	scan_y = 0
	start = time.time()

	for _ in range(RUN_COUNT):

		scan_x += 1
		if scan_x == 40:
			scan_x = 0
			scan_y += 1

	print("Second part took "+str(time.time() - start)+ "seconds.")


	#else:
	#	scan_x += 1

