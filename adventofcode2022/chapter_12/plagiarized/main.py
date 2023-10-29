import collections
import sys

#filename = 'puzzle.txt'

#with open(filename, 'r') as file:
data = [[l for l in line] for line in sys.stdin.read().strip().split()]


def get_adjacent(current: (int, int), cols, rows) -> [(int, int)]:
    col, row = current

    match current:
        case (0, 0):
            return [(0, 1), (1, 0)]
        case (0, x):
            return [(col, row - 1), (col + 1, row)] if x == rows - 1 else [(col, row - 1), (col + 1, row),
                                                                           (col, row + 1)]
        case (y, 0):
            return [(col - 1, row), (col, row + 1)] if y == cols - 1 else [(col - 1, row), (col, row + 1),
                                                                           (col + 1, row)]
        case _:
            if current == (cols - 1, rows - 1):
                return [(col, row - 1), (col - 1, row)]
            elif col == cols - 1:
                return [(col, row - 1), (col - 1, row), (col, row + 1)]
            elif row == rows - 1:
                return [(col, row - 1), (col - 1, row), (col + 1, row)]
            else:
                return [(col, row - 1), (col - 1, row), (col, row + 1), (col + 1, row)]


def bfs(root: (int, int), searched: (int, int), input_data: [[str]]) -> int:
    values = {chr(i): i - 96 for i in range(97, 97 + 26)}
    values['S'] = 1
    values['E'] = 26

    queue, visited = collections.deque(), set()
    queue.append([root])

    while queue:
        path = queue.popleft()
        row, col = path[-1]
        current_height = values[input_data[row][col]]

        if (row, col) not in visited:
            visited.add((row, col))

            if (row, col) == searched:
                return len(path) - 1

            for vertex in get_adjacent((row, col), len(input_data), len(input_data[0])):
                vertex_row, vertex_col = vertex
                vertex_height = values[input_data[vertex_row][vertex_col]]

                if vertex_height <= current_height + 1:
                    path_copy = path[:]
                    path_copy.append(vertex)
                    queue.append(path_copy)


starting, ending = None, None

for r, line in enumerate(data):
    if 'S' in line:
        starting = (r, line.index('S'))

    if 'E' in line:
        ending = (r, line.index('E'))

print(f"Part 1 - %d" % bfs(starting, ending, data))

#starts = set((row, col) for row in range(len(data)) for col in range(len(data[0])) if data[row][col] == 'a')
#distances = [distance for start in starts if (distance := bfs(start, ending, data)) is not None]

#print(f"Part 2 - %d" % min(distances))

