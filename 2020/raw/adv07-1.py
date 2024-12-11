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

def count_colors(graph):
  visited = set()
  pnext = ["shiny gold"]
  while pnext:
    name = pnext.pop(0)
    if name in visited:
      continue
    visited.add(name)
    for dst in graph[name]:
      pnext.append(dst)
  return len(visited) - 1

def solve(data):
  graph = aoc.ddict(list)
  for line in data:
    if line.dst.startswith("no other"):
      graph[line.src] = []
      continue
    for bag in line.dst.replace("bags", "bag").replace(".", "").split(", "):
      print(bag)
      bag = aoc.retuple("size_ name", r"(\d+) (.*) bag", bag)
      graph[line.src].append(bag.name)
  return count_colors(aoc.invert(graph))

data = aoc.retuple_read("src dst", r"(.*) bags contain (.*)\.")
aoc.cprint(solve(data))
