import sys
import aoc

close = {"]": "[", "}": "{", ">": "<", ")": "("}

def parse(line):
  left = []
  for c in line:
    if c not in close:
      left.append(c)
    else:
      if left[-1] == close[c]:
        left.pop()
      else:
        return (left, c)
  return (left, None)

SCORE1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
SCORE2 = {"(": 1, "[": 2, "{": 3, "<": 4}

lines = [line.strip() for line in sys.stdin]
ans = []
total = 0
for line in lines:
  left, last = parse(line)
  if last is not None:
    total += SCORE1[last]
  else:
    points = 0
    for c in reversed(left):
      points = points * 5 + SCORE2[c]
    ans.append(points)
ans.sort()
aoc.cprint(total)
aoc.cprint(ans[len(ans) // 2])
