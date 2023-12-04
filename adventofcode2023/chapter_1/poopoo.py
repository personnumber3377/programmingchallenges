import sys

f = lambda str, dir: min((str[::dir].find(num[::dir])%99, i) for i, num in enumerate(
    '1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine'.split()))[1]%9+1

print(sum(10*f(x, 1) + f(x, -1) for x in open(sys.argv[1])))