import sys
import re
import itertools
import math

order = list("AKQT98765432J")

def score(hand):
  s = set(hand)
  h = list(hand)
  h.sort(key=lambda x:order.index(x))
  counts = [list(g) for k, g in itertools.groupby(h)]
  counts = [(k[0], len(k)) for k in counts]
  counts.sort(key=lambda x:x[1], reverse=True)
  key = (len(counts), counts[0][1])
  if len(counts) == 1:
    return (0, hand)
  if len(counts) == 2 and counts[0][1] == 4:
    return (1, hand)
  if len(counts) == 2 and counts[0][1] == 3:
    return (2, hand)
  if len(counts) == 3 and counts[0][1] == 3:
    return (3, hand)
  if len(counts) == 3 and counts[0][1] == 2:
    return (4, hand)
  if len(counts) == 4 and counts[0][1] == 2:
    return (5, hand)
  return (6, hand)

def second(h):
  ranks = [score(h.replace("J", c))[0] for c in order]
  return (min(ranks), [order.index(i) for i in h])

hands = sys.stdin.readlines()
hands = [line.strip().split() for line in hands]
hands = [(second(h[0]), h[0], int(h[1])) for h in hands]
hands.sort(reverse=True)
ans = 0
for i,h in enumerate(hands):
  ans += (i + 1) * h[2]
print(ans)
  
