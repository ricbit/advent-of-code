import sys
import aoc

def gen(start, mult, mod):
  pos = start
  while True:
    pos = (pos * mult) % 2147483647
    if pos % mod == 0:
      yield pos

def count(n, m, mod1, mod2):
  ans = 0
  for i, x, y in zip(range(m), gen(n[0], 16807, mod1), gen(n[1], 48271, mod2)):
    if (x & 0xFFFF) == (y & 0xFFFF):
      ans += 1
  return ans

lines = [line.strip() for line in sys.stdin]
n = []
for line in lines:
  q = aoc.retuple("s_", r".*?(\d+)", line)
  n.append(q.s)
aoc.cprint(count(n, 40000000, 1, 1))
aoc.cprint(count(n, 5000000, 4, 8))
