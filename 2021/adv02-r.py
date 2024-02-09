import sys
import aoc

def part1(lines):
  h, v = 0, 0
  for q in cmds:
    match q.cmd:
      case "forward":
        h += q.dist
      case "down": 
        v += q.dist
      case "up":
        v -= q.dist
  return h * v

def part2(cmds):
  h, v, aim = 0, 0, 0
  for q in cmds:
    match q.cmd:
      case "forward":
        h += q.dist
        v += q.dist * aim
      case "down": 
        aim += q.dist
      case "up":
        aim -= q.dist
  return h * v

cmds = aoc.retuple_read("cmd dist_", r"(\w+) (\d+)", sys.stdin)
aoc.cprint(part1(cmds))
aoc.cprint(part2(cmds))

