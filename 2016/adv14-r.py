import sys
import re
import itertools
import aoc
from multiprocessing import Pool

def get(i, salt, blocks):
  value = salt + str(i)
  for i in range(blocks):
    value = aoc.md5(value)
  return value

def get_md5_range(salt, blocks):
  with Pool() as pool:
    for start in itertools.count(0):
      yield list(pool.starmap(get, ((i + start * 1000, salt, blocks) for i in range(1000))))

def search(salt, blocks):
  it = get_md5_range(salt, blocks)
  prev = next(it)
  vnext = next(it)
  for i in itertools.count(): 
    char = re.match(r".*?(\w)\1\1", prev[i % 1000])
    if char is not None:
      char = char.group(1) * 5
      for j in range(1000):
        if i % 1000 != j and char in prev[j]:
          yield i
          break
    prev[i % 1000] = vnext[i % 1000]
    if i % 1000 == 999:
      vnext = next(it)

def count(salt, blocks):
  for i, value in enumerate(search(salt, blocks)):
    if i == 63:
      return value

salt = sys.stdin.read().strip()
aoc.cprint(count(salt, 1))
aoc.cprint(count(salt, 2017))
