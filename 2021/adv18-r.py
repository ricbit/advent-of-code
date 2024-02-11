import sys
import itertools
import aoc

fishes = [eval(line) for line in sys.stdin]

def toposort(fish, current):
  if type(fish[0]) is not int:
    left, current = toposort(fish[0], current)
  else:
    left, current = (fish[0], current), current + 1
  if type(fish[1]) is not int:
    right, current = toposort(fish[1], current)
  else:
    right, current = (fish[1], current), current + 1
  return [left, right], current

def explode(fish, level, changes):
  if level < 3:
    if type(fish[0]) is list:
      left, exploded = explode(fish[0], level + 1, changes)
      if exploded:
        return [left, fish[1]], True
    else:
      left = fish[0]
    if type(fish[1]) is list:
      right, exploded = explode(fish[1], level + 1, changes)
      if exploded:
        return [fish[0], right], True
    else:
      right = fish[1]
    return [left, right], False
  else:
    if type(fish[0]) is list:
      left = (0, None)
      changes[fish[0][0][1] - 1] = fish[0][0][0]
      changes[fish[0][1][1] + 1] = fish[0][1][0]
      return [left, fish[1]], True
    if type(fish[1]) is list:
      right = (0, None)
      changes[fish[1][0][1] - 1] = fish[1][0][0]
      changes[fish[1][1][1] + 1] = fish[1][1][0]
      return [fish[0], right], True
    return fish, False

def apply_changes(fish, changes):
  if type(fish[0]) is list:
    left = apply_changes(fish[0], changes)
  elif fish[0][1] in changes:
    left = fish[0][0] + changes[fish[0][1]]
  else:
    left = fish[0][0]
  if type(fish[1]) is list:
    right = apply_changes(fish[1], changes)
  elif fish[1][1] in changes:
    right = fish[1][0] + changes[fish[1][1]]
  else:
    right = fish[1][0]
  return [left, right]

def split(fish, found):
  left, right = fish
  if type(fish[0]) is list:
    left, found = split(fish[0], False)
    if found:
      return [left, fish[1]], True
  elif fish[0] >= 10:
    left = [fish[0] // 2, (fish[0] + 1) // 2]
    return [left, fish[1]], True
  if type(fish[1]) is list:
    right, found = split(fish[1], False)
    if found:
      return [fish[0], right], True
  elif fish[1] >= 10:
    right = [fish[1] // 2, (fish[1] + 1) // 2]
    return [fish[0], right], True
  return [left, right], False

def reduce_fishes(fish):
  found = True
  while found:
    toposorted = toposort(fish, 0)[0]
    changes = {}
    exploded, found = explode(toposorted, 0, changes)
    fish = apply_changes(exploded, changes)
    if found:
      continue
    fish, found = split(fish, False)
  return fish

def allfish():
  ans = reduce_fishes(fishes[0])
  for fish in fishes[1:]:
    ans = [ans, fish]
    ans = reduce_fishes(ans)
  return ans

def magnitude(fish):
  if type(fish[0]) is not int:
    left = magnitude(fish[0])
  else:
    left = fish[0]
  if type(fish[1]) is not int:
    right = magnitude(fish[1])
  else:
    right = fish[1]
  return 3 * left + 2 * right

def allreduce():
  for fish in fishes:
    print(reduce_fishes(fish))

aoc.cprint(magnitude(allfish()))
ans = []
for a, b in itertools.permutations(fishes, 2):
  fish = [a, b]
  ans.append(magnitude(reduce_fishes(fish)))
print(max(ans))
