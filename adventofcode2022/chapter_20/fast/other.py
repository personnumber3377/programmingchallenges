xs = [*enumerate(int(x) * 811589153 for x in open('input.txt'))]
for x in xs * 10:
    xs.pop(j := xs.index(x))
    xs.insert((j+x[1]) % len(xs), x)
xs = [x for _,x in xs]
print(sum(xs[(xs.index(0)+1000*p) % len(xs)] for p in [1,2,3]))