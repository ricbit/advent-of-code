import sys
import aoc

def maybe(state, y):
  if y[0].isalpha():
    return state[y]
  else:
    return int(y)

class Computer:
  def __init__(self, prog, p, model):
    self.pc = 0
    self.state = aoc.ddict(lambda: 0, {"p": p})
    self.recv = []
    self.finished = False
    self.prog = prog
    self.sent = 0
    self.waiting = False
    self.model = model
    self.freq = 0

  def check(self):
    return self.finished or (self.waiting and not self.recv)

  def recv_cmd(self, x):
    if self.model == 1:
      return bool(self.state[x])
    else:
      self.waiting = not self.recv
      if self.recv:
        self.state[x] = self.recv.pop(0)
      return self.waiting

  def snd_cmd(self, x, send):
    if self.model == 1:
      self.freq = maybe(self.state, x)
    else:
      send(maybe(self.state, x))
      self.sent += 1

  def execute(self, send):
    while self.pc < len(self.prog):
      match self.prog[self.pc]:
        case "snd", x:
          self.snd_cmd(x, send)
        case "set", x, y:
          self.state[x] = maybe(self.state, y)
        case "add", x, y:
          self.state[x] += maybe(self.state, y)
        case "mul", x, y:
          self.state[x] *= maybe(self.state, y)
        case "mod", x, y:
          self.state[x] %= maybe(self.state, y)
        case "rcv", x:
          if self.recv_cmd(x):
            return self
        case "jgz", x, y:
          if maybe(self.state, x) > 0:
            self.pc += maybe(self.state, y) - 1
      self.pc += 1
    self.finished = True
    return self

def multicore(prog):
  comps = [Computer(prog, 0, 2), Computer(prog, 1, 2)]
  while not all(comps[i].check() for i in range(2)):
    for i in range(2):
      comps[i].execute(lambda x: comps[1 - i].recv.append(x))
  return comps[1].sent

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  prog.append(line.split())
aoc.cprint(Computer(prog, 0, 1).execute(lambda x: None).freq)
aoc.cprint(multicore(prog))
