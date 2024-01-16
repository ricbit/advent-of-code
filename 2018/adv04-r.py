import sys
import re
import itertools
import aoc
from collections import Counter

lines = [line.strip() for line in sys.stdin]
lines.sort()
guards = aoc.retuple_read(
    "date time_ action", 
    r"\[(.*?) \d+:(.*?)\] (wakes up|falls|Guard #\d+)", lines)
current = 0
mins = aoc.ddict(lambda: Counter())
total = Counter()
for _, guards_by_date in itertools.groupby(guards, key=lambda q: q.date):
  sleep = {}
  for guard in guards_by_date:
    match guard.action:
      case "wakes up":
        for i in range(sleep[current], guard.time):
          mins[current][i] += 1
        total[current] += guard.time - sleep[current]
      case "falls":
        sleep[current] = guard.time
      case guard_id:
        current = int(re.search(r"#(\d+)", guard_id).group(1))
guilty = aoc.maxindex(total)
aoc.cprint(guilty * aoc.maxindex(mins[guilty]))
sleepy = max(mins.keys(), key=lambda x: max(mins[x].values()))
max_minutes = aoc.maxindex(mins[sleepy])
aoc.cprint(sleepy * max_minutes)
