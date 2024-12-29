import aoc

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

def solve(regs, program):
  pc, ans = 0, []
  regs = [regs[i] for i in range(3)]
  while pc < len(program):
    match program[pc]:
      case 0: # adv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[0] = d
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
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[1] = d
      case 7: # cdv
        d = regs[0] // (2 ** combo(regs, program[pc + 1]))
        regs[2] = d
    pc += 2
  return ans

class Sim:
  def __init__(self, prog):
    self.prog = prog

  def rec(self, front, psize, shift, size):
    if shift == 0:
      return front
    incr = 2 ** (shift * 3 - 3)
    limit = incr * (2 ** size)
    for i in range(0, limit, incr):
      regs = {0: front + i, 1: 0, 2: 0}
      ans = solve(regs, self.prog)
      if ans[-psize:] == self.prog[-psize:]:
        found = self.rec(front + i, psize + 1, shift - 1, 3)
        if found is not None:
          return found
    return None

  def search(self):
    return self.rec(0, 1, len(self.prog), 9)

data = aoc.line_blocks()
regs, program = parse(data)
aoc.cprint(",".join(map(str, solve(regs, program))))
aoc.cprint(Sim(program).search())
