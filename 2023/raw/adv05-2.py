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
  new_map.sort(key=lambda x:x[1])
  maps.append(new_map)

def convert(seed, amap):
  for dst, src, size in amap:
    if src <= seed < src + size:
      return seed - src + dst
  return seed

def interval_break(abegin, aend, amap):
  intervals = []
  for dst, src, mapsize in amap:
    bbegin, bend = src, src + mapsize - 1
    mbegin, mend = max(abegin, bbegin), min(aend, bend)
    if mbegin <= mend:
      delta = dst - src
      if abegin < mbegin:
        yield (abegin, mbegin - 1)
      yield (mbegin + delta, mend + delta)
      if aend == mend:
        return
      abegin = mend + 1
  yield (abegin, aend)

dsts = []
for start, size in itertools.batched(seeds, 2):
  intervals = [(start, start + size - 1)]
  for amap in maps:
    new_intervals = []
    for abegin, aend in intervals:
      new_intervals.extend(interval_break(abegin, aend, amap))
    intervals = new_intervals
  dsts.extend(i[0] for i in intervals)

print(min(dsts))
  

