import sys
import aoc

def hamming(a, b):
  return sum(int(aa != bb) for aa, bb in zip(a, b))

def vcomp(table, a, b):
  if 0 <= a < table.h and 0 <= b < table.h:
    return hamming(table.table[a], table.table[b])
  return 0

def hcomp(table, a, b):
  extract = lambda x : [table[j][x] for j in range(table.h)]
  if 0 <= a < table.w and 0 <= b < table.w:
    return hamming(extract(a), extract(b))
  return 0

def find_mirror(table, size, func, distance):
  for i in range(1, size):
    if sum(func(table, i + j, i - j - 1) for j in range(i)) == distance:
      return i
  return 0

def sum_mirrors(tables, distance):
  ans = 0
  for raw_table in tables:
    table = aoc.Table(raw_table)
    ans += 100 * find_mirror(table, table.h, vcomp, distance)
    ans += find_mirror(table, table.w, hcomp, distance)
  return ans

tables = aoc.line_blocks()
print(sum_mirrors(tables, 0))
print(sum_mirrors(tables, 1))
