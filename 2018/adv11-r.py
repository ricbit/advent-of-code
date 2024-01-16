import sys
import aoc

def hundreds(n):
  return n // 100 % 10

def solve(serial, goal = None):
  m = 300
  tsum = aoc.Table([[0] * m for _ in range(m)])
  for j in range(m):
    curpos = 0
    for i in range(m):
      rackid = (i + 1 + 10)
      curpos += hundreds((rackid * (j + 1) + serial) * rackid) - 5
      tsum[j][i] = curpos + (0 if j == 0 else tsum[j - 1][i])
  best = (0, 0, 0, 0)
  for j in range(m):
    for i in range(m):
      sizerange = range(0, m) if goal is None else range(3, 4)
      for size in sizerange:
        if j + size >= m or i + size >= m:
          break
        py, px = j + size, i + size
        cur = tsum[py][px] - tsum[py][i] - tsum[j][px] + tsum[j][i]
        if cur > best[0]:
          best = (cur, j + 2, i + 2, size)
  return best

data = sys.stdin.read().strip()
cur = solve(int(data), 3)
aoc.cprint(f"{cur[2]},{cur[1]}")
cur = solve(int(data))
aoc.cprint(f"{cur[2]},{cur[1]},{cur[3]}")
