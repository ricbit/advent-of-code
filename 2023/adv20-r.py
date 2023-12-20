import sys
import re
import itertools
import math
from collections import defaultdict, Counter

def get_inputs(modules):
  inputs = defaultdict(list)
  for name, (value, outs) in modules.items():
    for out in outs:
      inputs[out].append(name)
  return inputs

def initialize(modules, inputs):
  flips = {}
  conj = defaultdict(dict)
  for name, (value, outs) in modules.items():
    if value == "%":
      flips[name] = 0
    if value == "&":
      for inp in inputs[name]:
        conj[name][inp] = 0
  return flips, conj

def send_signal(modules, pulses, value, name):
  for dest in modules[name][1]:
    pulses.append((value, dest, name))

def simulate(modules, inputs, nands, n):
  flips, conj = initialize(modules, inputs)
  counts, periods = Counter(), {}
  buttons = range(n) if n else itertools.count()
  for button in buttons:
    pulses = [(0, "broadcaster", "!")]
    while pulses:
      value, name, inp = pulses.pop(0)
      counts[value] += 1
      if name in nands and value == 0 and name not in periods:
        periods[name] = button + 1
      if len(periods) == len(nands):
        return math.lcm(*periods.values())
      match modules[name][0]:
        case None:
          send_signal(modules, pulses, value, name)
        case "%" if value == 0:
          flips[name] = 1 - flips[name]
          send_signal(modules, pulses, flips[name], name)
        case "&":
          conj[name][inp] = value
          nand = 0 if all(i == 1 for i in conj[name].values()) else 1
          send_signal(modules, pulses, nand, name)
  return math.prod(counts.values())

def simple_nands(modules, inputs):
  for name, (prefix, outs) in modules.items():
    if prefix == "&" and len(inputs[name]) == 1:
      yield name

modules = defaultdict(lambda: ("!", []))
for line in sys.stdin:
  prefix, name, outs = re.match(r"(%|&)?(\w+) -> (.*)$", line).groups()
  modules[name] = (prefix, [i.strip() for i in outs.strip().split(",")])
inputs = get_inputs(modules)
nands = list(simple_nands(modules, inputs))

print(simulate(modules, inputs, nands, 1000))
print(simulate(modules, inputs, nands, None))

  
