import aoc

class Order:
  def __init__(self, tickets, rules, my_ticket):
    self.tickets = tickets
    self.rules = rules
    self.my_ticket = my_ticket
    self.candidates = self.presolve()

  def presolve(self):
    candidates = []
    for x in range(len(self.rules)):
      candidate = []
      for rule_index, r in enumerate(self.rules):
        r = self.rules[rule_index]
        if all(r.a <= ticket[x] <= r.b or r.c <= ticket[x] <= r.d
               for ticket in self.tickets):
          candidate.append(rule_index)
      candidates.append((x, candidate))
    candidates.sort(key=lambda x: len(x[1]))
    return candidates

  def solve(self):
    used, ans = set(), 1
    departure = set(index for index, rule in enumerate(self.rules)
                    if rule.name.startswith("departure"))
    for index, cand in self.candidates:
      c = set(cand).difference(used)
      if aoc.first(c) in departure:
        ans *= self.my_ticket[index]
      used.update(c)
    return ans

def solve(data):
  rules_lines, my_ticket, nearby_tickets = data
  rules = []
  for rule in rules_lines:
    r = aoc.retuple("name a_ b_ c_ d_",
                    r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", rule)
    rules.append(r)
  my_ticket = aoc.ints(my_ticket[1].split(","))
  ans = 0
  valid = []
  for ticket in nearby_tickets[1:]:
    ticket = aoc.ints(ticket.split(","))
    good = True
    for field in ticket:
      if not any(r.a <= field <= r.b or r.c <= field <= r.d for r in rules):
        good = False
        ans += field
    if good:
      valid.append(ticket)
  order = Order(valid, rules, my_ticket)
  order.presolve()
  return ans, order.solve()

data = aoc.line_blocks()
part1, part2 = solve(data)
aoc.cprint(part1)
aoc.cprint(part2)
