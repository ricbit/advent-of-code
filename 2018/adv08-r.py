import sys
import aoc

def sum_meta(data, pos, meta):
  return sum(data[pos : pos + meta])

def calc1(data, pos, meta, ch):
  return sum(ch.values()) + sum_meta(data, pos, meta)

def calc2(data, pos, meta, ch):
  if not ch:
    return sum_meta(data, pos, meta)
  else:
    return sum(ch[data[pos + i] - 1] for i in range(meta))

def parse(data, pos, calc):
  children = data[pos]
  meta = data[pos + 1]
  pos += 2
  ch = aoc.ddict(lambda: 0)
  for i in range(children):
    cmeta, pos = parse(data, pos, calc)
    ch[i] = cmeta
  ans = calc(data, pos, meta, ch)
  pos += meta
  return ans, pos

data = aoc.ints(sys.stdin.read().strip().split())
aoc.cprint(parse(data, 0, calc1)[0])
aoc.cprint(parse(data, 0, calc2)[0])
