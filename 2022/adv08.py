import sys

grid = [[int(i) for i in line.strip()] for line in sys.stdin]
y, x = len(grid), len(grid[0])
visible = [[False] * x for _ in range(y)]

def valid(pos):
  return 0 <= pos[0] < y and 0 <= pos[1] < x

def walk(start, direction):
  j, i = start
  dj, di = direction
  visible[j][i] = True
  current = grid[j][i]
  while valid((j + dj, i + di)):
    j += dj
    i += di
    if grid[j][i] > current:
      current = grid[j][i]
      visible[j][i] = True

def first():
  for j in range(y):
    walk((j, 0), (0, 1))
    walk((j, x - 1), (0, -1))
  for i in range(x):
    walk((0, i), (1, 0))
    walk((y - 1, i), (-1, 0))
  return sum(sum(line) for line in visible)

def traverse(j, i, dj, di, base):
  count = 0
  while valid((j + dj, i + di)):
    j, i = j + dj, i + di
    count += 1
    if grid[j][i] >= base:
      break
  return count 

def view(j, i):
  base = grid[j][i]
  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  value = 1
  for dj, di in dirs:
    value *= traverse(j, i, dj, di, base)
  return value

def second():
  best = 0
  for j in range(y):
    for i in range(x):
      best = max(best, view(j, i))
  return best      

print(first())
print(second())
