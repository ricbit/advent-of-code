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
  lastflips = flips.copy()
  periods = {}
  countdown = -1
  for button in range(n):
    #  print(button, flips)
    kset = []
    for k, v in flips.items():
        if lastflips[k] != v:
            kset.append(k)
            if k not in periods:
                periods[k] = button
                #print(len(periods), conj)
                #if len(periods) == 48:
                #  return periods, inputs
    #print(button, len(kset), " ".join(sorted(kset)))
    #print(periods)
    lastflips = flips.copy()
    pulses = [(0, "broadcaster", "broadcaster")]
    if button % 100000 == 0:
        print(button)
    #print(len(flips))
    while pulses:
      countdown -= 1
      if countdown == 0:
          return
      pulse, name, inp = pulses.pop(0)
      if pulse == 1:
        highs += 1
      else:
        lows += 1
      if name == "rx" and pulse == 0:
        return button + 1
      if countdown > 0:
        print(button, inp, pulse, name)
      #print(pulses)
      if name in ["xc", "ct"] and pulse == 0:
          print(button,name, pulse)
      if conj["xc"]["zt"] == 0 and conj["ct"]["gt"] == 0 and button > 10:
          countdown = 10
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

def prefix(modules, p):    
  if p not in modules or modules[p][0] is None:
    return ""
  elif modules[p][0] == "%":
    return "FLIP_"
  else:
    return "NAND_"

def simple_nands(modules, periods, inputs):
  for name, (prefix, outs) in modules.items():
    if name in inputs:
      if all(modules.get(inp, "")[0]== "%" for inp in inputs[name]):
        if modules[name][0] == "&":
          print(name, sum([periods[inp] for inp in inputs[name]]))

def graphviz(modules):
  print("digraph a {")
  for name, (i, dests) in modules.items():
    for dest in dests:
      print("%s%s -> %s%s;" % (prefix(modules, name), name, 
          prefix(modules, dest), dest))
  print("}")
#graphviz(modules)
print(simulate(modules, 1000))
periods, inputs = simulate(modules, 20000000)
#print(simple_nands(modules, periods, inputs))

  
