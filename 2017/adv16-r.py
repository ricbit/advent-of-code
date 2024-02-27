import sys
import itertools
import aoc

def execute(prog, cmd):
  for c in cmd:
    match (c.code, c.src, c.dst):
      case "s", src, _:
        s = int(src)
        prog = prog[-s:] + prog[:-s]
      case "x", src, dst:
        a, b = int(src), int(dst)
        prog[a], prog[b] = prog[b], prog[a]
      case "p", src, dst:
        a = prog.index(src)
        b = prog.index(dst)
        prog[a], prog[b] = prog[b], prog[a]
  return prog

def iter_cycle(prog, cmd):
  for _ in itertools.count(1):
    prog = list(execute(prog, cmd))
    yield tuple(prog)

line = sys.stdin.read().strip()
cmd = []
for p in line.split(","):
  q = aoc.retuple("code src dst", r"(.)(.*?)(?:/(.*))?$", p)
  cmd.append(q)
prog = list(chr(i) for i in range(ord("a"), ord("p") + 1))
aoc.cprint("".join(execute(prog[:], cmd)))
aoc.cprint("".join(aoc.extrapolate(iter_cycle(prog, cmd), 1000000000)))
