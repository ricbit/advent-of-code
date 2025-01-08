import aoc

def run_opcode(code, p1, p2, p3, state):
  match code, p1, p2, p3:
    case 0, a, b, c:
      # addr
      state[c] = state[a] + state[b]
    case 1, a, b, c:
      # addi
      state[c] = state[a] + b
    case 2, a, b, c:
      # mulr
      state[c] = state[a] * state[b]
    case 3, a, b, c:
      # muli
      state[c] = state[a] * b
    case 4, a, b, c:
      # banr
      state[c] = state[a] & state[b]
    case 5, a, b, c:
      # bani
      state[c] = state[a] & b
    case 6, a, b, c:
      # borr
      state[c] = state[a] | state[b]
    case 7, a, b, c:
      # bori
      state[c] = state[a] | b
    case 8, a, b, c:
      # setr
      state[c] = state[a]
    case 9, a, b, c:
      # seti
      state[c] = a
    case 10, a, b, c:
      # gtir
      state[c] = 1 if a > state[b] else 0
    case 11, a, b, c:
      # gtri
      state[c] = 1 if state[a] > b else 0
    case 12, a, b, c:
      # gtrr
      state[c] = 1 if state[a] > state[b] else 0
    case 13, a, b, c:
      # eqir
      state[c] = 1 if a == state[b] else 0
    case 14, a, b, c:
      # eqri
      state[c] = 1 if state[a] == b else 0
    case 15, a, b, c:
      # eqrr
      state[c] = 1 if state[a] == state[b] else 0

def run_real(code, translation):
  state = [0] * 4
  for op, p1, p2, p3 in code:
    run_opcode(translation[op], p1, p2, p3, state)
  return state[0]

def parse_opcode(block):
  before = eval(block[0].split(" ", 1)[1])
  opcode = aoc.ints(block[1].split())
  after = eval(block[2].split(" ", 1)[1])
  return before, opcode, after

def find_opmap(blocks):
  suspect = 0
  opmap = set()
  for block in blocks:
    before, opcode, after = parse_opcode(block)
    valid = set()
    for code in range(16):
      state = before[:]
      run_opcode(code, opcode[1], opcode[2], opcode[3], state)
      if state == after:
        valid.add(code)
    if len(valid) >= 3:
      suspect += 1
    opmap.add((opcode[0], tuple(sorted(valid))))
  return opmap, suspect

def find_translation(opmap):
  guess = [(op, list(candidates)) for op, candidates in opmap]
  rules = {}
  while any(len(candidate) > 1 for _, candidate in guess):
    for op, candidate in guess:
      if len(candidate) == 1:
        rules[op] = candidate[0]
        for xop, xcandidate in guess:
          if xop != op and candidate[0] in xcandidate:
            xcandidate.remove(candidate[0])
  return {op:candidate[0] for op, candidate in guess}

blocks = aoc.line_blocks()
opmap, suspect = find_opmap(blocks[:-2])
aoc.cprint(suspect)
translation = find_translation(opmap)
code = [aoc.ints(line.split()) for line in blocks[-1]]
aoc.cprint(run_real(code, translation))
