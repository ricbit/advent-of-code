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

SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}

lines = [line.strip() for line in sys.stdin]
ans = 0
for line in lines:
  left, last = parse(line)
  if last is not None:
    ans += SCORE[last]
print(ans)
