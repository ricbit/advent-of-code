import sys
import itertools
import aoc
import sympy

def solve1(stones):
  ans = 0
  pmin, pmax = 200000000000000, 400000000000000
  bounds = lambda x: pmin <= x <= pmax
  for a, b in itertools.combinations(stones, 2):
    pax, pay, paz = a[0]
    pbx, pby, pbz = b[0]
    vax, vay, vaz = a[1]
    vbx, vby, vbz = b[1]
    d = vay * vbx - vax * vby
    if d == 0:
      continue
    ta = -(pay * vbx - pby * vbx - pax * vby + pbx * vby) / d
    tb = -(pay * vax - pby * vax - pax * vay + pbx * vay) / d
    py = pay + ta * vay
    px = pax + ta * vax
    if bounds(py) and bounds(px) and ta >= 0 and tb >= 0:
      ans += 1
  return ans

def solve2(stones):
  var = lambda name: [sympy.symbols(f'{name}{i}') for i in range(3)]
  t, p, v = [var(name) for name in "tpv"]
  eqs = []
  for j in range(3):
    for i in range(3):
      eqs.append(stones[j][0][i] + stones[j][1][i] * t[j] - p[i] - v[i] * t[j])
  ans = sympy.solve(eqs, list(aoc.flatten([p, v, t])))
  return int(sum(ans[0][:3]))

stones = []
for line in sys.stdin:
  pos, vel = line.strip().split("@")
  pos = aoc.ints(pos.split(","))
  vel = aoc.ints(vel.split(","))
  stones.append((pos, vel))

aoc.cprint(solve1(stones))
aoc.cprint(solve2(stones))
