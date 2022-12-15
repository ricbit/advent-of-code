import string
import sys

def priority(letter):
  if letter.isupper():
    return ord(letter) - ord('A') + 27
  else:
    return ord(letter) - ord('a') + 1

def first():
  priorities = 0
  for line in sys.stdin:
    sack = list(line.strip())
    size = len(sack) // 2
    common = set(sack[0:size]).intersection(set(sack[size:]))
    priorities += sum(priority(letter) for letter in common)
  print(priorities)

def second():
  sacks = [line.strip() for line in sys.stdin]
  size = len(sacks) // 3
  priorities = 0
  for index in range(size):
    a, b, c = [set(list(sacks[3 * index + i])) for i in range(3)]
    badge = a.intersection(b).intersection(c)
    priorities += sum(priority(letter) for letter in badge)
  print(priorities)

second()
