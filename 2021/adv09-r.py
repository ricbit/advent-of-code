import sys
import math
import aoc

floor = aoc.Table([aoc.ints(line.strip()) for line in sys.stdin])

def floorxy(y, x):
  return floor[y][x]

def floodfill(y, x, used):
  nextstep = set([(y, x)])
  used[y][x] = True
  ans = 1
  while nextstep:
    y, x = nextstep.pop()
    for j, i in floor.iter_neigh4(y, x):
      if not used[j][i] and floor[j][i] != 9:
        used[j][i] = True
        nextstep.add((j, i))
        ans += 1
  return ans

regions = []
used = [[False] * floor.w for i in range(floor.h)]
low_points = 0
for y, x in floor.iter_all():
  if all(floor[j][i] > floor[y][x] for j, i in floor.iter_neigh4(y, x)):
      low_points += 1 + floor[y][x]
  if not used[y][x] and floor[y][x] != 9:
    regions.append(floodfill(y, x, used))
regions.sort(reverse=True)
aoc.cprint(low_points)
aoc.cprint(math.prod(regions[:3]))
    
