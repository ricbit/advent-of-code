import sys
import aoc
from aoc.refintcode import IntCode

def run_cpu(data, value):
  cpu = IntCode(data[:])
  output = None
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        cpu.input = value
      case cpu.OUTPUT:
        output = cpu.output
  return output

data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(run_cpu(data, 1))
aoc.cprint(run_cpu(data, 5))
