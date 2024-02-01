import sys
import itertools
import aoc
import random
from collections import deque
import pytesseract
import numpy

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
    self.pos = 0
    self.output = []
    self.halted = False
    self.base = 0
    self.input_values = []

  def decode(self, size):
    ans = []
    opcode = self.data[self.pos] // 100
    for i in range(size - 1):
      addr = opcode % 10
      opcode //= 10
      arg = self.pos + 1 + i
      if addr == 0:
        ans.append(self.data[self.data[arg]])
      elif addr == 1:
        ans.append(self.data[arg])
      elif addr == 2:
        ans.append(self.data[self.data[arg] + self.base])
    addr = opcode % 10
    opcode //= 10
    arg = self.pos + 1 + size - 1
    if addr == 0:
      ans.append(Ref(self.data, self.data[arg]))
    elif addr == 1:
      ans.append(Ref(self.data, arg))
    elif addr == 2:
      ans.append(Ref(self.data, self.data[arg] + self.base))
    return ans

  def run(self):
    if self.halted:
      return True

    ops = 0
    while self.pos < len(self.data):
      ops += 1
      cmd = self.data[self.pos] % 100
      if cmd == 1: # ADD
        a, b, c = self.decode(3)
        c.set(a + b)
        self.pos += 4
      elif cmd == 2: # MUL
        a, b, c = self.decode(3)
        c.set(a * b)
        self.pos += 4
      elif cmd == 3: # IN
        (a,) = self.decode(1)
        a.set(self.input_values.pop())
        self.pos += 2
      elif cmd == 4: # OUT
        (a,) = self.decode(1)
        self.output.append(a.get())
        self.pos += 2
        return False
      elif cmd == 5: # JP NZ
        a, b = self.decode(2)
        self.pos = b.get() if (a != 0) else self.pos + 3
      elif cmd == 6: # JP Z
        a, b = self.decode(2)
        self.pos = b.get() if (a == 0) else self.pos + 3
      elif cmd == 7: # SET LT
        a, b, c = self.decode(3)
        c.set(int(a < b))
        self.pos += 4
      elif cmd == 8: # SET EQ
        a, b, c = self.decode(3)
        c.set(int(a == b))
        self.pos += 4
      elif cmd == 9: # SET BP
        (a,) = self.decode(1)
        self.base += a.get()
        self.pos += 2
      elif cmd == 99: # HALT
        self.halted = True
        return True

def simulate(data, field, path):
  d = {1: 1j, 2:-1j, 3:-1, 4:1}
  pos = 0
  cpu = IntCode(data, [])
  c = {0:"#", 1: ".", 2:"O"}
  for p in path:
    cpu.input_values.append(p)
    cpu.run()
    status = cpu.output[-1]
    pos += d[p]
    field[pos] = c[status]
  return field

def get_frontier(field):
  ans = []
  for pos, value in list(field.items()):
    if value == ".":
      d = {1: 1j, 2:-1j, 3:-1, 4:1}
      if any(field[pos + d[i]] == " " for i in range(1, 5)):
        ans.append(pos)
  return ans

def shortest(field, chosen):
  start = 0 
  vnext = deque([(start, [])])
  visited = set()
  d = {1: 1j, 2:-1j, 3:-1, 4:1}
  while vnext:
    pos, path = vnext.popleft()
    if pos == chosen:
      return path
    visited.add(pos)
    for i in range(1, 5):
      if field[pos + d[i]] in ".O" and (pos + d[i]) not in visited:
        vnext.append((pos + d[i], path + [i]))



def walk(data):
  field = aoc.ddict(lambda: " ")
  pos = 0
  field[pos] = "."
  d = {1: 1j, 2:-1j, 3:-1, 4:1}
  while True:
    chosen = random.choice(get_frontier(field))
    viable = [i for i in range(1, 5) if field[chosen + d[i]] == " "]
    path = shortest(field, chosen) + [random.choice(viable)]
    simulate(data, field, path)
    draw(field)
    if "O" in field.values():
      for k, v in field.items():
        if v == "O":
          return len(shortest(field, k))



def draw(field):
  b = aoc.bounds([(int(f.imag), int(f.real)) for f in field])
  aoc.cls()
  aoc.goto0()
  for j in reversed(range(b.ymin, 1 + b.ymax)):
    line = []
    for i in range(b.xmin, 1 + b.xmax):
      line.append(field[i + 1j * j])
    print("".join(line))

data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(walk(data))
