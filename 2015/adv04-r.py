import hashlib
import aoc
import itertools
import sys

def search(seed, size):
  zeros = "0" * size
  for i in itertools.count(0):
    m = hashlib.md5()
    m.update(bytes(seed, "ascii") + bytes(str(i), "ascii"))
    ans = m.hexdigest()
    if ans.startswith(zeros):
      return i

seed = sys.stdin.read().strip()
aoc.cprint(search(seed, 5))
aoc.cprint(search(seed, 6))
