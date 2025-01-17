import sys
import aoc
from aoc.assembunny import Assembunny

lines = [line.strip() for line in sys.stdin]
asm = Assembunny(lines)
state = {"a": 0, "b": 0, "c": 0, "d": 0}
aoc.cprint(asm.simulate(state)['a'])
state = {"a": 0, "b": 0, "c": 1, "d": 0}
aoc.cprint(asm.simulate(state)['a'])
