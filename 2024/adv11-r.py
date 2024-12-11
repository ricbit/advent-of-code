import sys
import aoc
import functools

@functools.lru_cache(None)
def rec(stone, depth):
  if depth == 0:
    return 1
  else:
    if stone == 0:
      value = rec(1, depth - 1)
    elif (x := len(s := str(stone))) % 2 == 0:
      value = rec(int(s[:x // 2]), depth - 1)
      value += rec(int(s[x // 2:]), depth - 1)
    else:
      value = rec(stone * 2024, depth -1)
  return value

def solve(stones, depth):
  return sum(rec(stone, depth) for stone in stones)

stones = aoc.ints(sys.stdin.read().split())
aoc.cprint(solve(stones, 25))
aoc.cprint(solve(stones, 75))
