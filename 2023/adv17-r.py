import sys
import aoc
import heapq
import cProfile

def heuristic(m, y, x):
  return m.h - y + m.w - x

def search(m, minsize, maxsize):
  pos = (0, 0)
  lastdir = (2, 2)
  vec = (pos, lastdir)
  visited = set()
  current = {}
  vnext = [(heuristic(m, 0, 0), 0) + vec]
  count = 0
  skipped = 0
  while vnext:
    count += 1
    old_heuristic, score, (y, x), (dy, dx) = heapq.heappop(vnext)
    if (oldvec := ((y, x), (dy, dx))) in visited:
      skipped += 1
      continue
    visited.add(oldvec)
    if (y, x) == (m.h - 1, m.w - 1):
      print(count, skipped)
      return score
    for j, i in m.iter_neigh4(y, x):
      dj, di = j - y, i - x
      if (dj, di) == (dy, dx) or (dj, di) == (-dy, -dx):
        continue
      dscore = 0
      for size in range(1, maxsize + 1):
        nj, ni = y + size * dj, x + size * di
        if not m.valid(nj, ni):
          break
        dscore += m[nj][ni]
        if size < minsize or (vec := ((nj, ni), (dj, di))) in visited:
          continue
        pure_score = score + dscore
        new_heuristic = heuristic(m, nj, ni) + pure_score
        if new_heuristic < current.get(vec, 1e9):
          heapq.heappush(vnext, (new_heuristic, pure_score) + vec)
          current[vec] = new_heuristic

lines = [[int(i) for i in line.strip()] for line in sys.stdin]
m = aoc.Table(lines)
print(search(m, 1, 3))
print(search(m, 4, 10))
