import sys
import string
import aoc
import re

def count(line):
  seq = aoc.bidi(line)
  prev, pos = seq.start, seq.next(seq.start)
  while seq.valid(pos):
    if seq.value(pos) == seq.value(prev).swapcase():
      seq.remove(pos)
      seq.remove(prev)
      prev, pos = seq.prev(prev), seq.next(pos)
      if not seq.valid(prev):
        prev, pos = pos, seq.next(pos)
    else:
      prev, pos = pos, seq.next(pos)
  return len(seq)

def checkall(line):
  for c in string.ascii_lowercase:
    yield count(line.replace(c, "").replace(c.upper(), ""))

line = sys.stdin.read().strip()
aoc.cprint(count(line))
aoc.cprint(min(checkall(line)))
