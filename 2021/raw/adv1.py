import sys

lines = [int(i) for i in sys.stdin.readlines()]
ans = 0
for a, b in zip(lines[1:], lines):
  if a > b:
    ans += 1
print(ans)
