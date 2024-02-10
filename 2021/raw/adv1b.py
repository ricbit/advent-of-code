import sys

lines = [int(i) for i in sys.stdin.readlines()]
ans = 0
for a, b, c, d in zip(lines[3:], lines[2:], lines[1:], lines):
  if a + b + c > b + c + d:
    ans += 1
print(ans)
