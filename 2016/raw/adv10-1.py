import sys
import re
import itertools
import math
import aoc
from collections import *

def process(storage, commands, bot):
  if len(storage[bot]) >= 2 and commands[bot]:
    low, high = commands[bot].pop(0)
    lvalue, hvalue = min(storage[bot]), max(storage[bot])
    if (lvalue, hvalue) == (17, 61):
      aoc.cprint(bot)
    storage[bot].remove(lvalue)
    storage[bot].remove(hvalue)
    storage[low].append(lvalue)
    storage[high].append(hvalue)
    process(storage, commands, low)
    process(storage, commands, high)

storage = aoc.ddict(lambda: [])
commands = aoc.ddict(lambda: [])
for line in sys.stdin:
  if line.startswith("value"):
    t = aoc.retuple("value_ bot_", r".*?(\d+).*?(\d+)", line)
    storage[t.bot].append(t.value)
    process(storage, commands, t.bot)
  else:
    t = aoc.retuple("bot_ out1 low_ out2 high_", r".*?(\d+).*?(output|bot).*?(\d+).*?(output|bot).*?(\d+)", line)
    commands[t.bot].append((t.low, t.high))
    process(storage, commands, t.bot)


  
