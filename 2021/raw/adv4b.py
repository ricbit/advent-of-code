import sys
import itertools
import aoc

def grouper(iterable, n):
  args = [iter(iterable)] * n
  return itertools.zip_longest(*args)

def build(block):
  for line in block[1:]:
    yield [int(i) for i in line.strip().split()]

def extract_lines(block):
  for line in block:
    yield set(line)
  for i in range(5):
    yield set(line[i] for line in block)

def search(blocks, numbers):
  for n in range(len(numbers)):
    drawn = set(numbers[:n+1])
    for i, block in enumerate(blocks):
      for line in block:
        inter = line.intersection(drawn)
        if len(inter) == 5:
          all_numbers = set(itertools.chain(*block[:5]))
          unmarked = sum(all_numbers.difference(drawn))
          yield (i, unmarked * numbers[n])
          break

lines = sys.stdin.readlines()
numbers = [int(i) for i in lines[0].split(",")]
blocks = [list(build(block)) for block in grouper(lines[1:], 6)]
blocks = [list(extract_lines(block)) for block in blocks]

used = [False] * len(blocks)
total = len(blocks)
for i, score in search(blocks, numbers):
  if not used[i]:
    used[i] = True
    total -= 1
    if total == 0:
      print(score)

