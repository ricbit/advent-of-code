import sys
import aoc
import heapq
import networkx as nx
import functools

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
  ordered_nodes = list(g.nodes)
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

def get_valid_moves(g, frog_pos, zstate, ordered_nests):
  proper_nest = lambda x: x[1] == skip[ord(frog) - ord("A")]
  for frog, mpos in frog_pos.items():
    for pos in mpos:
      newg = g.copy()
      for obstacle in aoc.flatten(frog_pos.values()):
        if obstacle != pos:
          newg.remove_node(obstacle)
      paths = nx.shortest_path_length(newg, source=pos, weight="steps").items()
      for dst, size in paths:
        # Can't walk inside a nest.
        if dst[0] > 1 and pos[0] > 1 and dst[1] == pos[1]:
          continue
        # Can't walk on the corridor
        if pos[0] == 1 and dst[0] == 1:
          continue
        # Can't enter another frog's nest.
        if dst[0] > 1 and not proper_nest(dst):
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

def heuristic(zstate, ordered_nodes, ordered_nests):
  h = 0
  for frog, pos in get_frog_pos(zstate, ordered_nodes).items():
    for src in pos:
      nest = skip[ord(frog) - ord("A")]
      factor = 10 ** (ord(frog) - ord('A'))
      h += abs(src[1] - nest) * factor
      if src[1] != nest:
        h += (src[0] - 1) * factor
  for frog, zscore, zpos in ordered_nests:
    if zstate[zpos] != frog:
      h += zscore
  return h

def update_state(score, heur, src, dst, count, pnext, state, nstate):
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

def solve(start, part1=True):
  g, ordered_nodes = build_base_graph(part1)
  ordered_nests = get_ordered_nests(ordered_nodes, start)
  print(ordered_nests)
  zstart = encode_state(start, ordered_nodes)
  pnext = [(heuristic(zstart, ordered_nodes, ordered_nests), 0, zstart)]
  print(ordered_nodes)
  visited = set()
  count = 0
  while pnext:
    heur, score, zstate = heapq.heappop(pnext)
    if zstate in visited:
      continue
    visited.add(zstate)
    state = decode_state(zstate, part1, ordered_nodes)
    if heuristic(zstate, ordered_nodes, ordered_nests) == 0:
      return score
    frog_pos = get_frog_pos(zstate, ordered_nodes)
    valid_moves = get_valid_moves(g, frog_pos, zstate, ordered_nests)
    for frog, src, dst, steps in valid_moves:
      nstate = state.copy()
      nstate[src[0]][src[1]] = "."
      nstate[dst[0]][dst[1]] = frog
      factor = 10 ** (ord(frog) - ord('A'))
      tstate = encode_state(nstate, ordered_nodes)
      if tstate not in visited:
        newscore = score + steps * factor
        h = newscore + heuristic(tstate, ordered_nodes, ordered_nests)
        count += 1
        if count % 1000 == 0:
          print(zstate, len(zstate))
          pass
          update_state(score, heur, src, dst, count, pnext, state, nstate)
        heapq.heappush(pnext, (h, newscore, tstate))
  return data

data = [list((line + " " * 8)[:13]) for line in sys.stdin.read().splitlines()]
table = aoc.Table(data)
aoc.cprint(solve(table, part1=True))
data.insert(-2, list("  #D#C#B#A#  "))
data.insert(-2, list("  #D#B#A#C#  "))
table = aoc.Table(data)
#aoc.cprint(solve(table, part1=False))
