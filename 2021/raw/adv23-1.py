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

# 0123456789012
# #############
# #...........#
# ###A#D#B#D###
#   #B#C#A#C#
#   #########

skip = [3, 5, 7, 9]

def build_base_graph():
  g = nx.Graph()
  for i in range(1, 11):
    if i not in skip:
      j = i + 1
      if j in skip:
        j += 1
      g.add_edge((1, i), (1, j), steps=j - i)
  for i in skip:
    g.add_edge((2, i), (1, i - 1), steps=2)
    g.add_edge((2, i), (1, i + 1), steps=2)
    g.add_edge((2, i), (3, i), steps=1)
  nx.nx_agraph.write_dot(g, "p23.dot")
  return g

def get_frog_pos(state):
  frog_pos = aoc.ddict(list)
  for j, i in state.iter_all():
    if state[j][i] in "ABCD":
      frog_pos[state[j][i]].append((j, i))
  return frog_pos

def get_valid_moves(g, state, frog_pos):
  proper_nest = lambda x: x[1] == skip[ord(frog) - ord("A")]
  for frog, mpos in frog_pos.items():
    for pos in mpos:
      #print(f"frog {frog} at pos {pos} ")
      newg = g.copy()
      for obstacle in aoc.flatten(frog_pos.values()):
        if obstacle != pos:
          newg.remove_node(obstacle)
      #print(list(newg.nodes))
      #print(list(newg.edges))
      for dst, size in nx.shortest_path_length(newg, source=pos, weight="steps").items():
        # Can't walk on its own nest.
        if dst[0] > 1 and pos[0] > 1 and dst[1] == pos[1]:
          continue
        # Can't walk on the corridor
        if pos[0] == 1 and dst[0] == 1:
          continue
        # Can't enter in another frog's nest.
        if dst[0] > 1 and not proper_nest(dst):
          continue
        # Can't walk from the right place
        if pos[0] > 1 and dst[0] > 1 and proper_nest(pos) and proper_nest(dst):
          continue
        # Must enter the nest all the way
        if dst[0] == 2 and proper_nest(dst) and state[3][dst[1]] == ".":
          continue
        # Must walk
        if dst == pos:
          continue
        yield (frog, pos, dst, size) 
  return []

def encode_state(state):
  return "".join("".join(line) for line in state.table)

def decode_state(encoded):
  return aoc.Table([list(encoded[13 * i: 13 * i + 13]) for i in range(5)])

def print_state(state):
  for line in state.table:
    print("".join(line))
  print()

def heuristic(state):
  h = 0
  for frog, pos in get_frog_pos(state).items():
    for j, i in pos: 
      if j <= 1 or (i != skip[ord(state[j][i]) - ord("A")]):
        factor = abs(i - skip[ord(state[j][i]) - ord("A")])
        if (i != skip[ord(state[j][i]) - ord("A")]):
          factor += 1 + (2 - j)
        factor *= 10 ** (ord(frog) - ord('A'))
        h += factor
  return h

def solve(start):
  pnext = [(heuristic(start), 0, encode_state(start))]
  g = build_base_graph()
  visited = set()
  estimate = {}
  count = 0
  while pnext:
    heur, score, state = heapq.heappop(pnext)
    if state in visited:
      continue
    visited.add(state)
    state = decode_state(state)
    if heuristic(state) == 0:
      return score
    frog_pos = get_frog_pos(state)
    for frog, src, dst, steps in get_valid_moves(g, state, frog_pos):
      nstate = state.copy()
      nstate[src[0]][src[1]] = "."
      nstate[dst[0]][dst[1]] = frog
      factor = 10 ** (ord(frog) - ord('A'))
      tstate = encode_state(nstate)
      if tstate not in visited:
        newscore = score + steps * factor
        h = newscore + heuristic(nstate)
        if h < estimate.get(tstate, 10e6):
          count += 1
          if count % 1000 == 0:
            print(f"from score {score} heur {heur}, src {src}, dst {dst} ")
            #print_state(state)
            #print(f"to score {score} heur {heur}")
            #print_state(nstate)
            #print("--- \n")
          heapq.heappush(pnext, (h, newscore, tstate))
          estimate[tstate] = h
  return data

data = [list((line + " " * 8)[:13]) for line in sys.stdin.read().splitlines()]
data = aoc.Table(data)
aoc.cprint(solve(data))
