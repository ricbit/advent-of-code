import sys
import itertools
import aoc

def find_antennas(t):
  pos = aoc.ddict(list)
  for j, i in t.iter_all():
    if t[j][i] != '.':
      pos[t[j][i]].append(j * 1j + i)
  return pos

def part1(t, antennas):
  anti = set()
  for k, v in antennas.items():
    for a, b in itertools.combinations(v, 2):
      d = b - a
      for i in [2, -1]:
        if t.cvalid(a + i * d):
          anti.add(a + i * d)
  return len(anti)

def part2(t, antennas):
  anti = set()
  for k, v in antennas.items():
    for a, b in itertools.combinations(v, 2):
      d = b - a
      for i in itertools.count(0):
        if t.cvalid(a + i * d):
          anti.add(a + i * d)
        else:
          break
      for i in itertools.count(-1, -1):
        if t.cvalid(a + i * d):
          anti.add(a + i * d)
        else:
          break 
  return len(anti)

t = aoc.Table.read()
antennas = find_antennas(t)
aoc.cprint(part1(t, antennas))
aoc.cprint(part2(t, antennas))
