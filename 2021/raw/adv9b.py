import sys
import math

floor = [[int(i) for i in line.strip()] for line in sys.stdin]
h, w = len(floor), len(floor[0])

def neigh(y, x):
  if x > 0: yield (y, x - 1)
  if x < w - 1: yield (y, x + 1)
  if y > 0: yield (y - 1, x)
  if y < h - 1: yield (y + 1, x)

def floorxy(y, x):
  return floor[y][x]

def floodfill(y, x, used):
  nextstep = set([(y, x)])
  used[y][x] = True
  ans = 1
  while nextstep:
    y, x = nextstep.pop()
    for j, i in neigh(y, x):
      if not used[j][i] and floor[j][i] != 9:
        used[j][i] = True
        nextstep.add((j, i))
        ans += 1
  return ans

regions = []
used = [[False] * w for i in range(h)]
for y in range(h):
  for x in range(w):
    if not used[y][x] and floor[y][x] != 9:
      regions.append(floodfill(y, x, used))
regions.sort(reverse=True)
print(math.prod(regions[:3]))
    
