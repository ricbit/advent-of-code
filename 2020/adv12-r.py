import aoc

def process(actions, waydir, relative=True):
  cdir = aoc.get_cdir("N")
  pos = 0
  for action in actions:
    if action.cdir in cdir:
      delta = cdir[action.cdir] * action.value
      if relative:
        pos += delta
      else:
        waydir += delta
    elif action.cdir == "F":
      pos += waydir * action.value
    elif action.cdir == "R":
      waydir = waydir * (1j) ** (action.value // 90)
    elif action.cdir == "L":
      waydir = waydir * (-1j) ** (action.value // 90)
  return int(abs(pos.real) + abs(pos.imag))

def part1(actions):
  return process(actions, 1, True)

def part2(actions):
  return process(actions, 10 - 1j, False)

data = aoc.retuple_read("cdir value_", r"(.)(\d+)")
aoc.cprint(part1(data))
aoc.cprint(part2(data))
