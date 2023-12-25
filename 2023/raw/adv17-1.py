import sys
import re
import itertools
import math
import aoc
import heapq

def search(m):
  pos = (0, 0)
  lastdir = 1J
  lastsize = 0
  visited = set([(pos, lastdir.real, lastdir.imag, lastsize)])
  vnext = [(0, pos, lastdir.real, lastdir.imag, lastsize, [])]
  while vnext:
    score, (y, x), ldr, ldi, lastsize, lastpath = heapq.heappop(vnext)
    print(score, y, x)
    lastdir = ldi * 1J + ldr
    if (y, x) == (m.h - 1, m.w - 1):
      return score, lastpath
    for j, i in m.iter_neigh4(y, x):
      newdir = (y - j) * 1J + (x - i)
      if (j, i) in lastpath:
        continue
      if newdir == lastdir:
        if lastsize < 3:
          vec = ((j, i), newdir.real, newdir.imag, lastsize + 1)
          if vec in visited:
            continue
          heapq.heappush(
              vnext, (score + m[j][i], (j, i), 
              lastdir.real, lastdir.imag, lastsize + 1, lastpath + [(j, i)]))
          visited.add(vec)
      else:
        vec = ((j, i), newdir.real, newdir.imag, 1)
        if vec in visited:
          continue
        heapq.heappush(vnext, (score + m[j][i], (j, i), newdir.real, newdir.imag, 1, lastpath + [(j, i)]))
        visited.add(vec)

lines = [[int(i) for i in line.strip()] for line in sys.stdin]
m = aoc.Table(lines)
for line in m.table:
  print(line)
print(search(m))
