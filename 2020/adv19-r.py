import aoc
import functools
import multiprocessing

def parse(rules):
  grammar = {}
  for line in rules:
    key, values = line.split(":")
    key = int(key)
    if '"' not in values:
      grammar[key] = tuple(
          tuple(aoc.ints(value.strip().split())) for value in values.split("|"))
    else:
      grammar[key] = values.strip()[1]
  return grammar

@functools.cache
def match_sequence(seq, message, part):
  if len(seq) == 1:
    return match_node(seq[0], message, part)
  for m in range(mintable[seq[0]], len(message) - sum(mintable[n] for n in seq[1:]) + 1):
    if match_node(seq[0], message[:m], part) and match_sequence(seq[1:], message[m:], part):
      return True
  return False

@functools.cache
def match_node(src, message, part):
  if isinstance(src, str):
    return message == src
  for dst in grammar[src]:
    if match_sequence(dst, message, part):
      return True
  return False

@functools.cache
def findmin(rule):
  ans = 1e10
  for dst in grammar[rule]:
    if isinstance(dst[0], str):
      mintable[rule] = 1
      return 1
    ans = min(ans, sum(findmin(d) for d in dst))
  mintable[rule] = ans
  return ans

def check(messages, part):
  with multiprocessing.Pool() as pool:
    ans = sum(pool.starmap(match_node, ((0, msg, part) for msg in messages)))
  return ans

rules, messages = aoc.line_blocks()
grammar = parse(rules)
mintable = aoc.ddict(lambda: None)
findmin(0)
messages = [m.strip() for m in messages]
aoc.cprint(check(messages, False))
grammar[8] = ((42,), (42, 8))
grammar[11] = ((42, 31), (42, 11, 31))
aoc.cprint(check(messages, True))
