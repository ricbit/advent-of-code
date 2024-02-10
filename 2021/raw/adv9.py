import sys

floor = [[int(i) for i in line.strip()] for line in sys.stdin]
h, w = len(floor), len(floor[0])

def neigh(y, x):
  if x > 0: yield (y, x - 1)
  if x < w - 1: yield (y, x + 1)
  if y > 0: yield (y - 1, x)
  if y < h - 1: yield (y + 1, x)

def floorxy(y, x):
  return floor[y][x]

ans = 0
for y in range(h):
  for x in range(w):
    if all(floorxy(j, i) > floor[y][x] for j, i in neigh(y, x)):
      ans += 1 + floor[y][x]

print(ans)
