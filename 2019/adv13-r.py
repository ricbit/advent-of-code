import sys
import aoc
from dataclasses import dataclass

class Ref:
  def __init__(self, data, pos):
    self.data = data
    self.pos = pos

  def get(self):
    return self.data[self.pos]

  def set(self, value):
    self.data[self.pos] = value


class IntCode:
  def __init__(self, data, input_values, state):
    self.data = aoc.ddict(lambda: 0)
    self.data.update({i: value for i, value in enumerate(data)})
    self.pos = 0
    self.output = []
    self.halted = False
    self.base = 0
    self.state = state

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
      if cmd == 1:  # ADD
        a, b, c = self.decode(3)
        c.set(a + b)
        self.pos += 4
      elif cmd == 2:  # MUL
        a, b, c = self.decode(3)
        c.set(a * b)
        self.pos += 4
      elif cmd == 3:  # IN
        (a,) = self.decode(1)
        a.set(self.state.run())
        self.pos += 2
      elif cmd == 4:  # OUT
        if self.data[self.pos] == 204 and self.data[self.pos + 1] == -3:
          if self.data[self.base - 1] == 3:
            self.state.paddle = self.data[self.base - 3]
          elif self.data[self.base - 1] == 4:
            self.state.ball = self.data[self.base - 3]
          self.pos += 6
          continue
        (a,) = self.decode(1)
        self.output.append(a.get())
        self.pos += 2
        return False
      elif cmd == 5:  # JP NZ
        a, b = self.decode(2)
        self.pos = b.get() if (a != 0) else self.pos + 3
      elif cmd == 6:  # JP Z
        a, b = self.decode(2)
        self.pos = b.get() if (a == 0) else self.pos + 3
      elif cmd == 7:  # SET LT
        a, b, c = self.decode(3)
        c.set(int(a < b))
        self.pos += 4
      elif cmd == 8:  # SET EQ
        a, b, c = self.decode(3)
        c.set(int(a == b))
        self.pos += 4
      elif cmd == 9:  # SET BP
        (a,) = self.decode(1)
        self.base += a.get()
        self.pos += 2
      elif cmd == 99:  # HALT
        self.halted = True
        return True

def provide_input(ball, paddle):
  if ball > paddle:
    return 1
  elif ball < paddle:
    return -1
  else:
    return 0

@dataclass(init=True)
class State:
  ball: int
  paddle: int

  def run(self):
    if self.ball > self.paddle:
      return 1
    elif self.ball < self.paddle:
      return -1
    else:
      return 0

def simulate(data, start):
  blocks = 0
  data[0] = start
  state = State(0, 0)
  cpu = IntCode(data, [], state)
  display = 0
  while not cpu.halted:
    cpu.run()
    x = cpu.output[-1]
    cpu.run()
    y = cpu.output[-1]
    cpu.run()
    tile_id = cpu.output[-1]
    match x, y, tile_id:
      case -1, 0, c:
        display = c
      case _, _, 2:
        blocks += 1
  return display, blocks

data = [int(i) for i in sys.stdin.read().split(",")]
aoc.cprint(simulate(data[:], data[0])[1])
aoc.cprint(simulate(data, 2)[0])
