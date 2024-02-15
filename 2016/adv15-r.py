import sys
import itertools
import aoc
from multiprocessing import Pool

discs = None

def simulate(time):
  for t, disc in enumerate(discs):
    if (time + disc.pos + t + 1) % disc.mod != 0:
      return False
  return True

def bulk_simulation(discs):
  M = 1000000
  with Pool() as pool:
    for bulk in itertools.count():
      results = list(pool.imap(simulate, (bulk * M + i for i in range(M)), 125000))
      for i, result in enumerate(results):
        if result:
          return bulk * M + i

def solve(lines):
  global discs
  discs = []
  for line in lines:
    discs.append(aoc.retuple(
        "disc mod_ time_ pos_", r".*?(\d+).*?(\d+).*?(\d+).*?(\d+)", line))
  return bulk_simulation(discs)

lines = sys.stdin.readlines()
aoc.cprint(solve(lines))
lines.append("1000 11 0 0")
aoc.cprint(solve(lines))
  
