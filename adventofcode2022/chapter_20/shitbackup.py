
import sys
import copy
import pickle
from collections import deque
from pathlib import Path
import time
import pickle
import random
import copy

'''
def swap(in_list:list, ind_a: int, ind_b: int) -> None:
	a,b = in_list[ind_a], in_list[ind_b]
	in_list[ind_a], in_list[ind_b] = b, a
	return
'''




def main2(data: list):
    #with open(INPUT_FILE, mode="rt") as f:
    #    data = list(map(int, f.read().splitlines()))
    




    # Part 1
    enumerated = deque(list(enumerate(data.copy())))  # deque of tuples of (original index, value)    
    print("enumerated originally: "+str([x[1] for x in enumerated]))
    enumerated = mix(enumerated)
    #print("enumerated == "+str(enumerated))
    fh = open("binary.bin","wb+")
    pickle.dump(enumerated, fh)
    fh.close()

    return [int(x[1]) for x in enumerated]

    coord_sum = 0
    for n in (1000, 2000, 3000):
        # Turn our enumerated list into a list
        coord_sum += value_at_n([val[1] for val in enumerated], n)
    print(f"Part 1: {coord_sum}")
    
    # Part 2
    new_data = [val*DECRYPTION_KEY for val in data]
    enumerated = deque(list(enumerate(new_data)))  # new deque    
    for _ in range(10): # run the mix 10 times, but always with same enumeration (starting order)
        enumerated = mix(enumerated) 
        
    coord_sum = 0
    for n in (1000, 2000, 3000):
        coord_sum += value_at_n([val[1] for val in enumerated], n)
    print(f"Part 2: {coord_sum}")

def mix(enumerated: deque):
    """ Perform the mix algorithm on our enumerated deque of numbers """
    # Move each number once, using original indexes
    # We can't iterate over actual values from enumerated, since we'll be modifying it as we go
    
    print("start")
    for original_index in range(len(enumerated)): 
        print("enumerated before == "+str([x[1] for x in enumerated]))
        while enumerated[0][0] != original_index: # bring our required element to the left end
            enumerated.rotate(-1) 
    
        current_pair = enumerated.popleft() 
        shift = current_pair[1] % len(enumerated)  # retrieve the value to move by; allow for wrapping over
        enumerated.rotate(-shift) # rotate everything by n positions
        enumerated.append(current_pair) # and now reinsert our pair at the end
        print("enumerated after == "+str([x[1] for x in enumerated]))
        
        # print(enumerated)
    print("end")
    return enumerated
    
def value_at_n(values: list, n: int):
    """ Determine the value at position n in our list.
    If index is beyond the end, then wrap the values as many times as required. """
    digit_posn = (values.index(0)+n) % len(values)
    return values[digit_posn]









def place(in_list: list, ind_a: int, ind_b) -> None: # numbers = place(numbers, a_index, b_index, quotient, num)
	
	# This is here to take care of the loop-around.

	print("Here are the numbers before mixing: "+str(in_list))
	print("ind_a == "+str(ind_a))
	print("ind_b == "+str(ind_b))
	ind_a = ind_a % (len(in_list) - 1)
	ind_b = ind_b % (len(in_list) - 1)
	
	if ind_b == 0:
		ind_b = len(in_list) - 1
	#elif ind_b == len(in_list) - 1:
	#	ind_b = 0

	element = in_list.pop(ind_a) # get the element
	#if ind_b > ind_a: # if the target index is larger than the index where it took it from, then we need to decrement the target index, because the elements shift.
	#	ind_b -= 1
	in_list.insert(ind_b,element)
	print("Here are the numbers after mixing: "+str(in_list))
	return in_list



def parse_input() -> list:
	return [int(x) for x in sys.stdin.read().split("\n")]


def get_numbers(numbers: list):
	index_zero = numbers.index(0) # get index of zero
	#print("index_zero == "+str(index_zero))
	res = 0
	for i in range(1,4):
		#print("i == "+str(i))
		#print("numbers[(1000*i) % (len(numbers))] == "+str(numbers[(1000*i+index_zero) % (len(numbers))]))
		res += numbers[(1000*i+index_zero) % (len(numbers))]
	return res


def solve_puzzle(puzzle_input: list) -> int:



	#print("puzzle_input == "+str(puzzle_input))

	if len(puzzle_input) == len(set(puzzle_input)):
		print("The numbers only appear once!!!")

	orig_numbers = copy.deepcopy(puzzle_input)
	numbers = puzzle_input
	length = len(orig_numbers)
	for i, num in enumerate(orig_numbers):

		if numbers[i] != num:
			a_index = numbers.index(num)
		else:
			a_index = i # assume that the element is not moved.

		b_index = a_index + num

		# swap


		numbers = place(numbers, a_index, b_index)



		#print("The numbers array after mixing: "+str(numbers))

	fh = open("binary.bin", "wb+")
	pickle.dump(numbers, fh)
	fh.close()

	result = get_numbers(numbers)

	print("result == "+str(result))

	return numbers
	

def main() -> int:
	#puzzle_input = parse_input()
	#result = solve_puzzle(puzzle_input)
	#print("Solution: "+str(result))
	comparison()

	return 0


def generate_random_input(length: int):

	out_list = [int(x) for x in range(length)]
	random.shuffle(out_list)
	return out_list


def fail(cor, our, input_list):
	print("="*50)

	print("FAIL!")
	print("correct output: "+str(cor))
	print("our output: "+str(our))
	print("input_list: "+str(input_list))


	print("="*50)
	exit(1)


def comparison():
	for _ in range(100):
		input_list = generate_random_input(4)
		ooflist2 = copy.deepcopy(input_list)
		correct_output = main2(ooflist2)
		ooflist = copy.deepcopy(input_list)
		our_output = solve_puzzle(ooflist)
		assert len(correct_output) == len(our_output)
		if correct_output != our_output:
			fail(correct_output, our_output, input_list)
	return 0

if __name__=="__main__":

	exit(main())
