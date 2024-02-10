import sys
import collections

crabs = [int(i) for i in sys.stdin.readline().strip().split(",")]
crabpos = collections.Counter()
for crab in crabs:
  crabpos[crab] += 1

def count(crabpos, x):
  ans = 0
  for i, crabs in crabpos.items():
    ans += abs(x - i) * crabs
  return ans

best = 1e9
for i in crabpos.keys():
  best = min(best, count(crabpos, i))
print(best)

    
