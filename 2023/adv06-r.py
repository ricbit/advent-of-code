import sys
import re
import itertools
import math
import multiprocessing

lines = sys.stdin.readlines()
time = lines[0].split(":")[1].split()
distance = lines[1].split(":")[1].split()

def count_wins(time, distance):
  a = math.ceil((time - (time ** 2 - 4 * distance) ** 0.5) / 2 + 1e-3)
  b = math.floor((time + (time ** 2 - 4 * distance) ** 0.5) / 2 - 1e-3)
  return b - a + 1

print(math.prod(count_wins(int(t), int(d)) for t, d in zip(time, distance)))
print(count_wins(int("".join(time)), int("".join(distance))))

  
