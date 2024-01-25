import sys
import aoc

DIR = aoc.get_cdir("U")

def solve(cmd):
  pos, dist = 0, 1
  visited = {}
  for c in cmd:
    for i in range(int(c[1:])):
      pos += DIR[c[0]]
      visited[pos] = dist
      dist += 1
  return visited

def intersect(path):
  return set(path[0].keys()).intersection(set(path[1].keys()))

def part2(inter):
  for pos in inter:
    yield path[0][pos] + path[1][pos]

def part1(inter):
  for pos in inter:
    yield int(abs(pos.real) + abs(pos.imag))

path = [solve(line.strip().split(",")) for line in sys.stdin]
inter = intersect(path)
aoc.cprint(min(part1(inter)))
aoc.cprint(min(part2(inter)))
