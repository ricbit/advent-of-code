import sys

h, v = 0, 0
for line in sys.stdin:
  cmd, dist = line.strip().split()
  dist = int(dist)
  if cmd == "forward":
    h += dist
  elif cmd == "down":
    v += dist
  elif cmd == "up":
    v -= dist
print(h * v)

