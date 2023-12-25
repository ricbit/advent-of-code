import sys
import re
import itertools
import math

lines = sys.stdin.readlines()
times = lines[0].split(":")[1].split()
distances = lines[1].split(":")[1].split()

def wins(time, distance):
  a = math.floor((time ** 2 - 4 * distance) ** 0.5 / 2)
  b = math.ceil((time ** 2 - 4 * distance) ** 0.5 / 2)
  return a + b

print(wins(int("".join(times)), int("".join(distances))))
