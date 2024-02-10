import sys
import itertools
import aoc

SEGMENTS = """
abcefg
cf
acdeg
acdfg
bcdf
abdfg
abdefg
acf
abcdefg
abcdfg
""".strip().split()
segments = [set(seg) for seg in SEGMENTS]

instances = []
for line in sys.stdin:
  numbers, given = (x.strip().split() for x in line.split("|"))
  instances.append((numbers, given))

def mapping():
  for perm in itertools.permutations("abcdefg"):
    code = {i: p for i, p in zip("abcdefg", perm)}
    yield code

def valid(numbers, code):
  for number in numbers:
    recoded = set(code[n] for n in number)
    if recoded not in segments:
      return False
  return True

def search(numbers):
  for code in mapping():
    if valid(numbers, code):
      return code

def decode(digit, code):
  recoded = set(code[n] for n in digit)
  for i, old in enumerate(segments):
    if recoded == old:
      return i

values = 0
digits = 0
for numbers, given in instances:
  code = search(numbers)
  n = 0
  for letter in given:
    digit = decode(letter, code)
    n = n * 10 + digit
    if digit in [1, 4, 7, 8]:
      digits += 1
  values += n
aoc.cprint(digits)
aoc.cprint(values)
