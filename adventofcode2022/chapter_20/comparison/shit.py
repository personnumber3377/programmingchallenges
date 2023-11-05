
import pickle

if __name__=="__main__":

	stuff1 = open("otherstuff.bin", "rb")
	shit1 = pickle.load(stuff1)
	stuff1.close()


	stuff2 = open("binary.bin", "rb")
	shit2 = pickle.load(stuff2)
	stuff2.close()


	#print("shit1 == "+str(shit1))
	print("shit2 == "+str(shit2))



	# value is the index number one

	ours = shit1

	others = [int(x[1]) for x in shit2]

	#print("others == "+str(others))

	print("comparison: "+str(ours == others))
	assert len(ours) == len(others)
	for i in range(len(others)):
		if ours[i] != others[i]:
			print("Fail at index "+str(i))
			print("ours : "+str(ours[i]))
			print("theirs: "+str(others[i]))
			exit(1)
	exit(0)