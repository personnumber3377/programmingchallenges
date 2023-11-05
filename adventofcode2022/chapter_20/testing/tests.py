

class Circ_array:
	def __init__(self, array: list):
		self.list = array
	def __getitem__(self,index):
		# gets the item at index "index"
		return self.list[index % len(self.list)]
	def __setitem__(self,index,value):
		# sets the item in the list at index to value "value"

		self.list[index % len(self.list)] = value

	def move_element(ind_a, ind_b) -> None:
		# Moves the element from index "ind_a" to "ind_b"
		ind_a = ind_a % len(self.list)
		ind_b = ind_b % len(self.list)

		element = self.list.pop(ind_a) # get the element
		#if ind_b > ind_a: # if the target index is larger than the index where it took it from, then we need to decrement the target index, because the elements shift.
		#	ind_b -= 1
		self.list.insert(ind_b,element)
		return

def main() -> int:

	

	return 0

if __name__=="__main__":
	exit(main())