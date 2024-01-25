import sys
import itertools
import aoc
from collections import deque

class IntCode:
  def __init__(self, data, input_values):
    self.data = data[:]
    self.input_values = deque(input_values)
    self.pos = 0
    self.output = []

  def decode(self, opcode, size, decode_last=False):
    ans = []
    msize = size if decode_last else size - 1
    for i in range(msize):
      if opcode[-1 - (2 + i)] == "0":
        ans.append(self.data[self.data[self.pos + 1 + i]])
      else:
        ans.append(self.data[self.pos + 1 + i])
    if not decode_last:
      ans.append(self.data[self.pos + size])
    return ans

  def run(self):
    while self.pos < len(self.data):
      opcode = "%05d" % self.data[self.pos]
      cmd = self.data[self.pos] % 100
      if cmd == 1: # ADD
        a, b, c = self.decode(opcode, 3)
        self.data[c] = a + b
        self.pos += 4
      elif cmd == 2: # MUL
        a, b, c = self.decode(opcode, 3)
        self.data[c] = a * b
        self.pos += 4
      elif cmd == 3: # IN
        (a,) = self.decode(opcode, 1)
        self.data[a] = self.input_values.popleft()
        self.pos += 2
      elif cmd == 4: # OUT
        (a,) = self.decode(opcode, 1, True)
        self.output.append(a)
        self.pos += 2
      elif cmd == 5: # JP NZ
        a, b = self.decode(opcode, 2, True)
        self.pos = b if (a != 0) else self.pos + 3
      elif cmd == 6: # JP Z
        a, b = self.decode(opcode, 2, True)
        self.pos = b if (a == 0) else self.pos + 3
      elif cmd == 7: # SET LT
        a, b, c = self.decode(opcode, 3)
        self.data[c] = int(a < b)
        self.pos += 4
      elif cmd == 8: # SET EQ
        a, b, c = self.decode(opcode, 3)
        self.data[c] = int(a == b)
        self.pos += 4
      elif cmd == 99: # HALT
        break

data = [int(i) for i in sys.stdin.read().split(",")]
cpu = IntCode(data, [5])
cpu.run()
aoc.cprint(cpu.output[0])
