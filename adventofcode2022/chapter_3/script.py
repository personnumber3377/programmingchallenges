


fh = open("input.txt", "r")
lines = fh.readlines()
fh.close()

priority_sum = 0


for line in lines:
	#print(line)
	line = line[:-1]
	first_part = line[:len(line)//2]
	second_part = line[len(line)//2:]
	print(first_part)
	print(second_part)

	for char in first_part:
		if char in second_part:
			print("Char: " + str(char))
			if char < "a":
				priority_sum += 27+ord(char)-ord("A")
			else:
				priority_sum += ord(char)+1-ord("a")
			break






print(priority_sum)




