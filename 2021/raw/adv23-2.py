import sys
import copy
import heapq

base = [list((line.rstrip() + " " * 13)[:13]) for line in sys.stdin]
w, h = len(base[0]), len(base)

START = 0
MOVED = 1
STOPPED = 2

def neigh(j, i):
  yield j - 1, i
  yield j + 1, i
  yield j, i - 1
  yield j, i + 1

def get_empty(base):
  empty = copy.deepcopy(base)
  for j in range(h):
    for i in range(w):
      if empty[j][i] >= "A" and empty[j][i] <= "D":
        empty[j][i] = "."
  return empty

def parse_start(base):
  first = set()
  for j in range(h):
    for i in range(w):
      if base[j][i] >= "A" and base[j][i] <= "D":
        yield (j, i, base[j][i], START)
        first.add(base[j][i])

def price(letter, value):
  return value * (10 ** (ord(letter) - ord("A")))

def candidates(base, amphi):
  j, i, letter, moved = amphi
  state = [(j, i, 0)]
  visited = [[False] * w for i in range(h)]
  while state:
    j, i, cost = state.pop(0)
    for jj, ii in neigh(j, i):
      if base[jj][ii] == "." and not visited[jj][ii]:
        visited[jj][ii] = True
        yield (jj, ii, price(letter, cost + 1))
        state.append((jj, ii, cost + 1))

def valid(base, amphi, candidates):
  j, i, letter, moved = amphi
  for jj, ii, cost in candidates:
    if moved == STOPPED:
      continue
    if j > 1 and jj > 1:
      continue
    if jj == 1 and ii in [3, 5, 7, 9]:
      continue
    if jj == 1 and moved != START:
      continue
    if jj != 1 and moved != MOVED:
      continue
    if jj != 1:
      if ii != 3 + 2 * (ord(letter) - ord('A')):
        continue
      if jj == 2 and (base[3][ii] == "." or base[3][ii] != letter):
        continue
    yield jj, ii, cost

def fill_base(state):
  empty = get_empty(base)
  for j, i, letter, moved in state:
    empty[j][i] = letter
  return empty

def smallest_path(amphis, y, x, goal):
  ans = []
  for j, i, letter, moved in amphis:
    if goal == letter:
      if i == x and j == y:
        return 0
      else:
        if j == 1:
          cost = j - 1 + abs(i - x)
        else:
          cost = j - 1 + j - 1 + abs(i - x)
        ans.append(price(letter, cost))
        #ans.append(cost)
  return min(ans)

def distance_base(amphis):
  ans = 0
  for j, i, letter, moved in amphis:
    ii = 3 + 2 * (ord(letter) - ord("A"))
    ans += price(letter, abs(ii - i))
  return ans

def update(amphis, j, i, jj, ii, letter):
  for y, x, letter, moved in amphis:
    if y == j and x == i:
      moved += 1
      if moved > 2: 
        moved = 2
      yield (jj, ii, letter, moved)
    else:
      yield (y, x, letter, moved)

def print_state(amphis, estimate, cost):
  current_base = fill_base(amphis)
  print(amphis)
  print("\n".join("".join(line) for line in current_base))
  print("\n%d %d\n" % (estimate, cost))

def search(base):
  start_amphi = tuple(parse_start(base))
  states = [(0, 0, start_amphi)]
  visited = {start_amphi: 0}
  while states:
    estimate, cost, amphis = heapq.heappop(states)
    #cost, estimate, amphis = heapq.heappop(states)
    if amphis in visited and estimate > visited[amphis]:
      continue
    print("%d %d %d" % (estimate, cost, len(states)))
    print_state(amphis, estimate, cost)
    current_base = fill_base(amphis)
    for amphi in amphis:
      j, i, letter, moved = amphi
      for candidate in valid(current_base, amphi, candidates(current_base, amphi)):
        jj, ii, price = candidate
        new_cost = cost + price
        new_amphi = tuple(sorted(update(amphis, j, i, jj, ii, letter)))
        new_distance =  distance_base(new_amphi)
        new_estimate = new_cost + new_distance
        if new_distance == 0:
          print_state(new_amphi, new_estimate, new_cost)
          return
        new_state = (new_estimate, new_cost, new_amphi)
        #new_state = (new_cost, new_estimate, new_amphi)
        if new_amphi not in visited or visited[new_amphi] > new_estimate:
          visited[new_amphi] = new_estimate
          heapq.heappush(states, new_state)

search(base)
