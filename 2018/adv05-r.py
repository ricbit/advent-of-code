import sys
import string
import aoc
import multiprocessing

def count(line):
  seq = aoc.bidi(line, circular=False)
  prev, pos = seq.start, seq.next(seq.start)
  while seq.valid(pos):
    if seq.value(pos) == seq.value(prev).swapcase():
      seq.remove(pos)
      seq.remove(prev)
      prev, pos = seq.prev(prev), seq.next(pos)
      if seq.valid(prev):
        continue
    prev, pos = pos, seq.next(pos)
  return len(seq)

def checkone(line, c):
  return count(line.replace(c, "").replace(c.upper(), ""))

line = sys.stdin.read().strip()
aoc.cprint(count(line))
with multiprocessing.Pool() as pool:
  aoc.cprint(min(pool.starmap(checkone, ((line, c) for c in string.ascii_lowercase))))
