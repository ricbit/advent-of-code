import aoc
import heapq
import mip
import multiprocessing

class Part1Machine:
  def __init__(self, goal, buttons, joltage):
    self.goal = int("".join(("0" if c == "." else "1") for c in goal), 2)
    self.buttons = []
    for button in buttons:
      b = sum(2 ** (len(goal) - 1 - i) for i in button)
      self.buttons.append(b)

  def search(self):
    state = 0
    visited = set([state])
    queue = aoc.bq([(0, state)], size=30)
    while queue:
      flips, state = queue.pop()
      if state == self.goal:
        return flips
      for button in self.buttons:
        nstate = state ^ button
        if nstate not in visited:
          queue.push((flips + 1, nstate))
          visited.add(nstate)
    return None

class Part2Machine:
  def __init__(self, goal, buttons, joltage):
    self.goal = tuple(joltage)
    self.buttons = buttons

  def search(self):
    m = mip.Model(sense=mip.MINIMIZE)
    m.verbose = 1
    button = [m.add_var(var_type=mip.INTEGER, name=f"b{i}")
              for i in range(len(self.buttons))]
    for i in range(len(self.goal)):
      m += mip.xsum(button[b] for b in range(len(button))
                    if i in self.buttons[b]) == self.goal[i]
    m.objective = mip.minimize(mip.xsum(button))
    m.optimize()
    return int(m.objective_value)

def select_machine(packed):
  machine_type, machines = packed
  if machine_type == 1:
    return Part1Machine(*machines).search()
  else:
    return Part2Machine(*machines).search()

def solve(machines, machine_type):
  with multiprocessing.Pool() as pool:
    m = ((machine_type, machine) for machine in machines)
    ans = pool.imap_unordered(select_machine, m)
    return sum(ans)

data = aoc.retuple_read(
    "goal buttons joltage",
    r"\[(.*?)\] (\(.*?\)\s+)\{(.*?)\}")
machines = []
for line in data:
  buttons = line.buttons.split()
  machines.append((line.goal,
                   tuple(tuple(aoc.ints(b[1:-1].split(","))) for b in buttons),
                   tuple(aoc.ints(line.joltage.split(",")))))
# Preload mip
mip.Model()
aoc.cprint(solve(machines, 1))
aoc.cprint(solve(machines, 2))
