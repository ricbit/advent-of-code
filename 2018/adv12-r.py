import aoc

def solve(initial, rules):
  plants = set(i for i, c in enumerate(initial) if c == "#")
  last_diffs, old_sum = list(range(5)), sum(plants)
  old_sum = sum(plants)
  for gen in range(2000):
    newplants = set()
    for x in range(min(plants) - 4, max(plants) + 4):
      pots = []
      for i in range(5):
        pots.append("#" if (x + i) in plants else ".")
      if rules.get("".join(pots), ".") == "#":
        newplants.add(x + 2)
    last_diffs, old_sum = last_diffs[1:] + [sum(plants) - old_sum], sum(plants)
    if len(set(last_diffs)) == 1:
      break
    plants = newplants
  return sum(plants) + (50000000000 - gen) * last_diffs[0]

data = aoc.line_blocks()
initial = data[0][0].split(": ")[1]
rules = {}
for line in data[1]:
  q = aoc.retuple("src dst", r"(.+) => (.)", line)
  rules[q.src] = q.dst
aoc.cprint(solve(initial, rules))
