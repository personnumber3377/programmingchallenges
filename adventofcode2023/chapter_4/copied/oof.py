
import sys

def prepare(input):
    cards = []

    for line in input.splitlines():
        winners, numbers = line.split(': ')[1].split(' | ')
        cards.append((winners.split(), numbers.split()))

    return cards

def second(input): 
    cards = [1] * len(input)

    for (i, card) in enumerate(input):
        for j in range(i + 1, i + 1 + len(set(card[0]) & set(card[1]))):
            cards[j] += 1 * cards[i]

    return sum(cards)

def main() -> int:
    stuff = prepare(sys.stdin.read())
    print(second(stuff))
    return 0

if __name__=="__main__":
    exit(main())