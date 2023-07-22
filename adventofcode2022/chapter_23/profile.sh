#!/bin/sh


python3.8 -m cProfile -s tottime optimization.py < actual.txt > profile.out


