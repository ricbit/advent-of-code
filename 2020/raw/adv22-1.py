import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(data):
  p1, p2 = data
  player1_cards = deque(aoc.ints(p1[1:]))
  player2_cards = deque(aoc.ints(p2[1:]))
  while player1_cards and player2_cards:
    c1 = player1_cards.popleft()
    c2 = player2_cards.popleft()
    if c1 > c2:
      player1_cards.append(c1)
      player1_cards.append(c2)
    else:
      player2_cards.append(c2)
      player2_cards.append(c1)
  print(player1_cards)
  print(player2_cards)
  if player1_cards:
    winner = player1_cards
  else:
    winner = player2_cards
  total = sum(a * b for a, b in zip(reversed(winner), range(1, 1 + len(winner))))
  return total

data = aoc.line_blocks()
aoc.cprint(solve(data))
# 1857 too low
# 306 too low
