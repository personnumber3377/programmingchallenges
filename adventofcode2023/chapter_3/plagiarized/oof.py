import sys

with open(sys.argv[1], 'r') as f:
    engine = [f'.{row}.' for row in f.read().split('\n')]

def get_adjacent(r, c):
    part_numbers = set()
    offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), 
               (0, 1), (1, -1), (1, 0), (1, 1))            
    for x, y in offsets:
        if engine[r + x][c + y].isdigit():
            left_pos = right_pos = c + y
            while engine[r + x][left_pos - 1].isdigit():
                left_pos -= 1
            while engine[r + x][right_pos + 1].isdigit():
                right_pos += 1
            part_numbers.add(int(engine[r + x][left_pos: right_pos + 1]))
    return part_numbers

def parts_list():
    all_parts = []
    for r, row in enumerate(engine):
        for c, symbol in enumerate(row):
            if not symbol.isdigit() and symbol != '.':
                all_parts.append((symbol, get_adjacent(r, c)))
    print("all_parts == "+str(all_parts))
    return all_parts

def AOC_2023_day3_pt1():
    return sum(sum(nums) for _, nums in parts_list())

def AOC_2023_day3_pt2():
    total = 0
    all_numbers = set()

    for symbol, nums in parts_list():
        if symbol == '*' and len(nums) == 2:
            print("Nums: "+str(nums))
            for num in nums:

                all_numbers.add(num)
            
            total += nums.pop() * nums.pop()
    print(all_numbers)
    return total

#print(AOC_2023_day3_pt1())
print(AOC_2023_day3_pt2())
