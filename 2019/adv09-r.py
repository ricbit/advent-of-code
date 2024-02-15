import sys
import itertools
import aoc
from collections import deque
from aoc.refintcode import IntCode

data = [int(i) for i in sys.stdin.read().split(",")]

cpu = IntCode(data[:])
cpu.input = 1
cpu.run()
aoc.cprint(cpu.output)

cpu = IntCode(data)
cpu.input = 2
cpu.run()
aoc.cprint(cpu.output)
