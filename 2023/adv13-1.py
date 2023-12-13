import sys
import re
import itertools
import math
from aoc import Table

def vcomp(table, a, b):
  if 0 <= a < table.h and 0 <= b < table.h:
    return table.table[a] == table.table[b]
  return True

def hcomp(table, a, b):
  if 0 <= a < table.w and 0 <= b < table.w:
    return all(table[j][a] == table[j][b] for j in range(table.h))
  return True

def find_vertical(table):
  for i in range(1, table.h):
    if all(vcomp(table, i + j, i - j - 1) for j in range(i)):
      return i
  return None

def find_horiz(table):
  for i in range(1, table.w):
    if all(hcomp(table, i + j, i - j - 1) for j in range(i)):
      return i
  return None

tables = sys.stdin.read().split("\n\n")
ans = 0
for raw_table in tables:
  table = Table(raw_table.strip().split("\n"))
  v = find_vertical(table)
  if v:
    ans += v * 100
  h = find_horiz(table)
  if h:
    ans += h
print(ans)
