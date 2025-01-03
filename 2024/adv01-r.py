import aoc
from collections import Counter

t = aoc.transpose(aoc.ints_read())
t[0].sort()
t[1].sort()
aoc.cprint(sum(abs(a - b) for a, b in zip(*t)))

hist = Counter(t[1])
aoc.cprint(sum(a * hist[a] for a in t[0]))
