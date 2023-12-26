import sys
import itertools
import aoc

def build_distances(t, reachable):
  allj = list(j for j, i in reachable)
  alli = list(i for j, i in reachable)
  minj, maxj = min(allj + [0]), max(allj + [t.h])
  mini, maxi = min(alli + [0]), max(alli + [t.h])
  sizej = maxj - minj + 1
  sizei = maxi - mini + 1
  m = [["."] * sizei for _ in range(sizej)]
  for j in range(minj, maxj + 1):
    for i in range(mini, maxi + 1):
      m[j - minj][i - mini] = t[j % t.h][i % t.w]
  for j, i in reachable:
    m[j - minj][i - mini] = "O"
  return m

def walk(t, py, px, n):
  reachable = set([(py, px)])
  last_odd = [set(), set()]
  visited = set()
  for step in range(n + 1):
    newreach = set()
    if step % 2 == n % 2:
      for j, i in reachable:
        visited.add((j, i))
    for j, i in reachable:
      for dj, di in aoc.DIRECTIONS.values():
        jj = j + dj
        ii = i + di
        if t[jj % t.h][ii % t.w] == ".":
          newreach.add((jj, ii))
    reachable = set((x for x in newreach if (
          x not in last_odd[0] and x not in last_odd[1])))
    last_odd = [last_odd[1], reachable]
  return build_distances(t, visited)

def find_s(t):
  for j, row in enumerate(t.table):
    if "S" in row:
      i = row.index("S")
      t[j][i] = "."
      return j, i

def get_sizes(dist):
  sizes = []
  for line in dist:
    sizes.append(len([c for c in line if c not in "#."]))
  return sizes

def simulate(t, py, px, n):
  reference = t.h * 3 + n % t.h
  sizes = get_sizes(walk(t, py, px, reference))
  ans = 0
  for i in range(t.h):
    chopped = itertools.islice(sizes, i, None, t.h)
    diffs = [(b - a) for a, b in itertools.pairwise(chopped)]
    half = (n - reference) // t.h
    last = sizes[i] + diffs[0]
    ans += sizes[i] + last
    ans += half * last + half * (half + 1) * diffs[1] // 2
    last += half * diffs[1]
    for i in itertools.islice(diffs, 1, len(diffs) - 1):
      last += i
      ans += last
    ans += half * last + half * (half + 1) * diffs[-2] // 2
    ans += last + half * diffs[-2] + diffs[-1]
  return ans

t = aoc.Table.read()
py, px = find_s(t)
print(sum(get_sizes(walk(t, py, px, 64))))
print(simulate(t, py, px, 26501365))
