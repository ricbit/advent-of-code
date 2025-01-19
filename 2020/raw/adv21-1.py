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

def solve(lines):
  foods = [(line.ingredients.split(), line.allergens.split(", ")) for line in lines]
  all_ingredients = set.union(*(set(f[1]) for f in foods))
  all_possible = set()
  for ingredient in all_ingredients:
    possible = []
    for food in foods:
      if ingredient in food[1]:
        possible.append(set(food[0]))
    possible = set.intersection(*possible)
    all_possible.update(possible)
  ans = 0
  for food in foods:
    for ingredient in food[0]:
      if ingredient not in all_possible:
        ans += 1
  return ans

lines = aoc.retuple_read("ingredients allergens", r"(.*) \(contains (.*)\)")
aoc.cprint(solve(lines))
