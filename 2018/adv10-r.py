import aoc
import numpy as np

def draw(positions, ymin, ymax, xmin, xmax):
  message = []
  fastpoints = set(tuple(x) for x in positions)
  for y in range(ymin, ymax + 1):
    line = []
    for x in range(xmin, xmax + 1):
      line.append("#" if (y, x) in fastpoints else ".")
    message.append("".join(line))
  return message

def solve(points):
  positions = np.array([[q.px, q.py] for q in points])
  velocities = np.array([[q.vx, q.vy] for q in points])
  lastarea, ans = 1e15, (0, [])
  for time in range(100000):
    ymax = np.amax(positions[:, 0])
    ymin = np.amin(positions[:, 0])
    xmax = np.amax(positions[:, 1])
    xmin = np.amin(positions[:, 1])
    area = (ymax - ymin) * (xmax - xmin)
    if area > lastarea:
      for line in ans[1]:
        print(line)
      return ans[0]
    lastarea = area
    if area < 100 ** 2:
      ans = (time, draw(positions, ymin, ymax, xmin, xmax))
    positions += velocities
  return None

points = aoc.retuple_read(
    "py_ px_ vy_ vx_",
    r".*?<(.*?), (.*)?>.*?<(.*?), (.*?)>")
aoc.cprint(solve(points))
