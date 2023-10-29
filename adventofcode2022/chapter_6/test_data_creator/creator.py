
import random


alphabet = "abcdefghijklmnopqrstuvxyz"
alphabet_set = set(alphabet)


def create_data() -> str:

	distinct_len = 14

	data = random.sample(alphabet,distinct_len)
	data[0] = random.choice(data[:-1])
	previous_chars = data[:]
	assert len(previous_chars) == distinct_len

	cur_len = distinct_len

	wanted_len = 1000

	while cur_len != wanted_len:

		cur_char = random.choice(previous_chars)

		#print("previous_chars == "+str(previous_chars))

		assert len(previous_chars) == distinct_len
		#while cur_char not previous_chars:

		#	cur_char = random.choice(previous_chars)

		data.append(cur_char)

		#previous_chars.pop(0)

		#previous_chars.append(random.choice(alphabet))

		print("previous_chars == "+str(previous_chars))

		cur_len += 1
		print("Current length: "+str(cur_len))
	
	selected_index = random.randrange(0,wanted_len- distinct_len)

	replacement = random.sample(alphabet,distinct_len)
	
	#replacement[0] = data[selected_index-1]
	data[selected_index-1] = replacement[0]
	data[selected_index:selected_index+14] = replacement
	print("Selected index: "+str(selected_index+distinct_len))
	return "".join(data)



if __name__=="__main__":

	print(create_data())

