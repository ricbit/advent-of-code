import sys

h, v, aim = 0, 0, 0
for line in sys.stdin:
  cmd, dist = line.strip().split()
  dist = int(dist)
  if cmd == "forward":
    h += dist
    v += dist * aim
  elif cmd == "down":
    aim += dist
  elif cmd == "up":
    aim -= dist
print(h * v)

