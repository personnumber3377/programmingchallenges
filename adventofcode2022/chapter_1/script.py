
fh = open("input.txt", "r")
lines = fh.readlines()
fh.close()

cur_sum = 0
max_sum = 0
sum_list = []
for line in lines:
	if line == "\n":
		sum_list.append(cur_sum)
		if cur_sum > max_sum:
			max_sum = cur_sum
		cur_sum = 0
	else:
		cur_sum += int(line)
#print(max_sum)
print(sorted(sum_list,reverse=True)[:3])
print(sum(sorted(sum_list,reverse=True)[:3]))



