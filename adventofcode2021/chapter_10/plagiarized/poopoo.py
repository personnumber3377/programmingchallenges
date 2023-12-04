
# https://www.reddit.com/r/adventofcode/comments/rd0s54/comment/hohtmda/?utm_source=share&utm_medium=web2x&context=3

import pathlib
import sys
 
openings = '{([<'
closings = '})]>'
 
closing_brackets = {cl: op for op, cl in zip(openings, closings)}
opening_brackets = {op: cl for op, cl in zip(openings, closings)}
 
syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}
 
 
def parse() -> list[int]:
    """ Parse input """
    #return puzzle_input.splitlines()
    return sys.stdin.read().split("\n")
 
 
def find_mismatch(text: str) -> str:
    """ Go thru a string and see if there's a mismatch """
    stack = []
    for char in text:
        if char in openings:
            stack.append(char)
        elif char in closings:
            popped = stack.pop()
            if closing_brackets[char] != popped:
                # print(
                #     f"Expected {opening_brackets[popped]}, but found {char} instead."
                # )
                return char
 
 
def part1(navi_sub: list[int]) -> int:
    """ Solve part 1 """
    scores = []
    for line in navi_sub:
        incorrect_char = find_mismatch(line)
        if incorrect_char is not None:
            scores.append(syntax_error_scores[incorrect_char])
    return sum(scores)
 
 
def remove_corrupted(lines: list[str]) -> list[str]:
    """ Return a list of only incomplete lines """
    incompletes = []
    for line in lines:
        if find_mismatch(line):
            continue
        incompletes.append(line)
    return incompletes
 
 
def fill_stack(line: str) -> list[str]:
    """ Fill the tack with chars from line and see what's left """
    stack = []
    for char in line:
        if char in openings:
            stack.append(char)
        elif char in closings:
            stack.pop()
    return stack
 
 
def get_missing(line: str) -> list[str]:
    """ See contents of stack and generate missing closings """
    # Return contents of stack (unclaimed openings)
    leftovers = fill_stack(line)
    # Get a list of the endings
    return [opening_brackets[op] for op in leftovers[::-1]]
 
 
def autocomplete_score(chars: list[str]) -> int:
    """ Check the chars left in the Stack and calculate the score """
    score = 0
    for char in chars:
        score *= 5
        score += autocomplete_scores[char]
    return score
 
 
def part2(navi_sub: list[int]) -> int:
    """ Solve part 2 """
    incompletes = remove_corrupted(navi_sub)
    scores = []
    for i,line in enumerate(incompletes):
        #print(i)
        missing_chars = get_missing(line)
        scores.append(autocomplete_score(missing_chars))
    # Return "middle" value
    low_high = sorted(scores)
    mid_idx = len(low_high) // 2
    return low_high[mid_idx]
 
 
def solve() -> tuple[int, int]:
    """ Solve the puzzle for the given input """
    data = parse()
    #solution1 = part1(data)  # Correct answer was 469755 (with my data) # get rid of part 1 solution because it messes with our measurements.
    solution2 = part2(data)  # Correct answer was 2762335572 (with my data)
 
    #return solution1, solution2
    return solution2
 
 
if __name__ == "__main__":
    #for path in sys.argv[1:]:
    #print(f"{path}:")
    #puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve()
    print(solutions)
    #print('\n'.join(str(solution) for solution in solutions))