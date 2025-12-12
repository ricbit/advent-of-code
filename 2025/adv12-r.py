import aoc

data = aoc.line_blocks()
shapes = ["".join(b[1:]).count("#") for b in data[:-1]]
gifts = data[-1]
ans = 0
for line in gifts:
  gift = aoc.retuple("x_ y_ spec", r"(\d+)x(\d+): (.*)$", line)
  amount = aoc.ints(gift.spec.split())
  required = sum(shapes[i] * a for i, a in enumerate(amount))
  if gift.x * gift.y >= required:
    ans += 1
aoc.cprint(ans)
