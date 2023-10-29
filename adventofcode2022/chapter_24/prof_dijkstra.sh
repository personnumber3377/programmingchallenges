#!/bin/sh

#python3.8 -m cProfile -s cumtime naive_part1.py < tiny_example.txt
python3.9 -m cProfile -s tottime dijkstra.py < part_1_input.txt

#part_1_input.txt