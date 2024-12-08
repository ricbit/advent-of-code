import sys
import itertools
import aoc

def find_antennas(t):
  pos = aoc.ddict(list)
  for j, i in t.iter_all():
    if t[j][i] != '.':
      pos[t[j][i]].append(j * 1j + i)
  return pos

def find_antinodes(t, antennas, directions):
  anti = set()
  for positions in antennas.values():
    for a, b in itertools.combinations(positions, 2):
      d = b - a
      for direction in directions():
        for i in direction:
          if t.cvalid(a + i * d):
            anti.add(a + i * d)
          else:
            break
  return len(anti)

def part1(t, antennas):
  return find_antinodes(t, antennas, lambda: [[2], [-1]])

def part2(t, antennas):
  directions = lambda: [itertools.count(0), itertools.count(-1, -1)]
  return find_antinodes(t, antennas, directions)

t = aoc.Table.read()
antennas = find_antennas(t)
aoc.cprint(part1(t, antennas))
aoc.cprint(part2(t, antennas))
