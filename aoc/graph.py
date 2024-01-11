import aoc
import re
import matplotlib.pyplot as plot
import numpy as np

def minutes(s):
  a, b = s.split(":")
  return int(a) * 60 + int(b)

def times():
  goal = []
  time = []
  for line in open("README.md", "rt").readlines():
    parse = re.match(r"(Goal|Time): (\d\d:\d\d) (\d\d:\d\d)\s*$", line)
    if parse:
      match parse.groups():
        case "Goal", t1, t2:
          goal.append((minutes(t1), minutes(t2)))
        case "Time", t1, t2:
          time.append((minutes(t1), minutes(t2)))
  for (a1, a2), (b1, b2) in zip(goal, time):
    yield a2, b2
    yield a1, b1

relative = []
for a, b in times():
  relative.append(b /a * 100)

xvalues = np.arange(1, len(relative) / 2 + 1, 0.5)
plot.plot(xvalues, list(reversed(relative)))
plot.axhline(y=100, color="r", linestyle="--")
plot.title("Relative times for AOC")
plot.xlabel("Problem")
plot.ylabel("Relative speed (%)")
plot.show()

