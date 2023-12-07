import sys
import re
import itertools
import math

first_order = "AKQJT98765432"
second_order = "AKQT98765432J"

def rank(hand, order):
  card_values = sorted(hand, key=lambda x: order.index(x))
  counts = [(k, len(list(g))) for k, g in itertools.groupby(card_values)]
  counts.sort(key=lambda x: x[1], reverse=True)
  match (len(counts), counts[0][1]):
    case (1, _):
      return 0
    case (2, 4):
      return 1
    case (2, 3):
      return 2
    case (3, 3):
      return 3
    case (3, 2):
      return 4
    case (4, 2):
      return 5
    case _:
      return 6

def first_score(hand, order):
  return (rank(hand, order) , [order.index(i) for i in hand])

def second_score(hand, order):
  all_ranks = [rank(hand.replace("J", c), order) for c in order]
  return (min(all_ranks), [order.index(i) for i in hand])

def winnings(hands, score, order):
  scored_hands = [(score(h[0], order), h[0], int(h[1])) for h in hands]
  scored_hands.sort(reverse=True)
  return sum((i + 1) * hand[2] for i, hand in enumerate(scored_hands))

hands = [line.strip().split() for line in sys.stdin]
print(winnings(hands, first_score, first_order))
print(winnings(hands, second_score, second_order))
  
