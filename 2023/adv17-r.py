import sys
import aoc
import heapq
from collections import defaultdict

def heuristic(m, y, x, score):
  return m.h - y + m.w - x

def search(m, minsize, maxsize):
  visited = defaultdict(lambda: 1e6)
  vnext = [(heuristic(m, 0, 0, 0), 0, (0, 0), 2)]
  while vnext:
    old_heuristic, score, (y, x), direction = heapq.heappop(vnext)
    if old_heuristic > visited[((y, x), direction)]:
      continue
    if (y, x) == (m.h - 1, m.w - 1):
      return score
    for j, i in m.iter_neigh4(y, x):
      dj, di = j - y, i - x
      if (dj == 0 and direction == 0) or (di == 0 and direction == 1):
        continue
      dscore = 0
      for size in range(1, maxsize + 1):
        nj, ni = y + size * dj, x + size * di
        if not m.valid(nj, ni):
          break
        dscore += m[nj][ni]
        pure_score = score + dscore
        new_heuristic = heuristic(m, nj, ni, pure_score) + pure_score
        vec = ((nj, ni), 0 if dj == 0 else 1)
        if size >= minsize and new_heuristic < visited[vec]:
          heapq.heappush(vnext, (new_heuristic, pure_score) + vec)
          visited[vec] = new_heuristic

lines = [[int(i) for i in line.strip()] for line in sys.stdin]
m = aoc.Table(lines)
print(search(m, 1, 3))
print(search(m, 4, 10))
