import sys
import math
import aoc
import functools

@functools.lru_cache()
def choose(n, pos, chosen, packs, goal):
  if n == goal:
    yield chosen
    return
  if pos >= len(packs) or n > goal:
    return
  if n + sum(packs[pos:]) < goal:
    return
  if len(chosen) < 7:
    yield from choose(n + packs[pos], pos + 1, chosen + (packs[pos],), packs, goal)
  yield from choose(n, pos + 1, chosen, packs, goal)

def quantum(sol):
  return len(sol), math.prod(sol)

packs = [int(line.strip()) for line in sys.stdin]
packs.sort(reverse=True)
goal = sum(packs) // 3
aoc.cprint(min(quantum(x) for x in choose(0, 0, tuple(), tuple(packs), goal))[1])
goal = sum(packs) // 4
aoc.cprint(min(quantum(x) for x in choose(0, 0, tuple(), tuple(packs), goal))[1])
  
