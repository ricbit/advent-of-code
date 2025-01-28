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

def simulate(lines, inter, maximize):
  s = z3.Optimize()
  s.set(timeout=60 * 1000)
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
  for addr, zinter in zip(range(len(lines) + 1), inter):
    for c, (a, b) in zinter.items():
      s.add(zvar[addr][c] <= z3.BitVecVal(b, size))
      #if a >= 0:
      s.add(zvar[addr][c] >= z3.BitVecVal(a - 1, size))
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
  print(s.check())
  print(s.statistics())
  m = s.model()
  return "".join(str(m.evaluate(v)) for v in values)

def intervals(lines):
  regs = {c: (0, 0) for c in "xyzw"}
  ans = [regs]
  print(regs.copy())
  for i, line in enumerate(lines):
    match line.split():
      case "inp", reg:
        regs[reg] = (1, 9)
      case "add", a, b:
        if b[0] in "xyzw":
          regs[a] = (min(regs[a][0] + regs[b][0], regs[a][0] + regs[b][1]),
                     max(regs[a][1] + regs[b][0], regs[a][1] + regs[b][1]))
        else:
          regs[a] = (regs[a][0] + int(b), regs[a][1] + int(b))
      case "mul", a, b:
        if b[0] in "xyzw":
          regs[a] = (min(regs[a][0] * regs[b][0], regs[a][0] * regs[b][1]),
                     max(regs[a][1] * regs[b][0], regs[a][1] * regs[b][1]))
        else:
          regs[a] = (regs[a][0] * int(b), regs[a][1] * int(b))
      case "div", a, b:
        if b[0] in "xyzw":
          regs[a] = (regs[a][0] // regs[b][1],
                     regs[a][1] // regs[b][0])
        else:
          regs[a] = (regs[a][0] // int(b), regs[a][1] // int(b))
      case "mod", a, b:
        if b[0] in "xyzw":
          print("bug")
        else:
          if regs[a][1] >= int(b):
            regs[a] = (0, int(b) - 1)
      case "eql", a, b:
        regs[a] = (0, 1)
    ans.append(regs.copy())
    print(line.strip(), regs)
  return ans
 
lines = [line.strip() for line in sys.stdin]
inter = intervals(lines)
aoc.cprint(simulate(lines, inter, True))
aoc.cprint(simulate(lines, inter, False))
