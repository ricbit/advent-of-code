import sys
import aoc

class Wires:
  def __init__(self, fixed):
    self.wires = {}
    self.fixed = fixed

  def __getitem__(self, value):
    if value.isdigit():
      return int(value)
    elif value in self.fixed:
      return self.fixed[value]
    else:
      return self.wires[value]

  def __setitem__(self, key, value):
    self.wires[key] = value

  def __contains__(self, value):
    return value in self.wires or value in self.fixed

def valid(wires, op1, op2):
  if not (op1.isdigit() or op1 in wires):
    return False
  if not (op2.isdigit() or op2 in wires):
    return False
  return True

def process_wire(wires, line):
  src, dst = line.strip().split(" -> ")  
  match src.split():
    case [val] if val.isdigit() or val in wires:
      wires[dst] = wires[val]
    case ["NOT", val] if val.isdigit() or val in wires:
      wires[dst] = (~(wires[val])) & 0xFFFF
    case [op1, "AND", op2] if valid(wires, op1, op2):
      wires[dst] = wires[op1] & wires[op2]
    case [op1, "OR", op2] if valid(wires, op1, op2):
      wires[dst] = wires[op1] | wires[op2]
    case [op1, "LSHIFT", op2] if valid(wires, op1, op2):
      wires[dst] = wires[op1] << wires[op2]
    case [op1, "RSHIFT", op2] if valid(wires, op1, op2):
      wires[dst] = wires[op1] >> wires[op2]
    case _:
      return False
  return True

def process_all(lines, fixed):
  wires = Wires(fixed)
  while lines:
    vnext = []
    for line in lines:
      if not process_wire(wires, line):
        vnext.append(line)
    lines = vnext
  return wires['a']

lines = sys.stdin.readlines()
first = process_all(lines, {})
aoc.cprint(first)
aoc.cprint(process_all(lines, {"b": first}))

      
