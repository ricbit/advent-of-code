import sys
import aoc
import heapq
import networkx as nx
import functools
from pyinstrument import Profiler
from collections import deque

# 0123456789012
# #############
# #...........#
# ###A#D#B#D###
#   #B#C#A#C#
#   #########

skip = [3, 5, 7, 9]

def build_base_graph(part1):
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
    if not part1:
      g.add_edge((3, i), (4, i), steps=1)
      g.add_edge((4, i), (5, i), steps=1)
  ordered_nodes = tuple(g.nodes)
  return g, ordered_nodes

def get_frog_pos(zstate, ordered_nodes):
  frog_pos = aoc.ddict(list)
  for node, (j, i) in zip(zstate, ordered_nodes):
    if node != ".":
      frog_pos[node].append((j, i))
  return frog_pos

def empty_below(frog, dst, zstate, ordered_nests):
  nest = ord(frog) - ord("A")
  if dst[1] != skip[nest]:
    return False
  nestsize = 2 if len(zstate) < 20 else 4
  for i in range(nest * nestsize + dst[0] - 2 + 1, nest * nestsize + nestsize):
    _, _, n = ordered_nests[i]
    if zstate[n] != frog:
      return True
  return False

@functools.cache
def get_paths(zg, pos, ordered_nodes, zstate):
  visited = [False] * len(zstate)
  pnext = deque([(0, ordered_nodes.index(pos))])
  ans = []
  while pnext:
    dist, pos = pnext.popleft()
    if visited[pos]:
      continue
    visited[pos] = True
    ans.append((ordered_nodes[pos], dist))
    for neigh, steps in zg[pos]:
      if zstate[neigh] == ".":
        pnext.append((dist + steps, neigh))
  return ans

def get_valid_moves(g, zg, frog_pos, zstate, ordered_nests, ordered_nodes, mask):
  for frog, mpos in frog_pos.items():
    for pos in mpos:
      paths = get_paths(zg, pos, ordered_nodes, mask)
      for dst, size in paths:
        # Can't walk inside a nest.
        if dst[0] > 1 and pos[0] > 1 and dst[1] == pos[1]:
          continue
        # Can't walk on the corridor
        if pos[0] == 1 and dst[0] == 1:
          continue
        # Can't enter another frog's nest.
        if dst[0] > 1 and dst[1] != skip[ord(frog) - ord("A")]:
          continue
        # Must enter the nest all the way
        if empty_below(frog, dst, zstate, ordered_nests):
          continue
        # Must walk
        if dst == pos:
          continue
        yield (frog, pos, dst, size)

def encode_state(state, ordered_nodes):
  return "".join(state[j][i] for j, i in ordered_nodes)

def decode_state(encoded, part1, ordered_nodes):
  limit = 5 if part1 else 7
  table = [["."] * 13 for _ in range(limit)]
  for value, (j, i) in zip(encoded, ordered_nodes):
    table[j][i] = value
  return aoc.Table(table)

def print_state(state):
  for line in state.table:
    print("".join(line))
  print()

@functools.cache
def compute_partial_heuristic(frog, j, i):
  if frog == ".":
    return 0
  nest = skip[ord(frog) - ord("A")]
  factor = 10 ** (ord(frog) - ord('A'))
  h = abs(i - nest) * factor
  if i != nest:
    h += (j - 1) * factor
  return h

def heuristic(zstate, ordered_nodes, ordered_nests):
  h = 0
  for frog, (j, i) in zip(zstate, ordered_nodes):
    h += compute_partial_heuristic(frog, j, i)
  for frog, zscore, zpos in ordered_nests:
    if zstate[zpos] != frog:
      h += zscore
  return h

def update_state(score, heur, src, dst, count, pnext, zstate, tstate, part1, ordered_nodes):
  state = decode_state(zstate, part1, ordered_nodes)
  nstate = decode_state(tstate, part1, ordered_nodes)
  print(f"from score {score} heur {heur}, src {src}, dst {dst} "
        f"iter {count} size {len(pnext)}")
  print_state(state)
  print(f"to score {score} heur {heur}")
  print_state(nstate)
  print("--- \n")

def get_ordered_nests(ordered_nodes, state):
  height = state.h
  ordered_nests = []
  for frog, s in zip("ABCD", skip):
    factor = 10 ** (ord(frog) - ord('A'))
    for j in range(2, height - 1):
      ordered_nests.append((frog, (j - 1) * factor, ordered_nodes.index((j, s))))
  return ordered_nests 

def build_zgraph(g, ordered_nodes):
  zgraph = [[] for _ in range(len(ordered_nodes))]
  for src, dst, steps in g.edges.data("steps"):
    src = ordered_nodes.index(src)
    dst = ordered_nodes.index(dst)
    zgraph[dst].append((src, steps))
    zgraph[src].append((dst, steps))
  return tuple(tuple(line) for line in zgraph)

def solve(start, part1=True):
  g, ordered_nodes = build_base_graph(part1)
  ordered_nests = get_ordered_nests(ordered_nodes, start)
  reversed_nodes = {v:i for i, v in enumerate(ordered_nodes)}
  zstart = encode_state(start, ordered_nodes)
  pnext = [(heuristic(zstart, ordered_nodes, ordered_nests), 0, zstart)]
  zg = build_zgraph(g, ordered_nodes)
  visited = set()
  count = 0
  while pnext:
    heur, score, zstate = heapq.heappop(pnext)
    if zstate in visited:
      continue
    visited.add(zstate)
    if heuristic(zstate, ordered_nodes, ordered_nests) == 0:
      return score
    frog_pos = get_frog_pos(zstate, ordered_nodes)
    mask = "".join("." if c == "." else "X" for c in zstate)
    valid_moves = get_valid_moves(
      g, zg, frog_pos, zstate, ordered_nests, ordered_nodes, mask)
    for frog, src, dst, steps in valid_moves:
      tstate = list(zstate)
      tstate[reversed_nodes[src]] = "."
      tstate[reversed_nodes[dst]] = frog
      tstate = "".join(tstate)
      if tstate not in visited:
        factor = 10 ** (ord(frog) - ord('A'))
        newscore = score + steps * factor
        h = newscore + heuristic(tstate, ordered_nodes, ordered_nests)
        count += 1
        if count % 1000 == 0:
          pass
          #update_state(score, heur, src, dst, count, pnext, zstate, tstate, part1, ordered_nodes)
        heapq.heappush(pnext, (h, newscore, tstate))
  return data

#if True:
with Profiler(interval=0.01) as profiler:
  data = [list((line + " " * 8)[:13]) for line in sys.stdin.read().splitlines()]
  table = aoc.Table(data)
  aoc.cprint(solve(table, part1=True))
  data.insert(-2, list("  #D#C#B#A#  "))
  data.insert(-2, list("  #D#B#A#C#  "))
  table = aoc.Table(data)
  aoc.cprint(solve(table, part1=False))

profiler.print()
#main()
