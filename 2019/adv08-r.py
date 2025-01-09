import sys
import aoc

mx, my = 25, 6

def get(layers, y, x):
  for layer in layers:
    c = layer[y * mx + x]
    if c != "2":
      return "." if c == "0" else "#"
  return "0"

data = sys.stdin.read().strip()
layers = []
size = mx * my
for i in range(len(data) // size):
  layers.append(data[size * i:size * i + size])

m = min(layers, key=lambda x: x.count("0"))
aoc.cprint(m.count("1") * m.count("2"))

for j in range(my):
  line = []
  for i in range(mx):
    line.append(get(layers, j, i))
  print("".join(line))
