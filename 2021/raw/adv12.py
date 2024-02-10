import sys

edges = {}
for line in sys.stdin:
  a, b = line.strip().split("-")
  edges.setdefault(a, set()).add(b)
  edges.setdefault(b, set()).add(a)

ans = 0
pending = set([("start", (), ())])
while len(pending) > 0:
  current, visited, path = pending.pop()
  if current == "end":
    ans += 1
    continue
  new_visited = visited
  new_path = path + (current,)
  if current[0].islower():
    new_visited = tuple(sorted(set(visited).union(set([current]))))
  for cave in edges[current]:
    if cave not in new_visited:
      pending.add((cave, new_visited, new_path))
print(ans)
