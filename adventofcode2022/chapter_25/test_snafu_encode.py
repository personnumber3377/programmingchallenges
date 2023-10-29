
from snafu_naive import *




if __name__=="__main__":
	#test_str = "2=-01"
	test_int = 4890
	test_int2 = 13
	expected_result = "2=-1=0"

	#assert encode_snafu(test_int) == "2=-1=0"
	result = encode_snafu(test_int)
	print("Encoding result2: ==============")

	result2 = encode_snafu(test_int2)
	print("Done! "+"="*20)
	oofthing = decode_snafu(result)
	print("oofthing:" +str(oofthing))
	print("Result: "+str(result))

	print("Result2: "+str(result2))

	if result != expected_result:
		print("Fail!")
		exit(1)
	shitoof = decode_snafu("1-=")
	print("shitoof: "+str(shitoof))
	print("Passed!")
	exit(0)
