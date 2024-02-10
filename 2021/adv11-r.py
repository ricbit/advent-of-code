import sys
import copy
import itertools
import aoc

lines = [line.strip() for line in sys.stdin]
energy = aoc.Table([[int(i) for i in line] for line in lines])

def increment(energy):
  for j, i in energy.iter_all():
    energy[j][i] += 1

def update_candidates(energy, flash):
  flashes = 0
  adds = [[0] * energy.w for i in range(energy.h)]
  for j, i in energy.iter_all():
    if energy[j][i] > 9 and not flash[j][i]:
      flash[j][i] = True
      flashes += 1
      for jj, ii in energy.iter_neigh8(j, i):
        adds[jj][ii] += 1
  for j, i in energy.iter_all():
    energy[j][i] += adds[j][i]
  return flashes

def step(energy):
  flash = [[False] * energy.w for i in range(energy.h)]
  increment(energy)
  flashes = 0
  while (new_flashes := update_candidates(energy, flash)):
    flashes += new_flashes
  for j, i in energy.iter_all():
    if energy[j][i] > 9:
      energy[j][i] = 0
  return flashes

def search1(energy):
  ans = 0
  for i in range(100):
    ans += step(energy)
  return ans

def search2(energy):
  for i in itertools.count(1):
    step(energy)
    if sum(sum(i) for i in energy) == 0:
      return i

aoc.cprint(search1(copy.deepcopy(energy)))
aoc.cprint(search2(energy))
