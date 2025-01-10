import sys
import aoc
import functools
import multiprocessing

def empty(opensize, groups):
  if opensize > 0:
    return int(groups == (opensize, ))
  else:
    return int(not groups)

def dot(springs, opensize, groups):
  if opensize > 0:
    if groups and groups[0] == opensize:
      return count(springs[1:].lstrip("."), 0, groups[1:])
    return 0
  else:
    return count(springs[1:].lstrip("."), 0, groups)

def sharp(springs, opensize, groups):
  return count(springs[1:], opensize + 1, groups)

@functools.lru_cache(maxsize=None)
def count(springs, opensize, groups):
  if not springs:
    return empty(opensize, groups)
  if len(groups) > len(springs):
    return 0
  if groups and opensize > groups[0]:
    return 0
  if springs[0] == ".":
    return dot(springs, opensize, groups)
  if springs[0] == "#":
    return sharp(springs, opensize, groups)
  if springs[0] == "?":
    return dot(springs, opensize, groups) + sharp(springs, opensize, groups)

def unfold_line(line, n):
  springs, groups = line.strip().split()
  groups = tuple(int(i) for i in groups.split(","))
  return count("?".join([springs] * n), 0, groups * n)

def unfold(lines, n, pool):
  return sum(pool.starmap(unfold_line, ((line, n) for line in lines)))

lines = sys.stdin.readlines()
with multiprocessing.Pool() as pool:
  aoc.cprint(unfold(lines, 1, pool))
  aoc.cprint(unfold(lines, 5, pool))
