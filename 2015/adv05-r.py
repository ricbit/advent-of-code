import sys
import re
import aoc

def has_vowel(word):
  return len([c for c in word if c in "aeiou"]) >= 3

def has_repeat(word):
  return any(a == b for a, b in zip(word, word[1:]))

def no_forbidden(word):
  return all(x not in word for x in ["ab", "cd", "pq", "xy"])

def rule1(words):
  ans = 0
  for w in words:
    if has_vowel(w) and has_repeat(w) and no_forbidden(w):
      ans += 1
  return ans

def rule2(words):
  ans = 0
  for w in words:
    if re.search(r"(..).*\1", w) is not None:
      if re.search(r"(.).\1", w) is not None:
        ans += 1
  return ans

words = [line.strip() for line in sys.stdin.readlines()]
aoc.cprint(rule1(words))
aoc.cprint(rule2(words))
