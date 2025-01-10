import sys
import aoc
import functools
import multiprocessing

@functools.lru_cache(maxsize=None)
def build(pos, used, size):
  ans = []
  for i, port in enumerate(ports):
    mask = 1 << i
    if mask & used != 0:
      continue
    if pos in port:
      npos = port[0] + port[1] - pos
      nsize, nstr = build(npos, used + mask, size)
      nsize = nsize + 1 if size is not None else None
      ans.append((nsize, port[0] + port[1] + nstr))
  return max(ans) if ans else (0, 0)

def inner_build(pos, used, size, i):
  mask = 1 << i
  port = ports[i]
  if mask & used != 0:
    return None
  if port[0] == pos or port[1] == pos:
    npos = port[0] + port[1] - pos
    nsize, nstr = build(npos, used + mask, size)
    nsize = nsize + 1 if size is not None else None
    return (nsize, port[0] + port[1] + nstr)
  return None

def base_build(pos, used, size, pool):
  ans = pool.starmap(inner_build, ((pos, used, size, i) for i in range(len(ports))))
  return max(s for s in ans if s is not None)

lines = [line.strip() for line in sys.stdin]
ports = []
for line in lines:
  ports.append(tuple(int(i) for i in line.split("/")))
with multiprocessing.Pool() as pool:
  aoc.cprint(base_build(0, 0, None, pool)[1])
  aoc.cprint(base_build(0, 0, 0, pool)[1])
