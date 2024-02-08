import sys

def get(wires, val):
  if val.isdigit():
    return int(val)
  else:
    if val == "b":
      return 16076
    else:
      return wires[val]

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
      wires[dst] = get(wires, val)
    case ["NOT", val] if val.isdigit() or val in wires:
      wires[dst] = (~(get(wires, val))) & 0xFFFF
    case [op1, "AND", op2] if valid(wires, op1, op2):
      wires[dst] = get(wires, op1) & get(wires, op2)
    case [op1, "OR", op2] if valid(wires, op1, op2):
      wires[dst] = get(wires, op1) | get(wires, op2)
    case [op1, "LSHIFT", op2] if valid(wires, op1, op2):
      wires[dst] = get(wires, op1) << get(wires, op2)
    case [op1, "RSHIFT", op2] if valid(wires, op1, op2):
      wires[dst] = get(wires, op1) >> get(wires, op2)
    case _:
      return False
  return True

def process_all(lines, b = None):
  wires = {} if b is None else {'b': b}
  while lines:
    vnext = []
    for line in lines:
      if not process_wire(wires, line):
        vnext.append(line)
    lines = vnext
  return wires['a']

lines = sys.stdin.readlines()
print(process_all(lines))
print(process_all(lines, b=16076))

      
