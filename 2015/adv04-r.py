import aoc
import itertools
import sys
import multiprocessing

def eval_md5(i, zeros):
  ans = aoc.md5(seed + str(i))
  if ans.startswith(zeros):
    return i
  return None

# multiprocessing is slower than single thread,
# maybe there is a hidden mutex in the lib.
def search_multi(zeros, pool):
  fac = 128
  for i in itertools.count(0, CPU * fac):
    #ans = [eval_md5(ii, zeros) for ii in range(i, i + CPU)]
    ans = list(pool.starmap(eval_md5, ((ii, zeros) for ii in range(i, i + CPU * fac)), fac))
    valid = [m for m in ans if m is not None]
    if valid:
      return min(valid)
  return None

def search(zeros, pool):
  for i in itertools.count(0):
    md5 = aoc.md5(seed + str(i))
    if md5.startswith(zeros):
      return i
  return None

seed = sys.stdin.read().strip()
CPU = 1
with multiprocessing.Pool(CPU) as pool:
  aoc.cprint(search("0" * 5, pool))
  aoc.cprint(search("0" * 6, pool))
