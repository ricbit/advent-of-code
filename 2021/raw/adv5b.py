import sys
import itertools

def coord(coords):
  return [int(i) for i in coords.split(",")]

def parse(line):
  coords = line.strip().split("->")
  return [coord(x) for x in coords]

def getmax(i, coord):
  return max(coord[0][i], coord[1][i])

lines = [parse(line) for line in sys.stdin]
maxx = max(getmax(0, line) for line in lines)
maxy = max(getmax(1, line) for line in lines)

def stride(a, b):
  if a == b:
    yield from itertools.repeat(a)
  yield a
  while a != b:
    if b > a:
      a += 1
    elif b < a:
      a -= 1
    yield a

table = [[0] * (maxx + 1) for i in range(maxy + 1)]
for c1, c2 in lines:
  for x, y in zip(stride(c1[0], c2[0]), stride(c1[1], c2[1])):
    table[y][x] += 1

count = 0
for yline in table:
  for elem in yline:
    if elem >= 2:
      count += 1
print(count)
