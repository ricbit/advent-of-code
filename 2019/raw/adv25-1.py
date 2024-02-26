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
from aoc.refintcode import IntCode

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
  inv: set
  visited: set

def game_logic(state):
  print(state)
  vhash = (state.room, tuple(sorted(state.inv)))
  if vhash in state.visited:
    return
  state.visited.add(vhash)
  for e in state.exits:
    yield e
  for item in state.items:
    yield "take " + item.strip()

def solve(data, drops):
  cpu = IntCode(data)
  current = list("""east
east
east
take shell
west
south
take monolith
north
west
north
west
take bowl of rice
east
north
take planetoid
west
take ornament
south
south
take fuel cell
north
north
east
east
take cake
south
west
north
take astrolabe
west
""")
  objs = [
    "shell",
    "monolith",
    "bowl of rice",
    "planetoid",
    "ornament",
    "fuel cell",
    "cake",
    "astrolabe"]
  output = []
  state = State()
  state.inv = set()
  state.visited = set()
  for obj, drop in zip(objs, drops):
    if drop:
      current.extend(list("drop " + obj + chr(10)))
  current.extend(list("north\n"))
  has_pressure = False
  allput = []
  while cpu.run():
    match cpu.state:
      case cpu.INPUT:
        if output:
          #parse(output, state)
          s = "".join(output)
          if "Pressure" in s:
            #print(s, flush=True)
            has_pressure = True
          output.clear()
          #for cmd in game_logic(state):
          #  queue.append(list(cmd + chr(10)))
          #if queue:
          #  current = list(queue.pop(0))
          #else:
          #  return 0o          
          if not current:
            if not has_pressure:
              #print(allput)
              return False
            return True
            #current = liist(input() + chr(10))
        if current:
          cpu.input = ord(current.pop(0))
      case cpu.OUTPUT:
        allput.append(chr(cpu.output))
        output.append(chr(cpu.output))
  print("".join(allput))
  return 0

def search(data):
  for i in itertools.product(range(2), repeat=8):
    pressure = solve(data, i)
    if not pressure:
      print(f"line {i}")

data = aoc.ints(open("input.25.txt", "rt").read().split(","))
aoc.cprint(search(data))
