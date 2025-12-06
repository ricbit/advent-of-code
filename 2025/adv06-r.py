import sys
import aoc
import functools

op_map = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b
}

def iter_part1(size, start, end):
  for jj in range(size - 1):
    yield [(jj, j) for j in range(start, end + 1)]

def iter_part2(size, start, end):
  for j in range(start, end + 1):
    yield [(jj, j) for jj in range(size - 1)]

def get_operator_positions(table):
  ops = []
  for i, op in enumerate(table[-1]):
    if op in "+*":
      ops.append(i)
  ops.append(len(table[0]))
  return ops

def solve(table, iter_part):
  ans = 0
  ops = get_operator_positions(table)
  for i, start in enumerate(ops[:-1]):
    ps = []
    for problem in iter_part(len(table), start, ops[i + 1] - 2):
      n = 0
      for jj, j in problem:
        if table[jj][j] == " ":
          continue
        digit = int(table[jj][j])
        n = n * 10 + digit
      ps.append(n)
    ans += functools.reduce(op_map[table[-1][start]], ps)
  return ans

data = sys.stdin.readlines()
aoc.cprint(solve(data, iter_part1))
aoc.cprint(solve(data, iter_part2))
