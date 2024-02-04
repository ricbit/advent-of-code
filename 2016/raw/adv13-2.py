import sys
import re
import itertools
import math
import aoc
from collections import *

def iswall(j, i, fav):
  return (i * i + 3 * i + 2 * i * j + j + j * j + fav).bit_count() % 2 == 1

def search(fav, goal):
  vnext = deque([(0, 1, 1)])
  visited = set()
  ans = 0
  while vnext:
    score, y, x = vnext.popleft()
    ans += 1
    visited.add((y, x))
    for dj, di in aoc.DIRECTIONS.values():
      j, i = y + dj, x + di
      if j >= 0 and i >= 0:
        if not iswall(j, i, fav)  and (j, i) not in visited and score < 50:
          vnext.append((1 + score, j, i))
          visited.add((j, i))
  return ans

fav = int(sys.stdin.read().strip())
#fav = 10
#for j in range(10):
#  print("".join(("#" if iswall(j,i,fav) else ".") for i in range(10)))
#aoc.cprint(search(10, (4, 7)))
aoc.cprint(search(fav, (39, 31)))
