import sys
import aoc

def count(fuel, recursive=False):
  a = fuel // 3 - 2
  if recursive:
    return a + count(a, recursive) if a > 0 else 0
  return a

def count_all(data, recursive=False):
  return sum(count(int(line), recursive) for line in data)

data = [line.strip() for line in sys.stdin]
aoc.cprint(count_all(data, False))
aoc.cprint(count_all(data, True))
