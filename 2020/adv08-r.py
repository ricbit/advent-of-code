import aoc
import itertools

def simulate(mem, early_stop=False):
  pc, acc, count = 0, 0, 0
  limit = 1000
  visited = set()
  while True:
    count += 1
    if pc == len(mem) or (early_stop and pc in visited):
      return acc
    if count > limit:
      return None
    visited.add(pc)
    match mem[pc]:
      case "nop", _: 
        pass        
      case "acc", value:
        acc += value
      case "jmp", value:
        pc = pc + value -1
    pc += 1

def search(mem):
  for i in range(len(mem)):
    for a, b in itertools.permutations(["nop", "jmp"]):
      if mem[i][0] == a:
        mem[i][0] = b
        if (ans := simulate(mem)) is not None:
          return ans
        mem[i][0] = a

data = [[x.opcode, x.value] for x in aoc.retuple_read("opcode value_", r"(\w+) ([-+0-9]+)")]
aoc.cprint(simulate(data, early_stop=True))
aoc.cprint(search(data))
