import itertools
import aoc
import networkx as nx

def create_graph(ops):
  g = nx.DiGraph()
  for op_b3, op in ops.items():
    g.add_edge(op_b3, op.b1)
    g.add_edge(op_b3, op.b2)
  return g

def simulate(g, nodes, ops):
  values = {}
  for node in reversed(list(nx.topological_sort(g))):
    if node in nodes:
      values[node] = nodes[node]
    else:
      op = ops[node]
      a = values[op.b1]
      b = values[op.b2]
      match op.op:
        case "AND":
          c = a & b
        case "OR":
          c = a | b
        case "XOR":
          c = a ^ b
      values[node] = c
  zs = {int(k[1:]): v for k, v in values.items() if k.startswith("z")}
  return int("".join(str(zs[k]) for k in sorted(zs.keys(), reverse=True)), 2)

def parse(data):
  bits, ops = data
  nodes = aoc.retuple_read("node bit_", r"(\w+): (\d+)", bits)
  nodes = {n.node: n.bit for n in nodes}
  ops = aoc.retuple_read("b1 op b2 b3", r"(\w+) (\w+) (\w+) -> (\w+)", ops)
  ops_dict = {}
  for op in ops:
    ops_dict[op.b3] = op
  return nodes, ops_dict

def part1(nodes, ops):
  g = create_graph(ops)
  return simulate(g, nodes, ops)

def find_error(g, a, b):
  brange = 45
  baseline = a + b
  x = list(reversed("0" * brange + bin(a)[2:]))[:brange]
  y = list(reversed("0" * brange + bin(b)[2:]))[:brange]
  for i in range(brange):
    nodes[f"x{i:02}"] = int(x[i])
    nodes[f"y{i:02}"] = int(y[i])
  try:
    z = simulate(g, nodes, ops)
  except nx.NetworkXUnfeasible:
    return None
  pos = 0
  while baseline + z > 0:
    if baseline % 2 != z % 2:
      return pos
    pos += 1
    baseline >>= 1
    z >>= 1
  return None

def swap_ops(g, ops, a, b):
  g.remove_edge(a, ops[a].b1)
  g.remove_edge(a, ops[a].b2)
  g.remove_edge(b, ops[b].b1)
  g.remove_edge(b, ops[b].b2)
  ops[a], ops[b] = ops[b], ops[a]
  g.add_edge(a, ops[a].b1)
  g.add_edge(a, ops[a].b2)
  g.add_edge(b, ops[b].b1)
  g.add_edge(b, ops[b].b2)

def build_patterns():
  all_ones = 2 ** 45 - 1
  alt01 = int("".join("01" * 24), 2)
  alt10 = int("".join("10" * 24), 2)
  patterns = [
      (0, 0),
      (all_ones, 0), (0, all_ones),
      (alt01, alt01), (alt10, alt10),
      (alt01, all_ones), (alt10, all_ones),
      (all_ones, alt01), (all_ones, alt10)]
  return patterns

def part2(ops):
  g = create_graph(ops)
  patterns = build_patterns()
  wires = set()
  for _ in range(4):
    wrong_bits = [find_error(g, a, b) for a, b in patterns]
    wrong_bit = min(bit for bit in wrong_bits if bit is not None)
    ug = g.to_undirected()
    nearby = list(nx.single_source_shortest_path_length(
        ug, f"z{wrong_bit:02}", 3))
    possible_pairs = set()
    for a, b in itertools.combinations(nearby, 2):
      if a[0] in "xy" or b[0] in "xy" or a == b:
        continue
      swap_ops(g, ops, a, b)
      new_wrong_bits = [find_error(g, a, b) for a, b in patterns]
      new_wrong_bit = [bit for bit in new_wrong_bits if bit is not None]
      if new_wrong_bit and min(new_wrong_bit) > wrong_bit:
        possible_pairs.add((a, b))
      swap_ops(g, ops, a, b)
    if len(possible_pairs) != 1:
      return "bug ", len(possible_pairs)
    sa, sb = aoc.first(possible_pairs)
    swap_ops(g, ops, sa, sb)
    wires.update([sa, sb])
  return ",".join(sorted(wires))

nodes, ops = parse(aoc.line_blocks())
aoc.cprint(part1(nodes, ops))
aoc.cprint(part2(ops))
