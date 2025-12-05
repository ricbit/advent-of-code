import aoc

def part1(ranges, products):
  ans = 0
  for k in products:
    ans += any(k in r for r in ranges)
  return ans

def add_inter(all_inter, i):
  for a in all_inter:
    if list(a.inter(i)):
      for x in i.sub(a):
        add_inter(all_inter, x)
      return
  all_inter.append(i)

def part2(ranges):
  all_inter = []
  for r in ranges:
    add_inter(all_inter, r)
  return sum(len(i) for i in all_inter)

ranges, products = aoc.line_blocks()
ranges = [aoc.Interval(*map(int, r.split("-"))) for r in ranges]
products = aoc.ints(products)
aoc.cprint(part1(ranges, products))
aoc.cprint(part2(ranges))
