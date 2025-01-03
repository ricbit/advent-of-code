import sys
import re
import itertools
import aoc
import copy
import bisect
from aoc.refintcode import IntCode
from dataclasses import dataclass

def parse(output, state):
  lines = "".join(output).split("\n")
  doors = False
  state.exits = []
  state.items = []
  for line in lines:
    if line.startswith("="):
      state.room = re.search(r"== (.*?) ==", line).group(1)
    elif line.startswith("Doors"):
      doors = True
    elif line.startswith("Items"):
      doors = False
    elif line.startswith("-"):
      if doors:
        state.exits.append(line.strip()[2:])
      else:
        state.items.append(line.strip()[2:])

@dataclass(init=False, repr=True)
class State:
  room: str
  exits: [str]
  items: [str]

def cpu_step(cpu, cmd):
  output = []
  cmd = list(cmd)
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        if output:
          break
        cpu.input = ord(cmd.pop(0))
      case cpu.OUTPUT:
        output.append(chr(cpu.output))
        if len(output) > 1000:
          cpu.state = cpu.HALTED
          break
  return cpu, "".join(output)

class DataType:
  def __init__(self, creator):
    self.data = aoc.ddict(creator)
    self.modified = {}

  def update(self, init):
    self.data.update(init)

  def __setitem__(self, key, value):
    self.modified[key] = value

  def __getitem__(self, key):
    if key in self.modified:
      return self.modified[key]
    return self.data[key]

  def copy(self):
    newdata = DataType(lambda: 0)
    newdata.data = self.data
    newdata.modified = copy.deepcopy(self.modified)
    return newdata

BLACKLIST = set(["giant electromagnet"])

def search_items(cpu, state, objects):
  if state.items and state.items[0] not in BLACKLIST:
    before_data = cpu.data.copy()
    fakecpu = copy.copy(cpu)
    fakecpu.data = cpu.data.copy()
    fakecpu, _ = cpu_step(fakecpu, "take " + state.items[0] + "\n")
    if fakecpu.state == cpu.HALTED:
      return
    after_data = fakecpu.data.modified
    for addr in after_data.keys():
      if before_data[addr] != after_data[addr] and after_data[addr] == -1:
        objects[state.items[0]] = addr

def init_cpu(data):
  cpu = IntCode(data, DataType)
  state = State()
  cpu, output = cpu_step(cpu, "")
  parse(output, state)
  return cpu, state

def copy_cpu(cpu):
  newcpu = copy.copy(cpu)
  newcpu.data = cpu.data.copy()
  return newcpu

def visit_rooms(data):
  cpu, state = init_cpu(data)
  visited = set()
  vnext = [(state, cpu)]
  objects = {}
  checkpoint = None
  while vnext:
    state, cpu = vnext.pop(0)
    if state.room in visited:
      continue
    visited.add(state.room)
    if state.room == "Security Checkpoint":
      checkpoint = copy_cpu(cpu)
    search_items(cpu, state, objects)
    for cmd in state.exits:
      newcpu = copy_cpu(cpu)
      newcpu, output = cpu_step(newcpu, cmd + chr(10))
      newstate = copy.deepcopy(state)
      parse(output, newstate)
      if newstate.room not in visited:
        vnext.append((newstate, newcpu))
  return checkpoint, objects

def find_weights(cpu, objects):
  weights = {}
  for name, addr in objects.items():
    newcpu = copy_cpu(cpu)
    newcpu.data[addr] = -1
    newcpu, _ = cpu_step(newcpu, "north\n")
    weights[name] = newcpu.data[1550]
  return weights

def find_total_weights(object_weights):
  total_weights = []
  for combinations in itertools.product(range(2), repeat=8):
    weight = sum(itertools.compress(object_weights.values(), combinations))
    total_weights.append((weight, combinations))
  total_weights.sort()
  return total_weights

def compute_weight(cpu, total_weights, objects, wm):
  newcpu = copy_cpu(cpu)
  for addr in itertools.compress(objects.values(), total_weights[wm][1]):
     newcpu.data[addr] = -1
  return cpu_step(newcpu, "north\n")

def test_weight(cpu, total_weights, objects, wm):
  _, output = compute_weight(cpu, total_weights, objects, wm)
  if (comp := re.search(r"(heavier|lighter)", output)) is None:
    return 0
  return 1 if comp.group(1) == "lighter" else -1

def find_password(cpu, objects):
  object_weights = find_weights(cpu, objects)
  total_weights = find_total_weights(object_weights)
  key = lambda wm : test_weight(cpu, total_weights, objects, wm)
  m = bisect.bisect_left(range(len(total_weights)), 0, key=key)
  _, output = compute_weight(cpu, total_weights, objects, m)
  return re.search(r"(\d{3,})", output).group(1)

data = aoc.ints(sys.stdin.read().split(","))
checkpoint, objects = visit_rooms(data)
aoc.cprint(find_password(checkpoint, objects))
