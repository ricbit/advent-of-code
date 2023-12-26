import sys
import itertools
import aoc

def scroll(table):
  for i in range(table.w):
    base = 0
    while base < table.h:
      if table[base][i] == ".":
        for k in range(base + 1, table.h):
          if table[k][i] == "#":
            base = k
            break
          if table[k][i] == "O":
            table[k][i], table[base][i] = table[base][i], table[k][i]
            base += 1
      base += 1
  return table

def score(table):
  return sum(r.count("O") * (table.h - j) for j, r in enumerate(table.table))

def turn(table):
  for i in range(4):
    scroll(table)
    table = table.clock90()
  return table

def table_hash(table):
  return "".join("".join(row) for row in table.table)

def search(table, n):
  visited, scores = {}, []
  for pos in itertools.count():
    scores.append(score(table))
    if (h := table_hash(table)) not in visited:
      visited[h] = pos
      table = turn(table)
    else:
      period = pos - visited[h]
      return scores[(n - visited[h]) % period + visited[h]]

table = aoc.Table.read()
print(score(scroll(table.copy())))
print(search(table, 10 ** 9))
