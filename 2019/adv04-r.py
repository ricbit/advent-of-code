import sys
import itertools
import aoc

def same(pwd):
  for a, b in zip(pwd, pwd[1:]):
    yield a == b

def same2(pwd):
  for k, v in itertools.groupby(pwd):
    yield len(list(v)) == 2

data = aoc.ints(sys.stdin.read().strip().split("-"))
ans1, ans2 = 0, 0
for pwd in range(data[0], 1 + data[1]):
  spwd = list(str(pwd))
  if spwd == list(sorted(spwd)):
    if any(same(spwd)):
      ans1 += 1
    if any(same2(spwd)):
      ans2 += 1
aoc.cprint(ans1)
aoc.cprint(ans2)
