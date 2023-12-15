import sys
import re
import itertools
import math

codes = sys.stdin.read().strip().split(",")
print(codes)

def applyhash(code):
  ans = 0
  for c in code:
    ans = (ans + ord(c)) * 17 % 256
  return ans

ans = 0
print(applyhash("HASH"))
print(sum(applyhash(code) for code in codes))
