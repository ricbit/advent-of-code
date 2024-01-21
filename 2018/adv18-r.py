import aoc
import copy

def solve(t):
  while True:
    t2 = copy.deepcopy(t)
    for j, i in t.iter_all():
      ground, tree, lumber = 0, 0, 0
      for jj, ii in t.iter_neigh8(j, i):
        match t[jj][ii]:
          case ".":
            ground += 1
          case "|":
            tree += 1
          case "#":
            lumber += 1
      match t[j][i]:
        case "." if tree >= 3:
          t2[j][i] = "|"
        case "|" if lumber >= 3:
          t2[j][i] = "#"
        case "#" if not (lumber >= 1 and tree >= 1):
          t2[j][i] = "."
    t = t2
    yield tuple(aoc.flatten(t.table))

def resource(key):
  tree = key.count("|")
  lumber = key.count("#")
  return tree * lumber 

t = aoc.Table.read()
aoc.cprint(aoc.extrapolate(solve(t), 10, resource))
aoc.cprint(aoc.extrapolate(solve(t), 1000000000, resource))
