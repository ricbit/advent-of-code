import sys
import copy
import aoc
from collections import deque
from multiprocessing import Pool

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
  
DIRS = {1: 1j, 2: -1j, 3: -1, 4: 1}
TILES = {0: "#", 1: ".", 2: "O"}

def simulate_step(cpu, field, pos, p):
  cpu.input_values.append(p)
  cpu.run()
  status = cpu.output[-1]
  pos += DIRS[p]
  field[pos] = TILES[status]
  return pos

def simulate(data, field, path):
  pos = 0
  cpu = IntCode(data, [])
  for p in path:
    pos = simulate_step(cpu, field, pos, p)
  return cpu

def smart_get(col, value, factory):
  if value not in col:
    path = factory(value)
    col[value] = path
  return col[value]

def process_state(chosen, path, field, path_cache, visited):
  viable = [i for i in range(1, 5) if field[chosen + DIRS[i]] == " "]
  cpu = smart_get(path_cache, path, lambda x: simulate(data, field, x))
  reuse_cpu = False
  frontier = []
  ball = None
  for p in viable:
    newpath = path + (p, )
    newcpu = cpu if reuse_cpu else copy.deepcopy(cpu)
    pos = simulate_step(newcpu, field, chosen, p)
    reuse_cpu = pos == chosen
    path_cache[newpath] = newcpu
    if field[pos] == "O":
      ball = (pos, len(newpath))
    if field[pos] == "." and pos not in visited:
      frontier.append((pos, newpath))
      visited.add(pos)
  return frontier, ball

def walk(data):
  field = aoc.ddict(lambda: " ")
  pos = 0
  field[pos] = "."
  path_cache = {}
  frontier = [(pos, ())]
  visited = set([pos])
  ball_found = None
  while frontier:
    chosen, path = frontier.pop()
    new_frontier, ball = process_state(chosen, path, field, path_cache, visited)
    if ball is not None:
      ball_found = ball
    frontier.extend(new_frontier)
  return ball_found, field

def draw(field):
  b = aoc.bounds([(int(f.imag), int(f.real)) for f in field])
  table = []
  for j in range(b.ymin, 1 + b.ymax):
    line = []
    for i in range(b.xmin, 1 + b.xmax):
      c = field[i + 1j * j]
      if c == "O":
        ballj, balli = j - b.ymin, i - b.xmin
      line.append(c)
    table.append(line)
  return table, (ballj, balli)

def grow(t, ball):
  ticks = [ball]
  visited = set(ticks)
  time = 0
  while ticks:
    time += 1
    frontier = set()
    for tick in ticks:
      for j, i in t.iter_neigh4(tick[0], tick[1]):
        if t[j][i] == "." and (j, i) not in visited:
          frontier.add((j, i))
          visited.add((j, i))
    ticks = frontier
  return time - 1

data = [int(i) for i in sys.stdin.read().split(",")]
(ballpos, ballpath), field = walk(data)
aoc.cprint(ballpath)
table, ball = draw(field)
data = aoc.Table(table)
aoc.cprint(grow(data, ball))
