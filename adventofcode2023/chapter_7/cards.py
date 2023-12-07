
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

# Thanks to https://stackoverflow.com/a/57003713

def compare_hands(item1, item2):
	print("item1 == "+str(item1))
	print("item2 == "+str(item2))
	cards = "23456789TJQKA"
	cards_values = {cards[i]:i for i in range(len(cards))}
	for i in range(len(item1[0])):
		# Note the way we are sorting here. We are sorting in reverse order (first the worst hand and then the best)
		if cards_values[item1[0][i]] < cards_values[item2[0][i]]:
			print(str(cards_values[item1[0][i]]) + "<" + str(cards_values[item2[0][i]]))
			return -1 # "return a negative value (< 0) when the left item should be sorted before the right item"
		elif cards_values[item1[0][i]] > cards_values[item2[0][i]]:
			print(str(cards_values[item1[0][i]]) + ">" + str(cards_values[item2[0][i]]))
			return 1
	# Hands are identical.

	return 0 # "return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence"

def sort_hands(hands_groups: list) -> None:
	for i in range(len(hands_groups)):
		# Sort each type individially.
		hands_groups[i] = sorted(hands_groups[i], key=cmp_to_key(compare_hands))
	return hands_groups

def get_result(cards_and_bids: list) -> int:
	# This actually calculates the score.
	NUM_OF_TYPES = 7
	# First sort the hands by type.
	#cards = "AKQJT98765432"
	cards = "23456789TJQKA"
	hands_sorted_by_type = [[] for _ in range(NUM_OF_TYPES)]
	for hand, bid in cards_and_bids:
		card_counts = {cards[i]:0 for i in range(len(cards))}
		#print(card_counts)
		for char in hand:
			card_counts[char] += 1
		hand_type = get_hand_type(card_counts)
		print("hand_type == "+str(hand_type))
		hands_sorted_by_type[hand_type].append([hand, bid])
	# Now we have the hands sorted by type. Now sort each of these groups by themselves by the score.
	sort_hands(hands_sorted_by_type)
	# Now they should all be sorted by type and each type group is sorted by value.
	# Join everything together
	all_hands_sorted = [item for row in hands_sorted_by_type for item in row] # Thanks to https://realpython.com/python-flatten-list/
	print("All hands sorted: "+str(all_hands_sorted))
	# Now get the score:
	res = 0
	for i, hand in enumerate(all_hands_sorted):
		res += (i+1)*hand[1] # hand[1] is the bid
	# Run the sanity test
	sanity_test(all_hands_sorted)
	return res

def main() -> int:
	cards_and_bids = parse_input()
	result = get_result(cards_and_bids)
	print("Result: "+str(result))
	return 0

if __name__=="__main__":
	exit(main())
