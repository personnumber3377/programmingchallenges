
import sys

LOOP_COUNT = 64

def get_neig(pos: tuple, matrix: list) -> list:
    possible_neighbours = [tuple((pos[0]-1, pos[1])), tuple((pos[0]+1, pos[1])), tuple((pos[0], pos[1]-1)), tuple((pos[0], pos[1]+1))] # Non-diagonal neighbours only.
    # Now check the validity of these spots
    for pos in possible_neighbours:
        if pos[0] < 0 or pos[1] < 0:
            continue # Do not yield
        if pos[0] >= len(matrix[0]) or pos[1] >= len(matrix):
            continue # Do not yield
        yield pos # Passed bounds checks.

def parse_input() -> list:
    # Parses stdin input
    lines = sys.stdin.read().split("\n")
    out = []
    for y, line in enumerate(lines):
        cur_line = []
        for x, char in enumerate(line):
            if char == "#": # "#" means wall
                cur_line.append(1)
            elif char == "S": # Start
                start = tuple((x,y))
                cur_line.append(0)
            else: # Empty space
                cur_line.append(0)
        out.append(cur_line)
    return out, start

def main() -> int:
    matrix, start = parse_input()
    new_positions = set([start]) # Initialize with the one position
    for i in range(LOOP_COUNT):
        # Main loop.
        new_new = set()
        for pos in new_positions: # optimization. no need to loop over positions which aren't new.
            neighbours = list(get_neig(pos, matrix)) # Get new spots.
            for neig in neighbours:
                assert isinstance(neig, tuple)
                if matrix[neig[1]][neig[0]] == 1: # Wall
                    continue
                #if neig not in visited: # No need to check. the "add" method doesn't do anything if element already is in set.
                new_new.add(neig)
        new_positions = new_new
    print(len(new_positions))
    return 0

if __name__=="__main__":
    exit(main())
