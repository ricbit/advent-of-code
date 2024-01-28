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
      arg = self.pos + 1 + i
      if addr == "0":
        ans.append(Ref(self.data, self.data[arg]))
      elif addr == "1":
        ans.append(Ref(self.data, arg))
      elif addr == "2":
        ans.append(Ref(self.data, self.data[arg] + self.base))
    return ans

  def run(self, input_generator):
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
        a.set(input_generator())
        self.pos += 2
      elif cmd == 4: # OUT
        (a,) = self.decode(opcode, 1)
        self.output.append(a.get())
        self.pos += 2
        return False
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

def provide_input(cpu, field, display, ball, paddle):
  if ball > paddle:
    return 1
  elif ball < paddle:
    return -1
  else:
    return 0

def simulate(data, start):
  field = aoc.ddict(lambda: 0)
  data[0] = start
  cpu = IntCode(data, [])
  display = 0
  ball = 0
  paddle = 0
  while not cpu.halted:
    cpu.run(lambda: provide_input(cpu, field, display, ball, paddle))
    x = cpu.output[-1]
    cpu.run(lambda: provide_input(cpu, field, display, ball, paddle))
    y = cpu.output[-1]
    cpu.run(lambda: provide_input(cpu, field, display, ball, paddle))
    tile_id = cpu.output[-1]
    if x == -1 and y == 0:
      display = tile_id
    else:
      if tile_id == 4:
        ball = x
      elif tile_id == 3:
        paddle = x
      field[x + 1j * y] = tile_id
  return display, list(field.values()).count(2)

def draw(field, display):
  b = aoc.bounds([(int(f.imag), int(f.real)) for f in field])
  d = {0: ".", 1: "#", 2: "H", 3: "-", 4: "o"}
  aoc.cls()
  aoc.goto0()
  print(display)
  for j in range(b.ymin, 1 + b.ymax):
    line = []
    for i in range(b.xmin, 1 + b.xmax):
      line.append(d[field[i + 1j * j]])
    print("".join(line))
  print()

data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(simulate(data[:], data[0])[1])
aoc.cprint(simulate(data, 2)[0])
