import sys
import re
import itertools
import math
import aoc

m = aoc.Table.read()
tiles = [(-1+0J, 1)]
visited = set()
while tiles:  
  pos, vdir = tiles.pop()
  print(pos, vdir)
  pos += vdir
  x, y = int(pos.real), int(pos.imag)
  vx, vy = int(vdir.real), int(vdir.imag)
  if not m.valid(y, x):
    continue
  print(y, x)
  print (m[y][x])
  if (y,x,vy,vx) in visited:
    continue
  visited.add((y,x,vy,vx))
  if m[y][x] == ".":
    tiles.append((pos, vdir))
  elif m[y][x] == "|":
    if vdir.imag == 0:
      tiles.append((pos, 1J))
      tiles.append((pos, -1J))
    else:
      tiles.append((pos, vdir))
  elif m[y][x] == "-":
    if vdir.real == 0:
      tiles.append((pos, 1))
      tiles.append((pos, -1))
    else:
      tiles.append((pos, vdir))
  elif m[y][x] == "\\":
    if vdir.imag == 0:
      tiles.append((pos, vdir * 1J))
    else:
      tiles.append((pos, vdir * -1J))
  elif m[y][x] == "/":
    if vdir.imag == 0:
      tiles.append((pos, vdir * -1J))
    else:
      tiles.append((pos, vdir * 1J))

v = set([(y,x) for y,x,vy,vx in visited])
ans = 0
for j in range(m.h):
  r = []
  for i in range(m.w):
    if (j, i) in v:
      r.append("*")
      ans += 1
    else:
      r.append(".")
  print("".join(r))
print(ans)
