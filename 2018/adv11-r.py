import sys
import aoc
import multiprocessing

def hundreds(n):
  return n // 100 % 10

def max_range(goal, j):
  cur = (0, 0, 0, 0)
  best = cur
  sizerange = range(0, m) if goal is None else range(3, 4)
  for size in sizerange:
    if j + size >= m:
      break
    for i in range(m - size):
      py, px = j + size, i + size
      cur = tsum[py][px] - tsum[py][i] - tsum[j][px] + tsum[j][i]
      if cur > best[0]:
        best = (cur, j + 2, i + 2, size)
  return best

def build_tsum(serial):
  tsum = aoc.Table([[0] * m for _ in range(m)])
  for j in range(m):
    curpos = 0
    for i in range(m):
      rackid = i + 1 + 10
      curpos += hundreds((rackid * (j + 1) + serial) * rackid) - 5
      tsum[j][i] = curpos + (0 if j == 0 else tsum[j - 1][i])
  return tsum

def solve(pool, goal=None):
  best = pool.starmap(max_range, ((goal, j) for j in range(m)))
  return max(best)

m = 300
data = sys.stdin.read().strip()
tsum = build_tsum(int(data))
with multiprocessing.Pool() as pool:
  cur = solve(pool, 3)
  aoc.cprint(f"{cur[2]},{cur[1]}")
  cur = solve(pool)
  aoc.cprint(f"{cur[2]},{cur[1]},{cur[3]}")
