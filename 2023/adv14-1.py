import sys
import re
import itertools
import math
import aoc

table = aoc.Table(sys.stdin)
for t in range(table.h): 
  for line in table.table:
    print(line)
  print()
  for j, i in table.iter_all(lambda x: x == "O"):
    if j > 0 and table[j - 1][i] == ".":
      table[j][i], table[j - 1][i] = table[j - 1][i], table[j][i]

ans = 0
for j, row in enumerate(table.table):
  for i,c in enumerate(row):
    if c == "O":
      ans += table.h - j
print(ans)
