import aoc

class Ref:
  def __init__(self, data, pos):
    self.data = data
    self.pos = pos

  def get(self):
    return self.data[self.pos]

  def set(self, value):
    self.data[self.pos] = value


class IntCode:
  def __init__(self, data, data_type=aoc.ddict):
    self.data = data_type(lambda: 0)
    self.data.update({i:value for i, value in enumerate(data)})
    self.pos = 0
    self.state = self.RUNNING
    self.base = 0
    self.input = None
    self.output = None

  RUNNING = 0
  HALTED = 1
  INPUT = 2
  OUTPUT = 3

  def decode(self, size):
    ans = []
    opcode = self.data[self.pos] // 100
    for i in range(size):
      addr = opcode % 10
      opcode //= 10
      arg = self.pos + 1 + i
      if addr == 0:
        ans.append(Ref(self.data, self.data[arg]))
      elif addr == 1:
        ans.append(Ref(self.data, arg))
      elif addr == 2:
        ans.append(Ref(self.data, self.data[arg] + self.base))
    return ans

  def run(self):
    if self.state == self.HALTED:
      return False

    self.state = self.RUNNING
    while True:
      cmd = self.data[self.pos] % 100
      if cmd == 1: # ADD
        a, b, c = self.decode(3)
        c.set(a.get() + b.get())
        self.pos += 4
      elif cmd == 2: # MUL
        a, b, c = self.decode(3)
        c.set(a.get() * b.get())
        self.pos += 4
      elif cmd == 3: # IN
        if self.input is None:
          self.state = self.INPUT
          return True
        (a,) = self.decode(1)
        a.set(self.input)
        self.input = None
        self.pos += 2
      elif cmd == 4: # OUT
        (a,) = self.decode(1)
        self.output = a.get()
        self.pos += 2
        self.state = self.OUTPUT
        return True
      elif cmd == 5: # JP NZ
        a, b = self.decode(2)
        self.pos = b.get() if (a.get() != 0) else self.pos + 3
      elif cmd == 6: # JP Z
        a, b = self.decode(2)
        self.pos = b.get() if (a.get() == 0) else self.pos + 3
      elif cmd == 7: # SET LT
        a, b, c = self.decode(3)
        c.set(int(a.get() < b.get()))
        self.pos += 4
      elif cmd == 8: # SET EQ
        a, b, c = self.decode(3)
        c.set(int(a.get() == b.get()))
        self.pos += 4
      elif cmd == 9: # SET BP
        (a,) = self.decode(1)
        self.base += a.get()
        self.pos += 2
      elif cmd == 99: # HALT
        self.state = self.HALTED
        return False

