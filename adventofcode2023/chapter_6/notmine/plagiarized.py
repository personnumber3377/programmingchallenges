
# Thanks to https://www.reddit.com/r/adventofcode/comments/18bwe6t/comment/kccr53u/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import sys
import re
from functools import reduce
from itertools import starmap
from math import ceil, sqrt
from operator import mul

def wins(time, distance):
    # invariant: hold * (time - hold) > distance
    # solve: -hold^2 + time*hold - distance = 0
    #        hold = (time +- sqrt(time^2 - 4 * distance)) / 2
    #             = (time +- d) / 2
    # solution: (time - d) / 2 < hold < (time - d) / 2
    d = sqrt(time ** 2 - 4 * distance)
    return int((time + d) / 2) - ceil((time - d) / 2) + 1 - 2 * (d % 1 == 0)

times, distances = (re.findall(r'\d+', line) for line in sys.stdin)
#print(reduce(mul, starmap(wins, zip(map(int, times), map(int, distances))))) # Measure time to execute part 2 only!
print(wins(int(''.join(times)), int(''.join(distances))))
