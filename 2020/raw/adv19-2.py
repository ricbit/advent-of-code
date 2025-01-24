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
import networkx as nx
from tqdm import tqdm

def parse(rules):
  grammar = {}
  for line in rules:
    key, values = line.split(":")
    key = int(key)
    if '"' not in values:
      grammar[key] = [aoc.ints(value.strip().split()) for value in values.split("|")]
    else:
      grammar[key] = values.strip()[1]
  return grammar

def minmax(rules):
  g = nx.DiGraph()
  for src, dsts in sorted(rules.items()):
    for dst in dsts:
      for node in dst:
        g.add_edge(src, node)
  nx.nx_agraph.write_dot(g, "p19.dot")

@functools.cache
def match_sequence(seq, message, part):
  if len(seq) == 1:
    return match_node(seq[0], message, part)
  for m in range(1, 1 + len(message)):
    if match_node(seq[0], message[:m], part) and match_sequence(seq[1:], message[m:], part):
      return True
  return False

@functools.cache
def match_node(src, message, part):
  if isinstance(src, str):
    return message == src
  for dst in grammar[src]:
    if match_sequence(tuple(dst), message, part):
      return True
  return False

def check(messages, part):
  ans = 0
  for msg in tqdm(messages):
    ans += match_node(0, msg, part)
  return ans

rules, messages = aoc.line_blocks()
grammar = parse(rules)
messages = [m.strip() for m in messages]
aoc.cprint(check(messages, False))
grammar[8] = [[42], [42, 8]]
grammar[11] = [[42, 31], [42, 11, 31]]
aoc.cprint(check(messages, True))


