
import sys
import copy


# Number of dimensions. (Unused, maybe I will refactor the code to support arbitrary dimensions.)
NUM_DIMS = 3
UP_COORD = 2 # Index of the coordinate which signifies the "up" direction.
UP_SIGN = 1 # sign of where is up (positive means that up is in the positive "UP_COORD" dir)
PART = 2

class Brick:
    def __init__(self, id: int, start: tuple, end: tuple) -> None:
        # Constructor
        #self.blocks = create_block_range(start, end)
        self.id = id
        self.pos1 = list(start)
        self.pos2 = list(end)
        self.below_bricks = set()
        self.above_bricks = set()
        self._supporting = None
        self._is_supported_by = None

        # Get the lowest and highest points.
        self.update_highest()
        self.update_lowest()

    def update_highest(self) -> None:
        self.highest = max(self.pos1[UP_COORD], self.pos2[UP_COORD])

    def update_lowest(self) -> None:
        self.lowest = max(self.pos1[UP_COORD], self.pos2[UP_COORD])

    def on_ground(self) -> bool:
        return self.lowest_point() == 1

    def highest_point(self):
        #return max(self.pos1[UP_COORD], self.pos2[UP_COORD])
        return self.highest
    
    def lowest_point(self):
        #return min(self.pos1[UP_COORD], self.pos2[UP_COORD])
        return self.lowest

    def is_level_below(self, other) -> bool:
        return self.highest_point() == other.lowest_point()-1
    def is_supported_by(self):
        if self._is_supported_by == None:
            self._is_supported_by = [x for x in self.below_bricks if x.is_level_below(self)]
        return self._is_supported_by

    def supporting(self):
        if self._supporting == None:
            #print("self.above_bricks == "+str(self.above_bricks))
            self._supporting = [x for x in self.above_bricks if self.is_level_below(x)]
        #print(self._supporting)
        return self._supporting

    def ranges_overlap(self, r1, r2) -> bool:
        return not (r1[1] < r2[0] or r1[0] > r2[1])

    def is_under(self, other) -> bool: # Check for x and y overlap.
        x_overlap, y_overlap, _ = self.overlaps(other)
        return x_overlap and y_overlap

    def overlaps(self, other) -> bool:
        x1, y1, z1 = self.pos1
        x2, y2, z2 = self.pos2
        x_r1 = (min(x1,x2), max(x1,x2))
        y_r1 = (min(y1,y2), max(y1,y2))
        z_r1 = (min(z1,z2), max(z1,z2))

        x3, y3, z3 = other.pos1
        x4, y4, z4 = other.pos2

        x_r2 = (min(x3,x4), max(x3,x4))
        y_r2 = (min(y3,y4), max(y3,y4))
        z_r2 = (min(z3,z4), max(z3,z4))

        overlap_x = self.ranges_overlap(x_r1, x_r2)
        overlap_y = self.ranges_overlap(y_r1, y_r2)
        overlap_z = self.ranges_overlap(z_r1, z_r2)

        return (overlap_x, overlap_y, overlap_z)

    def drop(self, amount=1) -> None:
        self.pos1[2] -= amount
        self.pos2[2] -= amount

    def __str__(self) -> str:
        return "Block: "+str(self.pos1)+", "+str(self.pos2)


def create_block_range(block_start: tuple, block_end: tuple) -> list:
    block_start = list(block_start)
    block_end = list(block_end)
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

def drop_bricks(bricks: list) -> list:
    # Make a copy of the original bricks.
    orig_bricks = copy.deepcopy(bricks)
    bricks.sort(key=lambda x: x.lowest_point())
    for falling in bricks:
        if falling.on_ground(): # If brick is already on ground, then don't go over it.
            continue
        highest_point = 1
        lower_bricks = [lower for lower in bricks if lower.lowest_point() < falling.lowest_point()] # Here we check all of the bricks and check if the brick is lower than the current falling brick.
        if lower_bricks == []: # If there are no bricks which are lower than this brick (this falling brick will fall to the ground) then continue
            #print(" no lower_bricks")
            continue
        # Now check for collision with the lower bricks.
        for lower in lower_bricks:
            if lower.is_under(falling): # Here check if we fall on top of this brick.
                #print("poopoo")
                falling.below_bricks.add(lower)
                lower.above_bricks.add(falling)
                #print("lower.above_bricks == "+str(lower.above_bricks))
                highest_point = max(highest_point, lower.highest_point()+1) # Update the current highest point.
        if falling.lowest_point() > highest_point: # Check if we need to move the brick.
            falling.drop(falling.lowest_point() - highest_point) # Move the brick by the difference.
            falling.update_highest()
            falling.update_lowest()

    # Now sort the bricks again by their lowest point. This needs to be done, because the positions of the bricks have changed.
    bricks.sort(key=lambda x: x.lowest_point())
    return bricks

def parse_input() -> list: # Outputs a dictionary, where the keys are coordinates and the value is which block there is at that coordinate. Also outputs a list where the blocks at certain coordinates are the elements and the indexes are which block is currently being considered.
    lines = sys.stdin.read().split("\n")
    bricks = []
    for block_num, line in enumerate(lines):
        # Separate on "~"
        block_start, block_end = line.split("~")
        # Now split the coordinates on "," .
        block_start = tuple((int(x) for x in block_start.split(",")))
        block_end = tuple((int(x) for x in block_end.split(",")))
        # Now generate the block range.
        new_brick = Brick(block_num, block_start, block_end)
        #print(new_brick)
        bricks.append(new_brick)

    return bricks

def disintegrate(brick: Brick) -> int: # This actually checks if we can remove the brick or not.
    # Loop over each brick which is supported by the current brick.
    for being_supported in brick.supporting():
        assert len(being_supported.is_supported_by()) != 0
        #print("being_supported.is_supported_by() == "+str(being_supported.is_supported_by()))
        if len(being_supported.is_supported_by()) == 1: # If that one brick is supported by only one other brick (the current one) then we can NOT remove it, therefore return zero
            return 0
    return 1 # Otherwise we can remove it. Return one

def solve(solve_func, bricks: list) -> int: # This is the actual solve function
    # Go over each brick with the corresponding part function.
    tot = 0
    for b in bricks:
        #print("poopoo")
        #print("tot == "+str(tot))
        tot += solve_func(b)
    return tot
    #return sum(solve_func(b) for b in bricks)

def debug(solve_func, bricks: list) -> int:
    for b in bricks:
        if b.id == 0: # Get the very first brick.
            return solve_func(b)

# Old recursive version. Replaced with a while loop.
'''
def fall_check_recursive(brick: Brick, cur_count = 0) -> int:
    # This function checks the bricks recursively to find out how many bricks would fall if one is removed.
    # First get the bricks are below the current brick and loop over them.
    bricks_which_we_supported = []
    print("New")
    for b in brick.supporting():
        if len(b.is_supported_by()) == 1: # The brick is supported only by this one brick, so therefore add one to the count and then add it to the list.
            cur_count += 1
            bricks_which_we_supported.append(b) # Loop over this next brick.
            print("poopoo")
    print("bricks_which_we_supported == "+str(bricks_which_we_supported))
    for b in bricks_which_we_supported:
        print("cur_count == "+str(cur_count))
        cur_count += fall_check_recursive(b, cur_count=cur_count)
    return cur_count
'''

def fall_check_new(initial_brick: Brick) -> int:
    # This function checks the bricks recursively to find out how many bricks would fall if one is removed.
    # First get the bricks are below the current brick and loop over them.
    bricks_which_we_supported = []
    bricks = [initial_brick]
    falling_bricks = set([initial_brick])
    cur_count = 0
    while bricks != []:
        new_bricks = []
        for brick in bricks:
            for b in brick.supporting():
                if b in falling_bricks: # Do not try to drop a brick many times. Just once.
                    continue
                #if len(b.is_supported_by()) == 1: # The brick is supported only by this one brick, so therefore add one to the count and then add it to the list.
                if all(b in falling_bricks for b in b.is_supported_by()): # 
                    cur_count += 1
                    new_bricks.append(b) # Loop over this next brick.
                    falling_bricks.add(b)
        bricks = new_bricks
    return cur_count

def chain_reaction(brick: Brick) -> int:
    #print("Fuck")
    return fall_check_new(brick)
    #return 0 # To be implemented...

def main() -> int:
    bricks = parse_input()
    bricks = drop_bricks(bricks) # Simulate the falling of the bricks. (We need to do this for both parts.)
    if PART == 1:
        res = solve(disintegrate, bricks)
    elif PART == 2:
        res = solve(chain_reaction, bricks)
    elif PART == 3: # Debug.
        res = debug(chain_reaction, bricks)
    else:
        print("Invalid part number: "+str(PART))
        exit(1)

    print(res) # Print final solution.
    return 0

if __name__=="__main__":
    exit(main())




