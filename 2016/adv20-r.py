import sys
import aoc

def black(blist, source):
  valid = [source]
  for res in blist:
    new = []
    for v in valid:
      for i in v.sub(res):
        new.append(i)
    valid = new
  return valid[0].begin, sum(len(i) for i in valid)

intervals = []
for line in sys.stdin:
  a, b = map(int, line.split("-"))
  intervals.append(aoc.Interval(a, b))
ans1, ans2 = black(intervals, aoc.Interval(0, 0xFFFFFFFF))
aoc.cprint(ans1)
aoc.cprint(ans2)
  
