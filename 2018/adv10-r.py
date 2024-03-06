import aoc

def solve(points):
  positions = [[q.px, q.py] for q in points]
  lastarea, ans = 1e15, (0, 0)
  for time in range(100000):
    b = aoc.bounds(positions)
    area = (b.ymax - b.ymin) * (b.xmax - b.xmin)
    if area > lastarea:
      for line in ans[1]:
        print(line)
      return ans[0]
    lastarea = area
    if area < 100 ** 2:
      message = []
      fastpoints = set(tuple(x) for x in positions)
      for y in range(b.ymin, b.ymax + 1):
        line = []
        for x in range(b.xmin, b.xmax + 1):
          line.append("#" if (y, x) in fastpoints else ".")
        message.append("".join(line))
      ans = (time, message)
    for i in range(len(points)):
      positions[i][0] += points[i].vx
      positions[i][1] += points[i].vy

points = aoc.retuple_read("py_ px_ vy_ vx_",
    r".*?<(.*?), (.*)?>.*?<(.*?), (.*?)>")
aoc.cprint(solve(points))
