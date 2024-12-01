import sys
import aoc

t = aoc.transpose(aoc.ints_read())
t[0].sort()
t[1].sort()
aoc.cprint(sum(abs(a - b) for a, b in zip(t[0], t[1])))

hist = aoc.histogram(t[1])
aoc.cprint(sum(a * hist[a] for a in t[0]))


