import aoc
import functools

def combo(regs, val):
  if val < 4:
    return val
  return regs[val - 4]

def parse(data):
  register, program = data
  regs = {}
  for line in register:
    x = aoc.retuple("name val_", r"Register (\w): (\d+)", line)
    regs[ord(x.name) - ord("A")] = x.val
  program = aoc.ints(program[0].split(":")[1].strip().split(","))
  return regs, program

def solve_part1(regs, program):
  pc, ans = 0, []
  while pc < len(program):
    match program[pc]:
      case 0: # adv
        regs[0] = regs[0] // (2 ** combo(regs, program[pc + 1]))
      case 1: # bxl
        regs[1] ^= program[pc + 1]
      case 2: # bst
        regs[1] = combo(regs, program[pc + 1]) % 8
      case 3: # jnz
        if regs[0] != 0:
          pc = program[pc + 1] - 2
      case 4: # bxc
        regs[1] ^= regs[2]
      case 5: # out
        ans.append(combo(regs, program[pc + 1]) % 8)
      case 6: # bdv
        regs[1] = regs[0] // (2 ** combo(regs, program[pc + 1]))
      case 7: # cdv
        regs[2] = regs[0] // (2 ** combo(regs, program[pc + 1]))
    pc += 2
  return ",".join(str(i) for i in ans)

@functools.cache
def simulate(a):
  b, c = 0, 0
  ans = []
  while a:
    b = a % 8
    b = b ^ 5 
    c = a >> b
    b = b ^ 6
    a = a >> 3
    b = b ^ c
    ans.append(b % 8)
  return ans

class Sim:
  def __init__(self, prog):
    self.prog = prog
    self.minback = 1e20

  @functools.cache
  def rec(self, x):
    back, shift = x
    if shift == len(self.prog):
      if simulate(back) == self.prog:
        self.minback = min(back, self.minback)
      return
    for i in range(128 * 8):
      stable = 2 ** (3 * shift)
      n = back + i * stable
      if simulate(n)[:shift + 1] == self.prog[:shift + 1]:
        if n < self.minback:
          self.rec((n % (stable * 8), shift + 1))

  def search(self):
    self.rec((0, 0))
    return self.minback

data = aoc.line_blocks()
regs, program = parse(data)
aoc.cprint(solve_part1(regs, program))
s = Sim(program)
aoc.cprint(s.search())
