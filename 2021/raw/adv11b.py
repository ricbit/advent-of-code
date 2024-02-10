import sys
import itertools

lines = [line.strip() for line in sys.stdin]
energy = [[int(i) for i in line] for line in lines]
h, w = 10, 10

def neigh(y, x):
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i != 0 or j != 0:
        yield (y + j, x + i)

def valid(y, x):
  for j, i in neigh(y, x):
    if j >= 0 and j < h and i >= 0 and i < w:
      yield (j, i)

def increment(energy):
  for j in range(h):
    for i in range(w):
      energy[j][i] += 1

def printenergy(energy):
  for hh in energy:
    print(hh)
  print("--")

def update_candidates(energy, flash):
  flashes = 0
  adds = [[0] * w for i in range(h)]
  for j in range(h):
    for i in range(w):
      if energy[j][i] > 9 and not flash[j][i]:
        flash[j][i] = True
        flashes += 1
        for jj, ii in valid(j, i):
          adds[jj][ii] += 1
  for j in range(h):
    for i in range(w):
      energy[j][i] += adds[j][i]
  return flashes


def step(energy):
  flash = [[False] * w for i in range(h)]
  increment(energy)
  flashes = 0
  while True:
    new_flashes = update_candidates(energy, flash)
    if new_flashes:
      flashes += new_flashes
    else:
      break
  for j in range(h):
    for i in range(w):
      if energy[j][i] > 9:
        energy[j][i] = 0
  return flashes

for i in itertools.count(1):
  step(energy)
  if sum(sum(i) for i in energy) == 0:
    print(i)
    break
