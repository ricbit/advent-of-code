import sys
import itertools

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
    for block in blocks:
      for line in block:
        inter = line.intersection(drawn)
        if len(inter) == 5:
          all_numbers = set(itertools.chain(*block[:5]))
          unmarked = sum(all_numbers.difference(drawn))
          print(block, numbers[:n+1], unmarked * numbers[n])
          return

lines = sys.stdin.readlines()
numbers = [int(i) for i in lines[0].split(",")]
blocks = [list(build(block)) for block in grouper(lines[1:], 6)]
blocks = [list(extract_lines(block)) for block in blocks]
search(blocks, numbers)

