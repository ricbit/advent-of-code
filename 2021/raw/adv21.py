import sys
import itertools

def deterministic_dice():
  yield from itertools.cycle(range(1, 101))

p1 = int(input().split(":")[1])
p2 = int(input().split(":")[1])

def roll(dice, pos, score):
  move = sum(itertools.islice(dice, 3))
  pos = (pos - 1 + move) % 10 + 1
  score += pos
  return pos, score

def play(p1, p2):
  dice = deterministic_dice()
  s1, s2 = 0, 0
  throws = 0
  while True:
    p1, s1 = roll(dice, p1, s1)
    throws += 3
    if s1 >= 1000:
      return s2 * throws
    p2, s2 = roll(dice, p2, s2)
    throws += 3
    if s2 >= 1000:
      return s1 * throws

print(play(p1, p2))
    
