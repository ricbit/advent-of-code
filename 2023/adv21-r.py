import aoc

def build_distances(t, reachable):
  allj = list(j for j, i in reachable)
  alli = list(i for j, i in reachable)
  minj, maxj = min(allj + [0]), max(allj + [t.h])
  mini, maxi = min(alli + [0]), max(alli + [t.w])
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
  notseen = lambda x: all(x not in last for last in last_odd)
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
    reachable = set((x for x in newreach if notseen(x)))
    last_odd = [last_odd[1], reachable]
  return build_distances(t, visited)

def find_s(t):
  for j, row in enumerate(t.table):
    if "S" in row:
      i = row.index("S")
      t[j][i] = "."
      return j, i

def get_sizes(dist):
  for line in dist:
    yield len([c for c in line if c not in "#."])

def direct(t, py, px, n):
  return sum(get_sizes(walk(t, py, px, n)))

def simulate(t, py, px, n):
  base = n % t.h
  x, y, z = [direct(t, py, px, base + i * t.h) for i in range(3)]
  a = (x - 2 * y + z) // 2
  b = (-3 * x + 4 * y - z) // 2
  c = x
  i = n // t.h
  return a * i * i + b * i + c

t = aoc.Table.read()
py, px = find_s(t)
print(direct(t, py, px, 64))
print(simulate(t, py, px, 26501365))
