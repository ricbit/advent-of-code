import sys

edges = {}
for line in sys.stdin:
  a, b = line.strip().split("-")
  edges.setdefault(a, set()).add(b)
  edges.setdefault(b, set()).add(a)

def middle(cave):
  return cave not in ("start", "end")

ans = 0
pending = set([("start", (), (), ())])
while len(pending) > 0:
  current, visited, path, double = pending.pop()
  if current == "end":
    ans += 1
    continue
  new_visited = visited
  new_path = path + (current,)
  if current[0].islower():
    if current in visited and middle(current):
      double = current
    else:
      new_visited = tuple(sorted(set(visited).union(set([current]))))
  for cave in edges[current]:
    if (cave not in new_visited) or (not double and middle(cave)):
      pending.add((cave, new_visited, new_path, double))
print(ans)
