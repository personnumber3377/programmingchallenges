import numpy as np
import math
from functools import reduce
from heapq import heappush, heappop
with open("part_1_input.txt") as fh:
    data = fh.read()
testdata = """\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""
def blizzard_list(data):
    lines = data.strip().splitlines()
    h, w = len(lines) - 2, len(lines[0]) - 2
    north, south, east, west, empty = [np.zeros((h, w), dtype=bool) for _ in range(5)]
    drxnmap = {
        "^": north,
        "v": south,
        ">": east,
        "<": west,
        ".": empty,
    }
    for row, line in enumerate(lines[1:-1]):
        for col, char in enumerate(line[1:-1]):
            drxnmap[char][row, col] = True
    del empty

    header = np.ones((1, w), dtype=bool)
    header[0, 0] = False
    footer = np.ones((1, w), dtype=bool)
    footer[0, -1] = False

    L = []
    for _ in range(math.lcm(h, w)):
        bliz = reduce(np.logical_or, [north, south, east, west])
        L.append(np.vstack([header, bliz, footer]))

        north = np.vstack([north[1:], north[:1]])
        south = np.vstack([south[-1:], south[:-1]])
        east = np.hstack([east[:, -1:], east[:, :-1]])
        west = np.hstack([west[:, 1:], west[:, :1]])

    return L


def open_spots(coords, ar):
    r0, c0 = coords
    L = []
    for (r, c) in [(r0, c0), (r0+1, c0), (r0-1, c0), (r0, c0+1), (r0, c0-1)]:
        if r < 0 or c < 0:
            continue
        try:
            v = ar[r, c]
        except IndexError:
            pass
        else:
            if not v:
                L.append((r, c))
    return L

'''
def dijkstra(data, start=(0, 0), finish=None, initial_state=0):
    states = blizzard_list(data)
    if finish is None:
        h, w = states[0].shape
        finish = (h-1, w-1)
    visited = {(start, initial_state): 0}
    pq = []
    heappush(pq, (0, start, initial_state))
    while pq:
        (d, p, s) = heappop(pq)
        if p == finish:
            return d
        next_s = (s + 1) % len(states)
        next_d = d + 1
        for spot in open_spots(p, states[next_s]):
            v = visited.get((spot, next_s))
            if v is None or v > next_d:
                visited[(spot, next_s)] = next_d
                heappush(pq, (next_d, spot, next_s))
'''


def dijkstra(data, start=(0, 0), finish=None, initial_state=0):
    states = blizzard_list(data)
    if finish is None:
        h, w = states[0].shape
        finish = (h-1, w-1)
    visited = {(start, initial_state): 0}
    pq = []
    count = 0
    print_count_gap = 100
    heappush(pq, (0, start, initial_state))
    while pq:
        if count % print_count_gap:
            print("count == "+str(count))
            print("len(pq) == "+str(len(pq)))
        (d, p, s) = heappop(pq)
        if p == finish:
            return d
        next_s = (s + 1) % len(states)
        next_d = d + 1
        for spot in open_spots(p, states[next_s]):
            v = visited.get((spot, next_s))
            if v is None or v > next_d:
                visited[(spot, next_s)] = next_d
                heappush(pq, (next_d, spot, next_s))
        count += 1


if __name__=="__main__":

    print(dijkstra(data))


