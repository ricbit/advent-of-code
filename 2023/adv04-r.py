import sys

points = 0
lines = sys.stdin.readlines()
card_copies = [1] * len(lines)
for pos, line in enumerate(lines):
  winning_cards, hand = [set(x.split()) for x in line.split(":")[1].split("|")]
  common_cards = len(winning_cards.intersection(hand))
  for i in range(min(common_cards, len(lines) - pos - 1)):
    card_copies[pos + i + 1] += card_copies[pos]
  points += 2 ** (common_cards - 1) if common_cards > 0 else 0

print(points)
print(sum(card_copies))
    
  
