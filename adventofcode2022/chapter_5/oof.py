
import sys

def run_program(boxes, moves):
	print("Running script:")
	print("------------------------------------------------------")
	count = 0
	for move in moves:
		print("Current move number: " + str(count+1))
		print("Current move: " + str(move))
		how_many = move[0]
		start = move[1]-1
		end = move[2]-1
		list_shit = []

		for _ in range(how_many):
			list_shit.append(boxes[start].pop(0))
		#list_shit.reverse()
		boxes[end]= list_shit+boxes[end]
		print("Boxes after move: " + str(boxes))
	#print(boxes)
	
	#
	resulting_string = ''.join(x[0] for x in boxes)
	print(resulting_string)
	print("Final boxes:")
	print(boxes)
	return resulting_string




def parse_input(lines: list):
	count = 0
	blocks = []
	while " 1 " not in lines[count]:
		count += 1
	print("Bullshit thing: " + str(lines[count]))
	len_of_list = int(lines[count].split(" ")[-2])
	blocks = []#*len_of_list
	for i in range(len_of_list):
		blocks.append([])
	count = 0
	shits = []
	while " 1 " not in lines[count]:
		if "[" in lines[count]:
			bullshitpoopoo = []
			for i in range(len_of_list-1):
				bullshitpoopoo.append(lines[count][i*4:i*4+3])
				print("Appending this: " + str(lines[count][i*4:i*4+3]))
			bullshitpoopoo.append(lines[count][-4:-1])
			shits.append(bullshitpoopoo)
		print("shit")
		print("lines[count]: " + str(lines[count]))
		count += 1
	print("Shits: " + str(shits))
	for oof in shits:
		print("oof == " + str(oof))
		for k in range(len(oof)):
			if oof[k] != "   ":
				print("oof[k] == " + str(oof[k]))
				print("blocks[k] before: " + str(blocks[k]))
				print("k == " + str(k))
				if oof[k][0] == "[" and oof[k][2] == "]":
					print("Blocks before: ")
					print(blocks)
					print("blocks[k] before == " + str(blocks[k]))
					blocks[k].append(oof[k][1])
					print("Blocks after: ")
					print(blocks)
					print("blocks[k] after == " + str(blocks[k]))

	moves = []

	for line in lines[count+1+1:]:
		appendablelist = []
		print("line == " + str(line))
		print("line[5:].index(\" \") == " + str(line[5:].index(" ")))
		appendablelist.append(int(line[5:line[5:].index(" ")+1+5]))
		line = line[line[5:].index(" ")+1+5:]
		print(line)
		print(appendablelist)
		line = line[5:]
		another_integer = line[:line.index(" ")]
		appendablelist.append(int(another_integer))
		line = line[line.index(" ")+1:]
		print(line)
		print(appendablelist)
		finalinteger = int(line[3:])
		appendablelist.append(finalinteger)
		moves.append(appendablelist)
		#moves.append(line)
	return blocks, moves

if __name__=="__main__":


	fh = open(sys.argv[1], "r")
	things = fh.readlines()
	fh.close()


	boxes, moves = parse_input(things)

	print(boxes)
	print(moves)


	string = run_program(boxes, moves)
	print("Answer: " + str(string))