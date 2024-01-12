import sys
import aoc

def walk(steps):
  pos = [0, 0]
  for step in steps:
    dpos = aoc.HEX[step]
    pos[0] += dpos[0]
    pos[1] += dpos[1]
    yield aoc.hex_dist(*pos)

line = sys.stdin.read().strip()
steps = line.split(",")
dist = list(walk(steps))
aoc.cprint(dist[-1])
aoc.cprint(max(dist))
