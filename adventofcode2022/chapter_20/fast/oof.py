import itertools
lut = {tag: n * 811589153 for tag, n in enumerate(int(l) for l in open("input.txt"))}
tags = list(lut.keys())
for _, (tag, n) in itertools.product(range(10), lut.items()):
    #print("tag == "+str(tag))
    #print("n == "+str(n))
    #print("indexes == "+str(tags))
    tags.pop(idx := tags.index(tag))
    #print("a_index == "+str(idx))
    #print("b_index == "+str((idx + n) % len(tags)))
    tags.insert((idx + n) % len(tags), tag)
nums = [lut[t] for t in tags]
#print("numbers list final: "+str(nums))
print(sum(nums[(nums.index(0) + o) % len(nums)] for o in [1000, 2000, 3000]))
