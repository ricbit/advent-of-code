import sys

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

table = [[0] * (maxx + 1) for i in range(maxy + 1)]
for c1, c2 in lines:
  if c1[0] == c2[0]:
    for y in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
      table[y][c1[0]] += 1
  elif c1[1] == c2[1]:
    for x in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
      table[c1[1]][x] += 1

count = 0
for yline in table:
  for elem in yline:
    if elem >= 2:
      count += 1
print(count)
