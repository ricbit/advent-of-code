import re
import aoc

def terminals(seq):
  return tuple(re.findall(r"([A-Z](?:[a-z])?)", seq))

def build_chomsky(forward):
  grammar = aoc.ddict(lambda: set())
  cur = 0
  for src, dsts in forward.items():
    for dst in dsts:
      if len(dst) <= 2:
        grammar[src].add(dst)
      key, val = src, dst
      while len(val) > 2:
        newkey = f"V{cur}"
        cur += 1
        grammar[key].add((val[0], newkey))
        key = newkey
        val = val[1:]
      grammar[key].add(val)
  return grammar

def parse(grammar, goal):
  reachable = {}
  for i, term in enumerate(goal):
    reachable[(i, term, 1)] = 0
  for size in range(1, len(goal)):
    for key, values in grammar.items():
      for value in values:
        for i in range(len(goal)):
          for s in range(1, size + 1):
            if (i, value[0], s) in reachable and (i + s, value[1], size - s + 1) in reachable:
              fac = 0 if key.startswith("V") else 1
              reachable[(i, key, size + 1)] = fac + min(
                reachable.get((i, key, size + 1), 1e6),
                reachable[(i, value[0], s)] + reachable[(i + s, value[1], size - s + 1)])
  return reachable[(0, "e", len(goal))]

def simple(forward, goal):
  molecules = set()
  for i in range(len(goal)):
    for sub in forward[goal[i]]:
      molecules.add("".join(goal[0:i] + sub + goal[i + 1:len(goal)]))
  return len(molecules)

blocks = aoc.line_blocks()
goal = blocks[1][0]
subs = aoc.ddict(lambda: set())
forward = aoc.ddict(lambda: set())
for line in blocks[0]:
  src, dst = line.split(" => ")
  forward[src].add(terminals(dst))
aoc.cprint(simple(forward, terminals(goal)))
grammar = build_chomsky(forward)
aoc.cprint(parse(grammar, terminals(goal)))
