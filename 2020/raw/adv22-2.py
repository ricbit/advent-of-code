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

def score(winner):
  cards = zip(reversed(winner), range(1, 1 + len(winner)))
  return sum(a * b for a, b in cards)

def part1(data):
  p1, p2 = data
  player1_cards = deque(p1)
  player2_cards = deque(p2)
  while player1_cards and player2_cards:
    c1 = player1_cards.popleft()
    c2 = player2_cards.popleft()
    if c1 > c2:
      player1_cards.append(c1)
      player1_cards.append(c2)
    else:
      player2_cards.append(c2)
      player2_cards.append(c1)
  if player1_cards:
    return score(player1_cards)
  return score(player2_cards)

def part2(data):
  p1, p2 = data
  player1_cards = deque(p1)
  player2_cards = deque(p2)
  visited = set()
  while player1_cards and player2_cards:
    state = (tuple(player1_cards), tuple(player2_cards))
    #print(state)
    if state in visited:
      return True, score(player1_cards)
    visited.add(state)
    c1 = player1_cards.popleft()
    c2 = player2_cards.popleft()
    if c1 <= len(player1_cards) and c2 <= len(player2_cards):
      p1won, winnerscore = part2((tuple(player1_cards)[:c1], tuple(player2_cards)[:c2]))
      if p1won:
        player1_cards.extend([c1, c2])
      else:
        player2_cards.extend([c2, c1])
      continue
    if c1 > c2:
      player1_cards.append(c1)
      player1_cards.append(c2)
    else:
      player2_cards.append(c2)
      player2_cards.append(c1)
  if player1_cards:
    return True, score(player1_cards)
  else:
    return False, score(player2_cards)

data = aoc.line_blocks()
data = [aoc.ints(x[1:]) for x in data]
aoc.cprint(part1(data))
aoc.cprint(part2(data)[1])
