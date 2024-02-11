import re
import sys

def read_stacks():
  stacks = [[] for _ in range(9)]
  for line in sys.stdin:
    size = len(line.rstrip())
    if not size:
      break
    for pos in range(1, size, 4):
      if line[pos].isupper():
        stacks[pos // 4].append(line[pos])
  return stacks

def iter_moves():
  for line in sys.stdin:
    moves = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    yield tuple(int(x) for x in moves.groups())

def first_process_moves(stacks):
  for size, move_from, move_to in iter_moves():
    for _ in range(size):
      crate = stacks[move_from - 1].pop(0)
      stacks[move_to - 1].insert(0, crate)
  solution = "".join(stack[0] for stack in stacks if stack)
  print(solution)

def second_process_moves(stacks):
  for size, move_from, move_to in iter_moves():
    crates = []
    for _ in range(size):
      crates.append(stacks[move_from - 1].pop(0))
    for crate in reversed(crates):
      stacks[move_to - 1].insert(0, crate)
  solution = "".join(stack[0] for stack in stacks if stack)
  print(solution)

stacks = read_stacks()
second_process_moves(stacks)
