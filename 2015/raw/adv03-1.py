import itertools
import aoc
import sys

def walk(data, size):
  visited = set([0])
  dirs = aoc.get_cdir(">")
  pos = [0] * size
  for vdir in itertools.batched(data, size):
    for i in range(size):
      pos[i] += dirs[vdir[i]]
      visited.add(pos[i])
  return len(visited)

data = sys.stdin.read().strip()
aoc.cprint(walk(data, 1))
aoc.cprint(walk(data, 2))
