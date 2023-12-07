import sys

FILE = sys.argv[1]

with open(FILE) as f:
    sum_of_powers = 0
    
    for line in f.readlines():
        cube_sets = line.strip().split(": ")[1].split("; ")
        bag = {'red': 0, 'green': 0, 'blue': 0}

        for cube_set in cube_sets:
            cubes = cube_set.split(", ")
            for cube in cubes:
                count, color = cube.split(" ")
                bag[color] = max(bag[color], int(count))

        sum_of_powers += bag['red'] * bag['green'] * bag['blue']

    print(sum_of_powers)