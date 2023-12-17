import sys
import aoc
import heapq

def search(m, minsize, maxsize):
  pos = (0, 0)
  lastdir = (2, 2)
  lastsize = 5
  vec = (pos, lastdir, lastsize)
  visited = set([vec])
  vnext = [(0,) + vec]
  while vnext:
    score, (y, x), (dy, dx), lastsize = heapq.heappop(vnext)
    if (y, x) == (m.h - 1, m.w - 1):
      return score
    for j, i in m.iter_neigh4(y, x):
      dj, di = y - j, x - i
      if (dj, di) == (dy, dx):
        if lastsize >= maxsize:
          continue
        if (vec := ((j, i), (dj, di), lastsize + 1)) in visited:
          continue
      else:
        if lastsize < minsize or (dj, di) == (-dy, -dx):
          continue
        if (vec := ((j, i), (dj, di), 1)) in visited:
          continue
      heapq.heappush(vnext, (score + m[j][i],) + vec)
      visited.add(vec)

lines = [[int(i) for i in line.strip()] for line in sys.stdin]
m = aoc.Table(lines)
print(search(m, 0, 3))
print(search(m, 4, 10))
