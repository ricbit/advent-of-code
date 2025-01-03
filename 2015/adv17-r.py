import sys
import functools
import aoc

@functools.lru_cache(maxsize=None)
def count(n, flask, used):
  if n == 0 and not flask and used == 0:
    return 1
  if not flask:
    return 0
  return (count(n - flask[0], tuple(flask[1:]), used - 1) +
          count(n, tuple(flask[1:]), used))

def search(flask):
  for i in range(1, 10):
    if (m := count(150, tuple(flask), i)):
      return m
  return None

flask = [int(line.strip()) for line in sys.stdin]
flask.sort(reverse=True)
aoc.cprint(sum(count(150, tuple(flask), i) for i in range(20)))
aoc.cprint(search(flask))
