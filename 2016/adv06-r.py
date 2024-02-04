import sys
import itertools
import aoc
from collections import *

def get_message(tlines, func):
  message = []
  for line in tlines:
    ans = []
    for k, v in itertools.groupby(line):
      ans.append((len(list(v)), k))
    message.append(func(ans)[1])
  return "".join(message)

lines = [line.strip() for line in sys.stdin]
tlines = [list(sorted(x)) for x in zip(*lines)]
aoc.cprint(get_message(tlines, max))
aoc.cprint(get_message(tlines, min))

