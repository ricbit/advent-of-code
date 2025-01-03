import sys
import aoc
import functools

@functools.lru_cache(maxsize=None)
def build(ports, pos, used, size):
  ans = []
  for i, port in enumerate(ports):
    mask = 1 << i
    if mask & used != 0:
      continue
    if port[0] == pos or port[1] == pos:
      npos = port[0] + port[1] - pos
      nsize, nstr = build(ports, npos, used + mask, size)
      nsize = nsize + 1 if size is not None else None
      ans.append((nsize, port[0] + port[1] + nstr))
  return max(ans) if ans else (0, 0)

lines = [line.strip() for line in sys.stdin]
ports = []
for line in lines:
  ports.append(tuple(int(i) for i in line.split("/")))
aoc.cprint(build(tuple(ports), 0, 0, None)[1])
aoc.cprint(build(tuple(ports), 0, 0, 0)[1])
