
import time
from operator import add

def map_test(a: list, b: list) -> None:

	res = tuple(map(add,a,b))

def sum_thing(a: list, b: list) -> None:

	res = tuple([a[i]+b[i] for i in range(len(a))])




if __name__=="__main__":

	#a = [1,2,3]*(10**6)
	#b = [4,5,6]*(10**6)
	a = [1,2]
	b = [3,4]


	n = 100000

	mapping_count = 0

	for _ in range(n):


		orig_time = time.time()

		map_test(a,b)
		map_time = time.time() - orig_time
		print("Mapping took "+str(map_time)+" seconds.")
		


		orig_time = time.time()
		sum_thing(a,b)
		sum_time = time.time() - orig_time
		print("Adding took "+str(sum_time)+" seconds.")

		



		

	exit(0)
