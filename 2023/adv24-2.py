import sys
import re
import itertools
import math
import aoc
from collections import *
import numpy

def inter(stones):
  ans = 0
  for a, b in itertools.combinations(stones, 2):
    pax, pay, paz = a[0]
    pbx, pby, pbz = b[0]
    vax, vay, vaz = a[1]
    vbx, vby, vbz = b[1]
    d = vay * vbx - vax * vby
    if d == 0:
      continue
    ta = -(pay * vbx - pby * vbx - pax * vby + pbx * vby)/d
    tb = -(pay * vax - pby * vax - pax * vay + pbx * vay)/d
    py = pay + ta * vay
    px = pax + ta * vax
    print(a,b,px,py,ta,tb)
    pmin, pmax = 200000000000000, 400000000000000
    if pmin <= py <= pmax and pmin <= px <= pmax and ta >= 0 and tb >= 0:
      ans += 1
  return ans


stones = []
eqs = []
for j, line in enumerate(sys.stdin.readlines()[3:6]):
  pos, vel = line.strip().split("@")
  pos = [int(i) for i in pos.split(",")]
  vel = [int(i) for i in vel.split(",")]
  stones.append((pos, vel))
  eqs.append("{%d,%d,%d} + t%d {%d,%d,%d} == {bx, by, bz} + t%d * {vx, vy, vz}"
          % (pos[0],pos[1],pos[2],j,vel[0],vel[1],vel[2],j))
print("Solve[{%s},{%s,bx,by,bz,vx,vy,vz}]" % (",".join(eqs), ",".join("t%d" % i for i in range(len(stones)))))
#print(inter(stones))
