import sys
import aoc
from aoc.refintcode import IntCode

def simulate(data, start):
  pos = 0
  vdir = 1j
  field = aoc.ddict(lambda: 0)
  field[pos] = start
  cpu = IntCode(data[:])
  while cpu.state != cpu.HALTED:
    cpu.input = field[pos]
    cpu.run()
    color = cpu.output
    field[pos] = color
    cpu.run()
    rdir = cpu.output
    if rdir == 0:
      vdir *= 1j
    else:
      vdir *= -1j
    pos += vdir
  return field

def draw(field):
  b = aoc.bounds([(int(f.imag), int(f.real)) for f in field])
  for j in reversed(range(b.ymin, 1 + b.ymax)):
    line = []
    for i in range(b.xmin, 1 + b.xmax):
      line.append("#" if field[i + 1j * j] else ".")
    print("".join(line))

data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(len(simulate(data, 0)))
draw(simulate(data, 1))
