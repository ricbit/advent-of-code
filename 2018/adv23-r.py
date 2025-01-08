import sys
import itertools
import aoc
import heapq
import copy

def solve1(nano):
  j = max(nano, key=lambda q:q.r)
  ans = 0
  for i in nano:
    if abs(j.x - i.x) + abs(j.y - i.y) + abs(j.z - i.z) <= j.r:
      ans += 1
  return ans

def bounds(series, calc):
  return [min(calc(q) - q.r for q in series), max(calc(q) + q.r for q in series)]

getcoord = {0: lambda q: q.x, 1: lambda q: q.y, 2: lambda q: q.z}

def qinside(q, vert, box):
  return all(box[i][0] <= getcoord[i](q) + vert[i] <= box[i][1] for i in range(3))

def vinside(q, corner):
  return abs(q.x - corner[0]) + abs(q.y - corner[1]) + abs(q.z - corner[2]) <= q.r

def check(q, box):
  vertexes = [
      [q.r, 0, 0], [-q.r, 0, 0],
      [0, q.r, 0], [0, -q.r, 0],
      [0, 0, q.r], [0, 0, -q.r]
  ]
  return (
      any(qinside(q, vert, box) for vert in vertexes) or
      any(vinside(q, corner) for corner in itertools.product(*box))
  )

def count(nano, box):
  return -sum(check(q, box) for q in nano)

def partition(nano, box):
  vnext = [(count(nano, box), box)]
  while vnext:
    _, box = heapq.heappop(vnext)
    sides = [(box[i][1] - box[i][0] + 1, i) for i in range(3)]
    sides.sort(reverse=True)
    if sides[0][0] == 1:
      return sum(box[i][0] for i in range(3))
    middle = sides[0][0] // 2
    side = sides[0][1]

    newbox1 = copy.deepcopy(box)
    newbox1[side][1] = newbox1[side][0] + middle - 1
    heapq.heappush(vnext, (count(nano, newbox1), newbox1))

    newbox2 = copy.deepcopy(box)
    newbox2[side][0] += middle
    heapq.heappush(vnext, (count(nano, newbox2), newbox2))
  return None

data = [line.strip() for line in sys.stdin]
nano = aoc.retuple_read(
    "x_ y_ z_ r_", r"pos=<([-+]?\d+),([-+]?\d+),([-+]?\d+)>, r=(\d+)", data)
aoc.cprint(solve1(nano))
box = [bounds(nano, getcoord[i]) for i in range(3)]
aoc.cprint(partition(nano, box))
