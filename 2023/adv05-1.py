import sys
import re
import itertools
import math

def read_map(lines, pos):
  name = re.match(r"^(\w+)-to-(\w+)", lines[pos]).groups()
  pos += 1
  new_map = []
  while pos < len(lines):
    line = lines[pos]
    if not line.strip():
      return pos + 1, new_map
    numbers = [int(i) for i in line.strip().split()]
    new_map.append(numbers)
    pos += 1
  return pos, new_map

lines = sys.stdin.readlines()
seeds = [int(i) for i in lines[0].split(":")[1].split()]
pos = 2
maps = []
while pos < len(lines):
  pos, new_map = read_map(lines, pos)
  maps.append(new_map)

def convert(seed, amap):
  for dst, src, size in amap:
    if src <= seed < src + size:
      return seed - src + dst
  return seed

dsts = []
for seed in seeds:
  for amap in maps:
    a = convert(seed, amap)
    seed = a
  dsts.append(seed)

print(min(dsts))
  

