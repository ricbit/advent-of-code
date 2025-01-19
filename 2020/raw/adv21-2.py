import aoc

def solve(lines):
  foods = [(line.ingredients.split(), line.allergens.split(", "))
           for line in lines]
  all_ingredients = set.union(*(set(f[1]) for f in foods))
  all_possible = set()
  all_allergens = []
  for ingredient in all_ingredients:
    possible = []
    for food in foods:
      if ingredient in food[1]:
        possible.append(set(food[0]))
    possible = set.intersection(*possible)
    all_allergens.append((ingredient, possible))
    all_possible.update(possible)
  safe = 0
  for food in foods:
    for ingredient in food[0]:
      if ingredient not in all_possible:
        safe += 1
  names = []
  while all_allergens:
    all_allergens.sort(key=lambda x:len(x[1]))
    allergen, name = all_allergens.pop(0)
    name = aoc.first(name)
    names.append((allergen, name))
    for ingredient, possible in all_allergens:
      possible.discard(name)
  names.sort()
  return safe, ",".join(name[1] for name in names)

lines = aoc.retuple_read(
    "ingredients allergens", r"(.*) \(contains (.*)\)")
safe, names = solve(lines)
aoc.cprint(safe)
aoc.cprint(names)
