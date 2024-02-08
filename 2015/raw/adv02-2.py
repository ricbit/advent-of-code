import re
import sys

ans = 0
for line in sys.stdin:
  a, b, c = [int(g) for g in re.match(r"^(\d+)x(\d+)x(\d+)", line).groups()]
  perimeters = [2 * i for i in [a + b, a + c, b + c]]
  ans += min(perimeters) + a * b * c
print(ans)


