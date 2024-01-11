import sys
import aoc

def simulate(prog):
  state = aoc.ddict(lambda: 0)
  tmax = []
  for q in prog:
    a = state[q.vcond]
    if eval(f"{a} {q.cond} {q.ncond}"):
      match q.inc:
        case "inc":
          state[q.var] += q.value
        case "dec":
          state[q.var] -= q.value
    tmax.append(max(state.values()))
  return tmax

lines = [line.strip() for line in sys.stdin]
prog = []
for line in lines:
  q = aoc.retuple("var inc value_ vcond cond ncond_",
      r"(\w+) (inc|dec) ([-+]?\d+) if (\w+) (\S+) ([-+]?\d+)", line)
  prog.append(q)
aoc.cprint(simulate(prog)[-1])
aoc.cprint(max(simulate(prog)))
