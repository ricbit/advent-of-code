import aoc
import functools

def solve(data):
  rulebook, pages = data
  rules = aoc.ddict(list)
  for rule in rulebook:
    a, b = rule.split("|")
    rules[a].append(b)
  part1, part2 = 0, 0
  comp = lambda a, b: 1 if a in rules[b] else -1
  middle = lambda page: int(page[len(page) // 2])
  for page in pages:
    page = page.split(",")
    sorted_page = list(sorted(page, key=functools.cmp_to_key(comp)))
    if page == sorted_page:
      part1 += middle(page)
    else:
      part2 += middle(sorted_page)
  return part1, part2

data = aoc.line_blocks()
part1, part2 = solve(data)
aoc.cprint(part1)
aoc.cprint(part2)
