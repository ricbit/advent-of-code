import sys
import itertools
import aoc
from collections import deque

class Ref:
  def __init__(self, data, pos):
    self.data = data
    self.pos = pos

  def get(self):
    return self.data[self.pos]

  def set(self, value):
    self.data[self.pos] = value


class IntCode:
  def __init__(self, data, input_values):
    self.data = aoc.ddict(lambda: 0)
    self.data.update({i:value for i, value in enumerate(data)})
    self.input_values = deque(input_values)
    self.pos = 0
    self.output = []
    self.halted = False
    self.base = 0

  def decode(self, opcode, size):
    ans = []
    for i in range(size):
      addr = opcode[-1 - (2 + i)]
      if addr == "0":
        ans.append(Ref(self.data, self.data[self.pos + 1 + i]))
      elif addr == "1":
        ans.append(Ref(self.data, self.pos + 1 + i))
      elif addr == "2":
        ans.append(Ref(self.data, self.data[self.pos + 1 + i] + self.base))
    return ans

  def run(self):
    if self.halted:
      return True

    while self.pos < len(self.data):
      opcode = "%05d" % self.data[self.pos]
      cmd = self.data[self.pos] % 100
      if cmd == 1: # ADD
        a, b, c = self.decode(opcode, 3)
        c.set(a.get() + b.get())
        self.pos += 4
      elif cmd == 2: # MUL
        a, b, c = self.decode(opcode, 3)
        c.set(a.get() * b.get())
        self.pos += 4
      elif cmd == 3: # IN
        (a,) = self.decode(opcode, 1)
        a.set(self.input_values.popleft())
        self.pos += 2
      elif cmd == 4: # OUT
        (a,) = self.decode(opcode, 1)
        self.output.append(a.get())
        self.pos += 2
      elif cmd == 5: # JP NZ
        a, b = self.decode(opcode, 2)
        self.pos = b.get() if (a.get() != 0) else self.pos + 3
      elif cmd == 6: # JP Z
        a, b = self.decode(opcode, 2)
        self.pos = b.get() if (a.get() == 0) else self.pos + 3
      elif cmd == 7: # SET LT
        a, b, c = self.decode(opcode, 3)
        c.set(int(a.get() < b.get()))
        self.pos += 4
      elif cmd == 8: # SET EQ
        a, b, c = self.decode(opcode, 3)
        c.set(int(a.get() == b.get()))
        self.pos += 4
      elif cmd == 9: # SET BP
        (a,) = self.decode(opcode, 1)
        self.base += a.get()
        self.pos += 2
      elif cmd == 99: # HALT
        self.halted = True
        return True

data = [int(i) for i in sys.stdin.read().split(",")]
cpu = IntCode(data, [1])
cpu.run()
aoc.cprint(cpu.output[0])
cpu = IntCode(data, [2])
cpu.run()
aoc.cprint(cpu.output[0])
