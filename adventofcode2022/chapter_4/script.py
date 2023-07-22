
import sys


print("sys.argv == " + str(sys.argv))

fh = open(sys.argv[1], "r") # read file

lines = fh.readlines() # read every line

fh.close()

# grouped = list(zip(*[iter(sequence)] * chunk_size))
# https://jasonstitt.com/python-group-iterator-list-function

pairs = lines

print(pairs)
count = 0

for thing in pairs:
	pair = thing.split(",")
	first_num_pair = [int(x) for x in pair[0].split("-")]
	second_num_pair = [int(x) for x in pair[1].split("-")]
	if first_num_pair[0] >= second_num_pair[0] and first_num_pair[0] <= second_num_pair[1]: #
		count += 1
		continue
	if first_num_pair[1] >= second_num_pair[0] and first_num_pair[1] <= second_num_pair[1]:
		count += 1
		continue
	if second_num_pair[0] >= first_num_pair[0] and second_num_pair[0] <= first_num_pair[1]:
		count += 1
		continue
	if second_num_pair[1] >= first_num_pair[0] and second_num_pair[1] <= first_num_pair[1]:
		count += 1
		continue

print(count)




