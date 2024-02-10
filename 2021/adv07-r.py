import sys
import collections
import aoc

crabs = aoc.ints(sys.stdin.read().split(","))
crabpos = collections.Counter()
for crab in crabs:
  crabpos[crab] += 1

def triangular(n):
  return n * (n + 1) // 2

def count(crabpos, x, weight):
  ans = 0
  for i, crabs in crabpos.items():
    ans += weight(abs(x - i)) * crabs
  return ans

def solve(crabpos, weight):
  best = 1e9
  for i in range(1 + max(crabpos.keys())):
    best = min(best, count(crabpos, i, weight))
  return best

aoc.cprint(solve(crabpos, lambda x: x))
aoc.cprint(solve(crabpos, triangular))

    
