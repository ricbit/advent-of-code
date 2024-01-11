import sys
import itertools
import aoc
import sympy
import numpy as np

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
  print(ans[0])
  return sum(ans[0][:3])
  #print(ans)
  #return ans[0][:3]

def solve_iter(stones):
  var = lambda name: [sympy.symbols(f'{name}{i}') for i in range(3)]
  last = [100000] * 9
  for _ in range(1000000, 100, -100):
    t, p, v = [list(x) for x in itertools.batched((i + 1 for i in last), 3)]
    eqs = []
    for j in range(3):
      for i in range(3):
        eqs.append(stones[j][0][i] + stones[j][1][i] * t[j] - p[i] - v[i] * t[j])
    f = t + p + v
    last = [a - b / 1e16 for a,b in zip(last, eqs)]
    if i % 100 == 0:
      print(last)
  #print(ans)
  #return ans[0][:3]

def cross(A, B):
  x, y, z = A
  a, b, c = B
  return (c * y - b * z, c * x - a * z, b * x - a * y)

def sub(A, B):
  x, y, z = A
  a, b, c = B
  return (x - a, y - b, z - c)

def add(A, B):
  x, y, z = A
  a, b, c = B
  return (x + a, y + b, z + c)

def solve3(stones):
  #c = []
  #for (p1, v1), (p2, v2) in itertools.combinations(stones[:3], 2):
  p1, v1 = stones[0]
  p2, v2 = stones[1]
  p1 = np.array(p1)
  p2 = np.array(p2)
  v1 = np.array(v1)
  v2 = np.array(v2)
  #a = cross(sub(v2, v1), sub(p2, p1))
  #b = add(cross(p1, cross(v1, p2)), cross(p2, cross(v2, p1)))
  P = np.array(solve2(stones))
  #print(cross(P, a), b)
  a = np.cross(v2 - v1, p2 - p1)
  b = np.cross(p1, np.cross(v1, p2)) + np.cross(p2, np.cross(v2, p1))
  print(np.cross(P, a), b)
  #m = np.array([[0, a[1], -a[2]], [a[2], 0, -a[0]], [a[1], -a[0], 0]]).astype(np.float64)
  #x = np.array([-b[0], -b[1], -b[2]]).astype(np.float64)
  #print(np.linalg.solve(m, x))

stones = []
for line in sys.stdin:
  pos, vel = line.strip().split("@")
  pos = [int(i) for i in pos.split(",")]
  vel = [int(i) for i in vel.split(",")]
  stones.append((pos, vel))

print(solve1(stones))
print(solve2(stones))
print(solve_iter(stones))
#print(solve3(stones))
