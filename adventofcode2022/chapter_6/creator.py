
import random
from header import *

alphabet = "abcdefghijklmnopqrstuvxyz"
alphabet_set = set(alphabet)


def create_data(distinct_len: int, wanted_len: int) -> str:

	#distinct_len = 14

	data = random.sample(alphabet,distinct_len)
	data[0] = random.choice(data[1:])
	previous_chars = data[:]
	assert len(previous_chars) == distinct_len

	cur_len = distinct_len

	#wanted_len = 1000

	while cur_len != wanted_len:

		cur_char = random.choice(previous_chars)

		#print("previous_chars == "+str(previous_chars))

		assert len(previous_chars) == distinct_len
		#while cur_char not previous_chars:

		#	cur_char = random.choice(previous_chars)

		data.append(cur_char)

		#previous_chars.pop(0)

		#previous_chars.append(random.choice(alphabet))

		#print("previous_chars == "+str(previous_chars))

		cur_len += 1
		#print("Current length: "+str(cur_len))
	
	selected_index = random.randrange(distinct_len,wanted_len- distinct_len)

	#replacement = random.sample(alphabet,distinct_len)
	
	#replacement[0] = data[selected_index-1]
	#print("replacement: "+str(replacement))
	#data[selected_index-1] = random.choice(data[selected_index - distinct_len: selected_index])
	#data[selected_index:selected_index+distinct_len] = replacement

	#print("selected_index: "+str(selected_index))


	new_chars = set()
	for i in range(distinct_len):
		cur_char = data[selected_index + i]
		prev_char = data[selected_index + i - distinct_len]
		#print("")
		if prev_char not in new_chars:

			#print("cur_char: "+str(cur_char))
			data[selected_index+i] = prev_char
			#new_chars.add(data[selected_index - distinct_len])
			new_chars.add(prev_char)


		else:
			#print("list(alphabet_set - new_chars) == "+str(list(alphabet_set - new_chars)))
			selected_char = random.choice(list(alphabet_set - new_chars))
			#print("selected_char == "+str(selected_char))
			data[selected_index+i] = selected_char
			new_chars.add(selected_char)

		#print("new_chars == "+str(new_chars))
		#print("data[selected_index:selected_index+distinct_len] == "+str(data[selected_index:selected_index+distinct_len]))
	cor_index = selected_index+distinct_len
	#print("Selected index: "+str(cor_index))
	return "".join(data), cor_index



if __name__=="__main__":

	#print(create_data())
	max_len = 100000
	min_len = 100

	min_dist_len = 2
	max_dist_len = len(alphabet)

	test_count = 1000

	for i in range(test_count):
		print("i: "+str(i))
		distinct_len = random.randrange(min_dist_len, max_dist_len+1)
		wanted_len = random.randrange(min_len, max_len+1)
		testdata, cor_index = create_data(distinct_len, wanted_len)

		predicted = solvestr(testdata, distinct_len)

		assert len(testdata) == wanted_len
		if cor_index < predicted - distinct_len and cor_index > predicted:


			print("Fail!")
			
			print("Test data: "+str(testdata))
			print("Distinct length: "+str(distinct_len))

			print("Predicted: "+str(predicted))
			print("cor_index: "+str(cor_index))
			exit(1)

	print("Passed!")
	exit(0)
