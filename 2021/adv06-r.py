import sys
import aoc
from collections import deque

fishes = aoc.ints(sys.stdin.read().split(","))
fishtypes = [0] * 9
for fish in fishes:
  fishtypes[fish] += 1

def count(days, fishtypes):
  fish = deque(fishtypes)
  for _ in range(days):
    fish.rotate(-1)
    fish[6] += fish[-1]
  return sum(fish)

aoc.cprint(count(80, fishtypes))
aoc.cprint(count(256, fishtypes))

