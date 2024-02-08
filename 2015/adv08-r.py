import sys
import aoc

def count(lines):
  ans = 0
  for line in lines:
    inside = line[1:-1]
    chars = 0
    pos = 0
    while pos < len(inside):
      chars += 1
      if inside[pos] == "\\":
        if inside[pos + 1] == "x":
          pos += 4
        else:
          pos += 2
      else:
        pos += 1
    ans += len(line) - chars
  return ans

def count2(lines):
  for line in lines:
    yield line.count("\\") + line.count("\"") + 2

lines = sys.stdin.readlines()
aoc.cprint(count(lines))
aoc.cprint(sum(count2(lines)))
