import sys

def has_vowel(word):
  return len([c for c in word if c in "aeiou"]) >= 3

def has_repeat(word):
  return any(a == b for a, b in zip(word, word[1:]))

def no_forbidden(word):
  return all(x not in word for x in ["ab", "cd", "pq", "xy"])

ans = 0
for w in sys.stdin:
  if has_vowel(w) and has_repeat(w) and no_forbidden(w):
    ans += 1
print(ans)
