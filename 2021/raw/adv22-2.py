import sys
import aoc
import numpy as np

def solve(m, bounds):
  tx, ty, tz = bounds
  for cube in cubes:
    state = 1 if cube.state == "on" else 0
    m[tx[cube.ax]: tx[cube.bx + 1],
      ty[cube.ay]: ty[cube.by + 1],
      tz[cube.az]: tz[cube.bz + 1]] = state
  ans = 0
  invx = {v:k for k, v in tx.items()}
  invy = {v:k for k, v in ty.items()}
  invz = {v:k for k, v in tz.items()}
  vz = [k for v,k in sorted(invz.items())]
  vz = np.array([a - b for a, b in zip(vz[1:], vz)] + [0])
  for x in range(len(invx) - 1):
    dx = invx[x + 1] - invx[x]
    for y in range(len(invy) - 1):
      dy = dx * (invy[y + 1] - invy[y])
      ans += dy * np.dot(m[x,y,:], vz)
  return ans

def get_bounds(cubes):
  xs, ys, zs = set(), set(), set()
  for cube in cubes:
    xs.add(cube.ax)
    ys.add(cube.ay)
    zs.add(cube.az)
    xs.add(cube.bx + 1)
    ys.add(cube.by + 1)
    zs.add(cube.bz + 1)
  tx = {x:i for i, x in enumerate(sorted(xs))}
  ty = {y:i for i, y in enumerate(sorted(ys))}
  tz = {z:i for i, z in enumerate(sorted(zs))}
  m = np.zeros((len(tx), len(ty), len(tz)), dtype=np.bool_)
  return m, (tx, ty, tz)

data = [line.strip() for line in sys.stdin]
cubes = aoc.retuple_read("state ax_ bx_ ay_ by_ az_ bz_",
    r"^(on|off).*?x=([-+]?\d+)..([-+]?\d+),y=([-+]?\d+)..([-+]?\d+),z=([-+]?\d+)..([-+]?\d+)",
    data)
m, bounds = get_bounds(cubes)
aoc.cprint(solve(m, bounds))
