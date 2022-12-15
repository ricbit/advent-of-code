import sys

lines = sys.stdin.readlines()

def commands():
  for line in lines:
    match line.strip().split():
      case ["noop"]:
        yield 0
      case ["addx", number]:
        yield 0
        yield int(number)
  yield 0

def engine():
  x = 1
  for clock, command in enumerate(commands()):
    yield clock + 1, x
    x += command

def first():
  signal = 0
  dump = [20 + 40 * i for i in range(6)]
  for clock, x in engine():
    if clock in dump:
      signal += x * clock
  return signal  

def crt():
  for j in range(6):
    for i in range(40):
      yield j, i

def second():
  grid = [["."] * 40 for _ in range(6)]
  for (j, i), (clock, x) in zip(crt(), engine()):
    if x - 1 <= i <= x + 1:
      grid[j][i] = "#"
  return grid

print(first())
print("\n".join("".join(line) for line in second()))

