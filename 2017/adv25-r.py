import re
import aoc

def turing(machine, start, size):
  tape = set()
  pos = 0
  state = start
  action = {1: lambda p: tape.add(p), 0: lambda p: tape.remove(p)}
  for _ in range(size):
    value = 1 if pos in tape else 0
    m = machine[(state, value)]
    action[m[0]](pos)
    pos += m[1]
    state = m[2]
  return len(tape)

def parse_state(block, n):
  write = re.search(r"(\d+).$", block[n]).group(1)
  move = re.search(r"\s(\w+)\.$", block[n + 1]).group(1)
  nstate = re.search(r"(.)\.$", block[n + 2]).group(1)
  return (int(write), 1 if move == "right" else - 1, nstate)

blocks = aoc.line_blocks()
start = re.search(r"(.)\.$", blocks[0][0]).group(1)
size = int(re.search(r"(\d+)", blocks[0][1]).group(1))
machine = {}
for block in blocks[1:]:
  name = re.search(r"(.):$", block[0]).group(1)
  machine[(name, 0)] = parse_state(block, 2)
  machine[(name, 1)] = parse_state(block, 6)
aoc.cprint(turing(machine, start, size))
