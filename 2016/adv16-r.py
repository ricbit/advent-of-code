import sys
import itertools
import aoc

def double(a):
  b = [1 - x for x in reversed(a)]
  return a + [0] + b

def upto(seed, goal):
  while len(seed) < goal:
    seed = double(seed)
  return seed[:goal]

def checksum(disk):
  while True:
    if len(disk) % 2 == 1:
      return "".join(str(i) for i in disk)
    newdisk = []
    for a, b in itertools.batched(disk, 2):
      newdisk.append(int(a == b))
    disk = newdisk
  

seed = [int(i) for i in sys.stdin.read().strip()]
aoc.cprint(checksum(upto(seed, 272)))
aoc.cprint(checksum(upto(seed, 35651584)))

