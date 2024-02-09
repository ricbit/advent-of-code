import sys
import itertools
import aoc

def extract_lines(original_block):
  block = [aoc.ints(line.split()) for line in original_block]
  for line in block:
    yield set(line)
  for line in zip(*block):
    yield set(line)

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

def sort_winners(blocks):
  used = [False] * len(blocks)
  for i, score in search(blocks, numbers):
    if not used[i]:
      used[i] = True
      yield score

blocks = aoc.line_blocks()
numbers = aoc.ints(blocks[0][0].split(","))
blocks = [list(extract_lines(block)) for block in blocks[1:]]
winners = list(sort_winners(blocks))
aoc.cprint(winners[0])
aoc.cprint(winners[-1])

