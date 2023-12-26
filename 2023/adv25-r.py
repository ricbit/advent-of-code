import sys
import random
from collections import *
import itertools
from multiprocessing import Pool

def read_graph():
  verts = defaultdict(lambda: set())
  names = {}
  current = 0
  for line in sys.stdin:
    a, links = line.strip().split(":")
    for b in links.split():
      if a not in names:
        names[a] = current
        current += 1
      if b not in names:
        names[b] = current
        current += 1
      verts[names[a]].add(names[b])
      verts[names[b]].add(names[a])
  return verts

def random_bfs(verts, used):
  vnext = deque()
  keys = list(verts.keys())
  source = random.choice(keys)
  sink = random.choice(keys)
  vnext.append(source)
  visited = [False] * len(verts)
  while vnext:
    node = vnext.popleft()
    if node == sink:
      return
    if visited[node]:
      continue
    visited[node] = True
    for neigh in verts[node]:
      if not visited[neigh]:
        vnext.append(neigh)
        a, b = sorted([node, neigh])
        used[(a, b)] += 1

def floodfill(verts, edges):
  vnext = deque()
  keys = list(verts.keys())
  source = random.choice(keys)
  vnext.append(source)
  visited = set()
  while vnext:
    node = vnext.popleft()
    if node in visited:
      continue
    visited.add(node)
    for neigh in verts[node]:
      if neigh not in visited:
        a, b = sorted([node, neigh])
        if (a, b) not in edges:
          vnext.append(neigh)
          visited.add(node)
  return len(visited)

def extract_edges(used):
  edges = list(used.items())
  edges.sort(key=lambda x: x[1], reverse=True)
  verts = set()
  ans = []
  for (a, b), v in edges:
    if a not in verts and b not in verts:
      ans.append((a, b))
      if len(ans) == 6:
        return ans

def search(_):
  used = Counter()
  for i in range(100):
    random_bfs(verts, used)
  edges = extract_edges(used)
  ans = [0]
  for subset in itertools.combinations(edges, 3):
    size = floodfill(verts, edges) 
    compl = len(verts) - size
    if size > len(verts) / 3 and compl > len(verts) / 3:
      ans.append(size * compl)
  return max(ans)

verts = read_graph()
with Pool() as p:
  print(max(p.imap_unordered(search, (i for i in range(20)))))
