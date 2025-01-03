import itertools
import aoc
import sys

def nextpwd(pwd):
  p = list(pwd)
  for j in range(len(p) - 1, -1, -1):
    if p[j] != "z":
      p[j] = chr(ord(p[j]) + 1)
      return "".join(p)
    p[j] = "a"
  return None

def triad(pwd, i):
  return pwd[i + 2] == chr(ord(pwd[i + 1]) + 1) == chr(ord(pwd[i]) + 2)

def valid(pwd):
  if any(c in pwd for c in "iol"):
    return False
  if not any(triad(pwd, i) for i in range(len(pwd) - 3)):
    return False
  dups = set()
  for k, v in itertools.groupby(pwd):
    if len(list(v)) >= 2:
      dups.add(k)
  return len(dups) >= 2

def nextvalid(pwd):
  pwd = nextpwd(pwd)
  while not valid(pwd):
    pwd = nextpwd(pwd)
  return pwd

pwd = sys.stdin.read().strip()
pwd = nextvalid(pwd)
aoc.cprint(pwd)
pwd = nextvalid(pwd)
aoc.cprint(pwd)
