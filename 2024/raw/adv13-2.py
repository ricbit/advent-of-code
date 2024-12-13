import aoc
from fractions import Fraction as F

def solve(blocks, offset):
  cost = 0
  for ba, bb, prize in blocks:
    ainc = aoc.retuple("x_ y_", r".*: X([-+0-9]+), Y([-+0-9]+)", ba)
    binc = aoc.retuple("x_ y_", r".*: X([-+0-9]+), Y([-+0-9]+)", bb)
    pos = aoc.retuple("x_ y_", r".*: X=(\d+), Y=(\d+)", prize)
    py, px = F(pos.y + offset, 1), F(pos.x + offset, 1)
    xa, xb = F(ainc.x, 1), F(binc.x, 1)
    ya, yb = F(ainc.y, 1), F(binc.y, 1)
    pa = (py * xb - px * yb) / (xb * ya - xa * yb)
    pb = (px * ya - py * xa) / (xb * ya - xa * yb)
    if pa.denominator == 1 and pb.denominator == 1:
      cost += 3 * pa + pb
  return cost

data = aoc.line_blocks()
aoc.cprint(solve(data, 0))
aoc.cprint(solve(data, 10**13))
