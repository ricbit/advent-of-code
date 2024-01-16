import sys
import aoc

mx, my = 0, 0
quads = aoc.retuple_read("x_ y_ w_ h_", r".*?@ (\d+),(\d+): (\d+)x(\d+)$")
for quad in quads:
  mx = max(mx, quad.x + quad.w)
  my = max(my, quad.y + quad.h)
t = aoc.Table([[-1] * mx for _ in range(my)])
double = set()
mult = set()
for n, quad in enumerate(quads):
  for j, i in t.iter_quad(quad.y, quad.x, quad.h, quad.w):
      if t[j][i] >= 0:
        double.add(t[j][i])
        double.add(n)
        mult.add((j, i))
      t[j][i] = n
aoc.cprint(len(mult))
for i in range(len(quads)):
  if i not in double:
    aoc.cprint(i + 1)

