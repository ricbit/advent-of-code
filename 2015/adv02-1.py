import re
import sys

ans = 0
for line in sys.stdin:
  a, b, c = [int(g) for g in re.match(r"^(\d+)x(\d+)x(\d+)", line).groups()]
  areas = [a * b, a * c, b * c]
  ans += 2 * sum(areas) + min(areas)
print(ans)


