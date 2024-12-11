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

def build_graph(data):
  graph = aoc.ddict(list)
  for line in data:
    if line.dst.startswith("no other"):
      graph[line.src] = []
      continue
    for bag in line.dst.replace("bags", "bag").replace(".", "").split(", "):
      bag = aoc.retuple("size_ name", r"(\d+) (.*) bag", bag)
      graph[line.src].append(bag)
  return graph

def custom_invert(graph):
  invert = aoc.ddict(list)
  for src, dst in graph.items():
    for bag in dst:
      invert[bag.name].append(src)
  return invert

def part1(graph):
  return count_colors(graph)

def dfs(graph, name):
  return 1 + sum(dfs(graph, bag.name) * bag.size for bag in graph[name])

def part2(graph):
  return dfs(graph, "shiny gold") - 1

data = aoc.retuple_read("src dst", r"(.*) bags contain (.*)\.")
graph = build_graph(data)
aoc.cprint(part1(custom_invert(graph)))
aoc.cprint(part2(graph))
