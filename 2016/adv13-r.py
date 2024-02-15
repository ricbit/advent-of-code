import sys
import aoc
from collections import deque

def iswall(j, i, fav):
  return (i * i + 3 * i + 2 * i * j + j + j * j + fav).bit_count() % 2 == 1

def search(fav):
  vnext = deque([(0, 1, 1)])
  visited = {}
  while vnext:
    score, y, x = vnext.popleft()
    visited[(y, x)] = score
    for j, i in aoc.iter_neigh4(y, x):
      if j >= 0 and i >= 0:
        if not iswall(j, i, fav) and (j, i) not in visited:
          vnext.append((1 + score, j, i))
          visited[(j, i)] = 1 + score
  return visited

fav = int(sys.stdin.read().strip())
scores = search(fav)
aoc.cprint(scores[(39, 31)])
aoc.cprint(sum(steps <= 50 for steps in scores.values()))
