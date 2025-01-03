import numpy
import sys
import re
import aoc

def part1(cmds):
  m = numpy.zeros((1000, 1000), dtype=int) - 1
  for q in cmds:
    pslice = m[q.a : q.c + 1, q.b : q.d + 1]
    match q.cmd:
      case "turn on":
        pslice[:] = 1
      case "turn off":
        pslice[:] = -1
      case "toggle":
        pslice[:] *= -1
  return numpy.count_nonzero(m == 1)

def part2(cmds):
  m = numpy.zeros((1000, 1000), dtype=int)
  for q in cmds:
    pslice = m[q.a : q.c + 1, q.b : q.d + 1]
    match q.cmd:
      case "turn on":
        pslice[:] += 1
      case "turn off":
        pslice[:] -= 1
        numpy.clip(pslice, 0, 100000, pslice)
      case "toggle":
        pslice[:] += 2
  return numpy.sum(m)

cmds = aoc.retuple_read("cmd a_ b_ c_ d_",
    r"^((?:\w+|\s+)*?)\s+(\d+),(\d+).*?(\d+),(\d+)$", sys.stdin)
aoc.cprint(part1(cmds))
aoc.cprint(part2(cmds))
