import sys
import re
import itertools
import math
import aoc
import random
from collections import *
import copy
from multiprocessing import Pool

verts = defaultdict(lambda: [])
edges = []
for line in sys.stdin:
  a, links = line.strip().split(":")
  for b in links.split():
    edges.append(((a, b), (a, b)))
    verts[a].append(len(edges) - 1)
    verts[b].append(len(edges) - 1)

def contract(original_verts, original_edges):
  verts = copy.deepcopy(original_verts)
  edges = copy.deepcopy(original_edges)
  while len(edges) > 2:
    idx = random.randrange(0, len(edges))
    (a, b), name = edges[idx]


print(verts)
print(edges)


#print(len(graph),a,b)
#print(a*b)
