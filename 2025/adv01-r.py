import aoc

def solve(data):
  pos = 50
  part1, part2 = 0, 0
  for line in data:
    direction = 1 if line.d == "R" else -1
    for i in range(line.size):
      pos += direction
      if pos % 100 == 0:
        part2 += 1
    if pos % 100 == 0:
      part1 += 1
  return part1, part2

data = aoc.retuple_read("d size_", r"(.)(\d+)")
part1, part2 = solve(data)
aoc.cprint(part1)
aoc.cprint(part2)
