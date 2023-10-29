

if __name__=="__main__":

	dict1 = {"something": "stuff", "somethingelse":"otherstuff", 123:321}

	thing_list = []


	for i in range(10):

		dict2 = (dict1).copy()
		thing_list.append(dict2)
		dict1[123] = i
	dict1["something"] = "newstuff"

	#assert dict1 != dict2

	print("dict1: "+str(dict1))
	print("dict2: "+str(dict2))


	print("thing_list == "+str(thing_list))

	thing_list[0]["something"] = "blabla"
	print("thing_list == "+str(thing_list))
	exit(0)