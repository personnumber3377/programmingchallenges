
import sys

def decode_snafu(encoded:str) -> int:


	cur_power = len(encoded) - 1

	values = {"-": -1, "=": -2, "0": 0, "1": 1, "2": 2, "3":3 }

	out = 0
	for char in encoded:

		value = values[char]

		out += (value)*(5**cur_power)

		cur_power -= 1

	return out
'''
def encode_snafu(decoded: int) -> str:

	cur_power = 1000

	if (3)*(5**cur_power) < decoded:
		print("Number too big!")
		exit(1)

	#while (3)*(5**cur_power) > decoded:
	while (5**cur_power) > decoded:
		#print("(3)*(5**cur_power) == "+str((3)*(5**cur_power)))
		cur_power -= 1

	#cur_power -= 1
	value = 0

	string = []

	while True:
		print("String: "+str(string))
		print("Cur power: "+str(cur_power))
		if value > decoded:
			# need to subtract
			print("decoded - (5**cur_power) == "+str(decoded - (5**cur_power)))
			if value < decoded + (5**cur_power):
				string.append("-")
				print("Subtracting1: "+str((-1)*(5**cur_power)))
				value += (-1)*(5**cur_power)
			#elif value <= decoded - (5**cur_power):
			else:
				string.append("=")
				print("Subtracting2: "+str((-2)*(5**cur_power)))
				value += (-2)*(5**cur_power)
			#else:
			#	print("Failed with value == "+str(value)+" and cur_power == "+str(cur_power))
			#	exit(1)





		#if value < decoded:
		else:
			print("Poopoo")
			char_count = 0

			while value + char_count*(5**cur_power) < decoded:

				char_count += 1
			print("Char count: "+str(char_count))
			assert char_count < 4

			string.append(str(char_count))
			print("Adding: "+str(char_count*(5**cur_power)))
			value = value + char_count*(5**cur_power)

		cur_power -= 1
		if cur_power == -1:
			break


		

		assert value >= 0
		print("Value: "+str(value))

	out_string = "".join(string)
	print("String is : "+str(out_string))
	return out_string
'''

def encode_snafu(decoded: int) -> str:

	cur_power = 1000

	if (3)*(5**cur_power) < decoded:
		print("Number too big!")
		exit(1)

	#while (3)*(5**cur_power) > decoded:
	
	while (5**cur_power) > decoded:
		#print("(3)*(5**cur_power) == "+str((3)*(5**cur_power)))
		cur_power -= 1

	list_thing = []
	remainder = decoded


	EXAMPLE = True


	example_stuff = [2,-2,-1,1,-2,0]

	n = 0
	while remainder != 0:
		
		count = 3

		while count*(5**cur_power) > remainder:
			print("Looped!")
			count -= 1
			#if count < -2:
			#	print("poopoo")
			#	exit(1)
		count += 1
		print("count: "+str(count))
		print("(3)*(5**(cur_power - 1)) == "+str((3)*(5**(cur_power - 1))))

		print("remainder - count*(5**cur_power) == "+str(remainder - count*(5**cur_power)))
		if (3)*(5**(cur_power - 1)) < remainder - count*(5**cur_power):

			count += 1

		assert count >= -2

		print("count: "+str(count))
		print("cur_power: "+str(cur_power))
		#print("remainder: "+str(remainder))

		list_thing.append(count)
		print("count*(5**cur_power) == "+str(count*(5**cur_power)))
		remainder -= count*(5**cur_power)
		#assert decoded >= 0
		cur_power -= 1
		
		if example_stuff[n] != count:
			print("Exit.")
			exit(1)
		print("remainder: "+str(remainder))
		assert cur_power >= 0


		n += 1

	print("list_thing: "+str(list_thing))

	return str(list_thing)




def snafu() -> int:

	lines = sys.stdin.buffer.read().decode('ascii').split("\n")


	total_sum = 0

	for line in lines:

		total_sum += decode_snafu(line)
	print("Snafu returned this: "+str(total_sum))
	return total_sum


if __name__=="__main__":

	print("Solution to puzzle: " + str(encode_snafu(snafu())))

