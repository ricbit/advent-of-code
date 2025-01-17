import sys
import aoc
import z3

def read(reg, addr, zvar):
  if reg[0] in "xyzw":
    return zvar[addr - 1][reg]
  return int(reg)

def add_wires(s, zvar, addr, a):
  for c in 'xyzw':
    if c != a:
      s.add(zvar[addr][c] == zvar[addr - 1][c])

def simulate(lines, maximize):
  s = z3.Optimize()
  s.set(timeout=3 * 60 * 1000)
  size = 64
  zvar = [{c: z3.BitVec(f"{c}_{i}", size) for c in 'xyzw'}
          for i in range(1 + len(lines))]
  values = [z3.BitVec(f'value_{i}', size) for i in range(14)]
  zero, one = z3.BitVecVal(0, size), z3.BitVecVal(1, size)
  s.add(zvar[0]['x'] == zero)
  s.add(zvar[0]['y'] == zero)
  s.add(zvar[0]['z'] == zero)
  s.add(zvar[0]['w'] == zero)
  for i in range(14):
    s.add(values[i] > zero)
    s.add(values[i] <= z3.BitVecVal(9, size))
  cur = 0
  for addr, line in enumerate(lines, 1):
    match line.split():
      case "inp", reg:
        s.add(zvar[addr][reg] == values[cur])
        cur += 1
        add_wires(s, zvar, addr, reg)
      case "add", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] + read(b, addr, zvar))
        add_wires(s, zvar, addr, a)
      case "mul", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] * read(b, addr, zvar))
        add_wires(s, zvar, addr, a)
      case "div", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] / read(b, addr, zvar))
        add_wires(s, zvar, addr, a)
        if b[0] in "xyzw":
          s.add(zvar[addr - 1][b] != zero)
      case "mod", a, b:
        s.add(zvar[addr][a] == zvar[addr - 1][a] % read(b, addr, zvar))
        add_wires(s, zvar, addr, a)
        s.add(zvar[addr - 1][a] >= zero)
        if b[0] in "xyzw":
          s.add(zvar[addr - 1][b] > zero)
      case "eql", a, b:
        s.add(zvar[addr][a] == z3.If(
            zvar[addr - 1][a] == read(b, addr, zvar), one, zero))
        add_wires(s, zvar, addr, a)
  s.add(zvar[-1]['z'] == zero)
  output = sum(values[13 - cur] * 10 ** cur for cur in range(14))
  if maximize:
    s.maximize(output)
  else:
    s.minimize(output)
  s.check()
  m = s.model()
  return "".join(str(m.evaluate(v)) for v in values)

lines = [line.strip() for line in sys.stdin]
aoc.cprint(simulate(lines, True))
aoc.cprint(simulate(lines, False))
