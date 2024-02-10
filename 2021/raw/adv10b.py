import sys

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

SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}

lines = [line.strip() for line in sys.stdin]
ans = []
for line in lines:
  left, last = parse(line)
  if last is None:
    points = 0
    for c in reversed(left):
      points = points * 5 + SCORE[c]
    ans.append(points)
ans.sort()
print(ans[len(ans) // 2])
