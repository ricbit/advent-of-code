import sys
import aoc

def check(state):
  d = state["d"]
  e = state["e"]
  b = state["b"]
  s = int(b ** 0.5) + 2
  for i in range(d, s):
    if b % i == 0 and e <= b // d <= b:
      return 0
  return 1

def maybe(state, x):
  if x.isalpha():
    return state[x]
  else:
    return int(x)

def simulate(prog, a):
  pc = 0
  state = {r: 0 for r in "abcdefgh"}
  state['a'] = a
  count = 0
  while pc < len(prog):
    match prog[pc]:
      case "set", x, y:
        state[x] = maybe(state, y)
      case "sub", x, y:
        state[x] -= maybe(state, y)
      case "mul", x, y:
        state[x] *= maybe(state, y)
        count += 1
      case "jnz", x, y:
        if maybe(state, x):
          pc += maybe(state, y) - 1
      case "chk", x, y:
        state['f'] = check(state)
    pc += 1
  return count, state['h']

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  prog.append(line.split(";")[0].strip().split(" "))
aoc.cprint(simulate(prog, 0)[0])
patch = """
    sub a 0
    chk f 0
    set g 0
    set e b
    sub a 0
    sub a 0
    sub a 0
    set d b
"""
patch = patch.strip().strip("\n")
for i, line in enumerate(patch.split("\n")):
  prog[i + 16] = line.strip().split()
aoc.cprint(simulate(prog, 1)[1])
