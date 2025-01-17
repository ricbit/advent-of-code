import sys
import aoc
from aoc.assembunny import Assembunny

lines = [line.strip() for line in sys.stdin]
asm = Assembunny(lines)
state = {"a": 0, "b": 0, "c": 0, "d": 0}
base = asm.simulate(state, breakpoint=9)['a']
size = (len(bin(base)) - 2) // 2
out = int("10" * size, 2) - base
aoc.cprint(out)
