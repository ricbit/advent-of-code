# Requires python 3.12

import sys
import re
import itertools
import math
import aoc
from dataclasses import dataclass

@dataclass(repr=True, init=True)
class SeedMap:
  delta: int
  begin: int
  end: int

@dataclass(repr=True, init=True)
class Interval:
  begin: int
  end: int

def read_map(lines, pos):
  new_map = []
  while pos + 1 < len(lines) and lines[pos + 1].strip():
    pos += 1
    dst, src, size = [int(i) for i in lines[pos].strip().split()]
    new_map.append(SeedMap(dst - src, src, src + size - 1))
  return pos + 2, new_map

def read_input():
  lines = sys.stdin.readlines()
  seeds = [int(i) for i in lines[0].split(":")[1].split()]
  pos = 2
  maps = []
  while pos < len(lines):
    pos, new_map = read_map(lines, pos)
    new_map.sort(key=lambda x : x.begin)
    maps.append(new_map)
  return seeds, maps

def interval_break(a, seed_map):
  for b in seed_map:
    m = Interval(max(a.begin, b.begin), min(a.end, b.end))
    if m.begin <= m.end:
      if a.begin < m.begin:
        yield Interval(a.begin, m.begin - 1)
      yield Interval(m.begin + b.delta, m.end + b.delta)
      if a.end == m.end:
        return
      a.begin = m.end + 1
  yield a

def transform(seed_intervals, seed_maps):
  begins = []
  for ibegin, isize in seed_intervals:
    intervals = [Interval(ibegin, ibegin + isize - 1)]
    for seed_map in seed_maps:
      new_intervals = []
      for interval in intervals:
        new_intervals.extend(interval_break(interval, seed_map))
      intervals = new_intervals
    begins.extend(i.begin for i in intervals)
  return min(begins)

seeds, maps = read_input()
print(transform(((i, 1) for i in seeds), maps))
print(transform(itertools.batched(seeds, 2), maps))
