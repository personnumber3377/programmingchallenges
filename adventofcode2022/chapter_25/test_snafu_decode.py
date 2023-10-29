
from snafu_naive import *




if __name__=="__main__":
	test_str = "2=-01"


	assert decode_snafu(test_str) == 976

	print("decode_snafu(\"1-=\") == "+str(decode_snafu("1-=")))
	print("Passed!")
	exit(0)
