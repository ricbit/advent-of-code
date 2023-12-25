import sys
import re
import itertools
import math
from collections import defaultdict

def simulate(modules, n):
  flips = {}
  conj = defaultdict(dict)
  inputs = defaultdict(list)
  for name, (value, outs) in modules.items():
    if value == "%":
      flips[name] = 0
    for out in outs:
      inputs[out].append(name)
  #print(inputs)
  for name, (value, outs) in modules.items():
    if value == "&":
      for inp in inputs[name]:
        conj[name][inp] = 0
  lows = 0
  highs = 0
  for button in range(n):
    pulses = [(0, "broadcaster", "broadcaster")]
    while pulses:
      pulse, name, inp = pulses.pop(0)
      if pulse == 1:
        highs += 1
      else:
        lows += 1
      if name == "rx" and pulse == 0:
        return button + 1
      #print(inp, pulse, name)
      #print(pulses)
      if name not in modules:
        continue
      match modules[name][0]:
        case None:
          for dest in modules[name][1]:
            pulses.append((pulse, dest, name))
        case "%":
          if pulse == 0:
            flips[name] = 1 - flips[name]
            for dest in modules[name][1]:
              pulses.append((flips[name], dest, name))
        case "&":
          conj[name][inp] = pulse
          if all(i == 1 for i in conj[name].values()):
            for dest in modules[name][1]:
              pulses.append((0, dest, name))
          else:
            for dest in modules[name][1]:
              pulses.append((1, dest, name))
  return lows * highs

modules = {}
for line in sys.stdin:
  prefix, name, outs = re.match(r"(%|&)?(\w+) -> (.*)$", line).groups()
  modules[name] = (prefix, [i.strip() for i in outs.strip().split(",")])

print(modules)
print(simulate(modules, 1000))
print(simulate(modules, 10000000))

  
