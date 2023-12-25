import sys
import re
import itertools
import math
from aoc import Table

def hamming(a, b):
  return sum((0 if aa == bb else 1) for aa, bb in zip(a, b))

def vcomp(table, a, b):
  if 0 <= a < table.h and 0 <= b < table.h:
    return hamming(table.table[a], table.table[b])
  return 0

def hcomp(table, a, b):
  if 0 <= a < table.w and 0 <= b < table.w:
    return hamming(
      [table[j][a] for j in range(table.h)],
      [table[j][b] for j in range(table.h)])
  return 0

def find_vertical(table, eqs):
  for i in range(1, table.h):
    if sum(vcomp(table, i + j, i - j - 1) for j in range(i)) == eqs:
      return i
  return None

def find_horiz(table, eqs):
  for i in range(1, table.w):
    if sum(hcomp(table, i + j, i - j - 1) for j in range(i)) == eqs:
      return i
  return None

tables = sys.stdin.read().split("\n\n")
ans = 0
for raw_table in tables:
  table = Table(raw_table.strip().split("\n"))
  v = find_vertical(table, 1)
  if v:
    ans += v * 100
  h = find_horiz(table, 1)
  if h:
    ans += h
print(ans)
