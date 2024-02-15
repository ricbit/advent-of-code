import sys
import aoc
from aoc.refintcode import IntCode

CODE1 = """
    NOT D T
    OR C T
    AND A T
    NOT T J
    WALK
"""

CODE2 = """
    NOT C J
    AND H J
    NOT B T
    OR T J
    NOT A T
    OR T J
    AND D J
    RUN
"""

def solve(data, code):
  cpu = IntCode(data)
  opcodes = []
  for line in code.split("\n"):
    if line.strip() and not line.strip().startswith("-"):
      opcodes.append(line.strip() + chr(10))
  stream = "".join(opcodes)
  pos = 0
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        cpu.input = ord(stream[pos])
        pos += 1
      case cpu.OUTPUT:
        last = cpu.output
  return last

data = aoc.ints(sys.stdin.read().strip().split(","))
aoc.cprint(solve(data, CODE1))
aoc.cprint(solve(data, CODE2))
