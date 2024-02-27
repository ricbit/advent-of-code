import sys
import aoc

def walk1(layers):
  m = max(layers)
  x = [0] * (m + 1)
  d = [1] * (m + 1)
  ans = 0
  for i in range(m + 1):
    if x[i] == 0 and i in layers:
      ans += i * layers[i]
    for j in range(m + 1):
      if j in layers:
        x[j] += d[j]
        if x[j] >= layers[j]:
          x[j] = layers[j] - 2
          d[j] *= -1
        if x[j] < 0:
          x[j] = 1
          d[j] *= -1
  return ans

def ypos(size, time):
  yoyo = size + size - 2
  t = time % yoyo
  if t < size:
    return t
  else:
    return yoyo - t

def walk2(x, time, layers):
  for i, size in layers.items():
    x[i] = ypos(size, time)

def canwalk(series, layers, m, offset):
  return all(series[(i + offset) % m][i] != 0 for i in range(m))

def walkseries(layers):
  m = max(layers) + 1
  series = [[1] * m for _ in range(m)]
  for i in range(m):
    walk2(series[i], i, layers)
  delay = 0
  while True:
    if canwalk(series, layers, m, delay):
      return delay
    walk2(series[delay % m], delay + m, layers)
    delay += 1

lines = [line.strip() for line in sys.stdin]
layers = {}
for line in lines:
  index, value = aoc.ints(line.split(": "))
  layers[index] = value
aoc.cprint(walk1(layers))
aoc.cprint(walkseries(layers))
