import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def toint(c):
  return (c.imag, c.real)

def solve(t):
  sy, sx = t.find("S")
  ey, ex = t.find("E")
  t[sy][sx] = "."
  t[ey][ex] = "."
  pos = sy * 1j + sx
  end = ey * 1j + ex
  pnext = [(0, toint(pos), toint(1), [])]
  visited = aoc.ddict(lambda: [1e10, set()])
  best = None
  while pnext:
    score, pos, pdir, path = heapq.heappop(pnext)
    if best is not None and score > best:
      continue
    pos = pos[0] * 1j + pos[1]
    pdir = pdir[0] * 1j + pdir[1]
    state = (pos, pdir)
    if score < visited[state][0]:
      visited[state] = [score, set(path)]
    elif score == visited[state][0]:
      visited[state][1].update(set(path))
    else:
      continue
    if pos == end:
      if best is None:
        best = score    
    for turn in [1j, -1j]:
      if score + 1000 > visited[(pos, pdir * turn)][0]:
        continue
      heapq.heappush(pnext, (score + 1000, toint(pos), toint(pdir * turn), 
        path + [(toint(pos), toint(pdir * turn))]))
    if t.get(pos + pdir) != "#":
      if score + 1 > visited[(pos + pdir, pdir)][0]:
        continue
      heapq.heappush(pnext, (score + 1, toint(pos + pdir), toint(pdir),
        path + [(toint(pos + pdir), toint(pdir))]))
  # --
  ans = set()
  for pdir in [1,-1,1j,-1j]:
    v = visited[(end, pdir)]
    if len(v[1]) > 0:
      print(v[0], len(v[1]))
      pos = set(p for p, pd in v[1])
      ans.update(pos)
      for j in range(t.h):
        line = []
        for i in range(t.w):
          line.append("O" if (j, i) in pos else t[j][i])
        print("".join(line))
  return len(ans)

data = aoc.Table.read()
aoc.cprint(solve(data))
