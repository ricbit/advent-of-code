import re
import sys

ans1, ans2 = 0, 0
for line in sys.stdin:
  a, b, c = [int(g) for g in re.match(r"^(\d+)x(\d+)x(\d+)", line).groups()]
  perimeters = [2 * i for i in [a + b, a + c, b + c]]
  ans1 += min(perimeters) + a * b * c
  areas = [a * b, a * c, b * c]
  ans2 += 2 * sum(areas) + min(areas)
print(ans)


