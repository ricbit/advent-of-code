import re
import sys
import aoc

boxes = aoc.retuple_read("a_ b_ c_", r"^(\d+)x(\d+)x(\d+)", sys.stdin)
ans1, ans2 = 0, 0
for box in boxes:
  a, b, c = box
  perimeters = [2 * i for i in [a + b, a + c, b + c]]
  ans2 += min(perimeters) + a * b * c
  areas = [a * b, a * c, b * c]
  ans1 += 2 * sum(areas) + min(areas)
aoc.cprint(ans1)
aoc.cprint(ans2)
