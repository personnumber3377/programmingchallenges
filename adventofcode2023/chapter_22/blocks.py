
import sys

# Number of dimensions. (Unused, maybe I will refactor the code to support arbitrary dimensions.)
NUM_DIMS = 3
UP_COORD = 1 # Index of the coordinate which signifies the "up" direction.
UP_SIGN = 1 # sign of where is up (positive means that up is in the positive "UP_COORD" dir)


def create_block_range(block_start: tuple, block_end: tuple) -> list:
    # First get the coordinate which changes.
    for x in range(len(block_start)):
        if block_start[x] != block_end[x]:
            # This differs, therefore this is the coordinate which changes.
            change_ind = x
            if block_start[x] <= block_end[x]:
                # block_start is the actual start
                start = block_start
                end = block_end
            else:
                # Otherwise the start is actually block end.
                start = block_end
                end = block_start
            diff = abs(start[x] - end[x])
            break # No need to go over anymore.
    # This creates a list of all of the coordinates occupied by one brick.
    out = []
    for i in range(diff+1): # Here just create the list of coordinates.
        out.append(start)
        start[change_ind] += 1
    return out # return the list of coordinates


def parse_input() -> list: # Outputs a dictionary, where the keys are coordinates and the value is which block there is at that coordinate. Also outputs a list where the blocks at certain coordinates are the elements and the indexes are which block is currently being considered.
    lines = sys.stdin.read().split("\n")
    pos_dict = dict()
    block_coord_list = []
    for block_num, line in enumerate(lines):
        # Separate on "~"
        block_start, block_end = line.split("~")
        # Now split the coordinates on "," .
        block_start = tuple((int(x) for x in block_start.split(",")))
        block_end = tuple((int(x) for x in block_end.split(",")))
        # Now generate the block range.
        blocks_stuff = create_block_range(block_start, block_end)
        # First append to the block coordinates list.
        block_coord_list.append(blocks_stuff)
        # Now we have the list, now add the stuff to the dictionary thing.
        for pos in blocks_stuff:
            pos_dict


def main() -> int:

    return 0

if __name__=="__main__":
    exit(main())
