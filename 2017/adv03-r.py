import sys
import aoc

def sum_neigh(m, j, i):
  return sum(m[(jj, ii)] for jj, ii in aoc.iter_neigh8(j, i))

def part1(goal):
  for j, i, value in aoc.spiral():
    if value == goal:
      return abs(j) + abs(i)

def part2(goal):
  for j, i, value in aoc.spiral(lambda m, j, i, cur: sum_neigh(m, j, i)):
    if value > goal:
      return value

goal = int(sys.stdin.read())
aoc.cprint(part1(goal))
aoc.cprint(part2(goal))
