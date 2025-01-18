import sys
import re
import aoc
from collections import Counter

def find_tiles(lines):
  hit = Counter()
  for line in lines:
    steps = re.findall(r"(w|e|ne|nw|se|sw)", line)
    start = (0, 0)
    for step in steps:
      diff = aoc.HEX2[step]
      start = (start[0] + diff[0], start[1] + diff[1])
    hit[start] ^= 1
  return {c for c, v in hit.items() if v == 1}

def iter_neigh(pos, initial):
  black = 0
  white = set()
  for neigh in aoc.HEX2.values():
    npos = (pos[0] + neigh[0], pos[1] + neigh[1])
    if npos in initial:
      black += 1
    else:
      white.add(npos)
  return black, white

def iterdays(initial):
  for _ in range(100):
    stayblack = set()
    checkwhite = set()
    for pos in initial:
      black, white = iter_neigh(pos, initial)
      checkwhite.update(white)
      if black in [1, 2]:
        stayblack.add(pos)
    for pos in checkwhite:
      black, white = iter_neigh(pos, initial)
      if black == 2:
        stayblack.add(pos)
    initial = stayblack
  return len(initial)

lines = sys.stdin.read().splitlines()
initial = find_tiles(lines)
aoc.cprint(len(initial))
aoc.cprint(iterdays(initial))
