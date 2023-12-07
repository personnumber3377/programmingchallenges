
import sys
from functools import cmp_to_key

def parse_input() -> list:
	lines = sys.stdin.read().split("\n")
	out = []
	for line in lines:
		hand, bid = line.split(" ")
		bid = int(bid)
		out.append([hand, bid])
	print(out)
	return out


def get_hand_type(card_counts: dict) -> int:
	'''
	Five of a kind, where all five cards have the same label: AAAAA
	Four of a kind, where four cards have the same label and one card has a different label: AA8AA
	Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
	Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
	Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
	One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
	High card, where all cards' labels are distinct: 23456
	'''
	counts = list(card_counts.values())
	pairs = counts.count(2)
	if 5 in counts:
		return 6
	elif 4 in counts:
		return 5
	elif 3 in counts and 2 in counts:
		# Full house
		return 4
	elif 3 in counts:
		return 3
	elif pairs == 2:
		# Two pair
		return 2
	elif pairs == 1:
		# One pair
		return 1
	else:
		return 0 # High card


def get_hand_value(hand: str) -> int:
	# Ok so now just get the type and the hand value.
	#cards = "AKQJT98765432"
	cards = "23456789TJQKA"
	card_values = {cards[i]:i for i in range(len(cards))} # These are the relative values of each card
	print("card_values == "+str(card_values))
	card_counts = {str(x): 0 for x in cards}
	out = 0
	for i, card in enumerate(hand):
		card_counts[card] += 1 # This is later used to get the "type" of the hand.
		# Add to the out integer the value of the current card.
		# len(cards)**(cardindex)
		#qqq = (len(cards) - i)**(card_values[card])
		qqq = (card_values[card])**(len(cards) - i)
		print("qqq == "+str(qqq))
		print("card_values[card] == "+str(card_values[card]))
		print("card == "+str(card))
		out += qqq
	# Now add the type which trumps all other values of the card
	hand_type = get_hand_type(card_counts)
	print("Hand type for hand "+str(hand)+" is "+str(hand_type))
	#stuff = (len(cards)+1)**(hand_type+len(cards))
	#print("Adding stuff: "+str(stuff))
	out += (len(cards)+1)**(hand_type+len(cards))
	return out#, hand_type


def compare(item1, item2):
	return item1[0] - item2[0]

def sanity_test(hands_stuff: list) -> None:
	# This is used to test the program that it works properly.
	cards = "23456789TJQKA"
	card_values = {cards[i]:i for i in range(len(cards))}
	for i in range(len(hands_stuff)-1):
		print("Now checking: "+str(hands_stuff[i])+" and "+str(hands_stuff[i+1]))

		card_counts1 = {str(x): 0 for x in cards}
		card_counts2 = {str(x): 0 for x in cards}
		#card_counts[card] += 1
		
		# Compare hands. The second hand is supposed to be of greater value than the first
		
		first_hand = hands_stuff[i][2]
		second_hand = hands_stuff[i+1][2]

		for char in first_hand:
			card_counts1[char] += 1
		for char in second_hand:
			card_counts2[char] += 1

		# Now check the type of each hand
		assert get_hand_type(card_counts2) >= get_hand_type(card_counts1)

		# Now check the values of the cards.

		for i in range(len(first_hand)):
			if first_hand[i] == second_hand[i]:
				continue
			else:
				# Now when they differ, the second hand has to have the higher card
				print("second_hand[i] == "+str(second_hand[i]))
				print("first_hand[i] == "+str(first_hand[i]))
				assert second_hand[i] > first_hand[i]
				break


	return

def get_result(cards_and_bids: list) -> int:
	# This actually calculates the score.

	# First sort the list by the value of the hand
	stuff = []
	for hand, bid in cards_and_bids:
		val = get_hand_value(hand)
		#print(str(hand)+": "+str(val))
		stuff.append([val, bid, hand])
	thing = sorted(stuff, key=cmp_to_key(compare))
	sanity_test(thing)
	#print(thing)
	print("Sorted by rank:"+str(stuff))
	print("Now printing all of the hands in order of importance: ")
	for oof in thing:
		print(oof[2])
	total = 0
	count = 1
	for oof in thing:
		total += count*oof[1]
		count += 1
	return total

def main() -> int:
	cards_and_bids = parse_input()
	result = get_result(cards_and_bids)
	print("Result: "+str(result))
	return 0

if __name__=="__main__":
	exit(main())
