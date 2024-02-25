import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass
from aoc.refintcode import IntCode, Ref

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
    else:
      return self.data[key]

  def copy(self):
    newdata = DataType(lambda: 0)
    newdata.data = self.data
    newdata.modified = copy.deepcopy(self.modified)
    return newdata

BLACKLIST = set(["infinite loop", "giant electromagnet", "photons", "escape pod", "molten lava"])

def search_items(cpu, state, objects):
  if state.items and state.items[0] not in BLACKLIST:
    before_data = cpu.data.copy()
    fakecpu = copy.copy(cpu)
    fakecpu.data = cpu.data.copy()
    fakecpu, _ = cpu_step(fakecpu, "take " + state.items[0] + "\n")
    after_data = fakecpu.data.modified
    for addr in after_data.keys():
      if before_data[addr] != after_data[addr] and after_data[addr] == -1:
        objects[state.items[0]] = addr

def init_cpu():
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
  cpu, state = init_cpu()
  visited = set()
  vnext = [(state, cpu)]
  objects = {}
  checkpoint = None
  while vnext:
    state, cpu = vnext.pop(0)
    if state.room in visited:
      continue
    visited.add(state.room)
    if state.room == "Securiy Checkpoint":
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

def find_password(cpu, objects):
  print(objects)
  for i in itertools.product(range(2), repeat=8):
    pass

data = aoc.ints(sys.stdin.read().split(","))
checkpoint, objects = visit_rooms(data)
aoc.cprint(find_password(checkpoint, objects))
