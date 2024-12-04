import itertools
import aoc

def solve_p1(t):
  ans = 0
  for j, i in t.iter_all():
    for diag in aoc.get_diagonals():
      for k, w in enumerate("XMAS"):
        p = complex(j, i) + k * diag
        if t.cvalid(p) and t.get(p) == w:
          continue
        break
      else:
        ans += 1
  return ans

def solve_p2(t):
  pos = list(itertools.product([1, -1], repeat=2))
  ans = 0
  for j, i in t.iter_all():
    if all(t.valid(j + y, i + x) for y, x in pos):
      if t[j][i] != "A":
        continue
      if set([t[j - 1][i - 1], t[j + 1][i + 1]]) != set(["S", "M"]):
        continue
      if set([t[j + 1][i - 1], t[j - 1][i + 1]]) != set(["S", "M"]):
        continue
      ans += 1
  return ans

data = aoc.Table.read()
aoc.cprint(solve_p1(data))
aoc.cprint(solve_p2(data))
