
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
	card_counts = {str(x): 0 for x in cards}
	out = 0
	for i, card in enumerate(hand):
		card_counts[card] += 1 # This is later used to get the "type" of the hand.
		# Add to the out integer the value of the current card.
		# len(cards)**(cardindex)
		out += (len(cards) - i)**(card_values[card])
	# Now add the type which trumps all other values of the card
	hand_type = get_hand_type(card_counts)
	out += (len(cards)+1)**(hand_type)
	return out


def compare(item1, item2):
	return (item1[1]) - (item2[1])

def get_result(cards_and_bids: list) -> int:
	# This actually calculates the score.

	# First sort the list by the value of the hand
	stuff = []
	for hand, bid in cards_and_bids:
		val = get_hand_value(hand)
		print(str(hand)+": "+str(val))
		stuff.append([hand, val])
	thing = sorted(stuff, key=cmp_to_key(compare))
	print(thing)
	return 0

def main() -> int:
	cards_and_bids = parse_input()
	result = get_result(cards_and_bids)
	return 0

if __name__=="__main__":
	exit(main())
