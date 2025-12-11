import aoc
import copy

def rule1(infected, vdir, pos, ans):
  if infected[pos] == "#":
    vdir *= 1j
    infected[pos] = "."
  else:
    vdir *= -1j
    infected[pos] = "#"
    ans += 1
  return vdir, ans

cdir = dict(zip(".W#F", [-1j, 1, 1j, -1]))
cinfected = dict(zip(".W#F", "W#F."))

def rule2(infected, vdir, pos, ans):
  current = infected[pos]
  vdir *= cdir[current]
  infected[pos] = cinfected[current]
  if current == "W":
    ans += 1
  return vdir, ans

def govirus(infected, y, x, vdir, n, rule):
  ans = 0
  pos = (y * 1j + x)
  for _ in range(n):
    vdir, ans = rule(infected, vdir, pos, ans)
    pos += vdir
  return ans

t = aoc.Table.read()
infected = aoc.ddict(lambda: ".")
for j, i in t.iter_all():
  if t[j][i] == "#":
    infected[j * 1j + i] = "#"
m = len(t.table) // 2
infected2 = copy.deepcopy(infected)
aoc.cprint(govirus(infected, m, m, -1j, 10000, rule1))
aoc.cprint(govirus(infected2, m, m, -1j, 10000000, rule2))
