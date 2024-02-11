import itertools
import heapq
import re
import sys
import mip

def parse():
  desc_re = r"Each\s+(\w+)\s.*?(\d+)\s+(\w+).*?(?:(\d+)\s+(\w+).*?)?\."
  minerals = {"ore": 3, "clay": 2, "obsidian": 1, "geode": 0}
  blueprints = []
  for line in sys.stdin:
    description = re.findall(desc_re, line)
    blueprint = [[0] * 4 for _ in range(4)]
    for robot in description:
      blueprint[minerals[robot[0]]][minerals[robot[2]]] = int(robot[1])
      if robot[3]:
        blueprint[minerals[robot[0]]][minerals[robot[4]]] = int(robot[3])
    blueprints.append(blueprint)
  return blueprints

def mipsearch(blueprint, time):
  time += 1
  m = mip.Model(sense=mip.MAXIMIZE)
  m.verbose = 0
  mv = []
  for t in range(time):
    mipline = []
    for x in range(4):
      mipline.append(m.add_var(var_type=mip.INTEGER, lb=0, ub=1000,
        name="ORE-%d-%d" % (t, x)))
    for x in range(4):
      mipline.append(m.add_var(var_type=mip.INTEGER, lb=0, ub=1000,
        name="ROBOT-%d-%d" % (t, x)))
    for r in range(4):
      for x in range(4):
        mipline.append(m.add_var(var_type=mip.INTEGER, lb=0, ub=1000,
          name="PRICE-%d-ROBOT-%d-ORE-%d" % (t, r, x)))
    for x in range(4):
      mipline.append(m.add_var(var_type=mip.BINARY,
        name="BUY-%d-%d" % (t, x)))
    mv.append(mipline)
  ORE = 0
  ROBOT = 4
  PRICE = 8
  BUY = 8 + 16
  # Start with one ore robot, no ore
  for i in range(4):
    m += mv[0][ORE + i] == 0
    init = 1 if i== 3 else 0
    m += mv[0][ROBOT + i] == init
  # Can´t buy on the first round
  for i in range(4):
    m += mv[0][BUY + i] == 0
  # Buy at most one robot each round
  for t in range(time):
    m += mip.xsum(mv[t][BUY + i] for i in range(4)) <= 1
  # Each robot has a price
  for t in range(time):
    for i, robot in enumerate(blueprint):
      for j, ore in enumerate(robot):
        m += mv[t][PRICE + i * 4 + j] - ore * mv[t][BUY + i] == 0
  # Increase amount of robots
  for t in range(1, time):
    for i in range(4):
      m += mv[t][ROBOT + i] - mv[t - 1][ROBOT + i] - mv[t - 1][BUY + i] == 0
  # Produce ore and buy robots
  for t in range(1, time):
    for i in range(4):
      m += (mv[t][ORE + i] - 
        mv[t - 1][ORE + i] - mv[t - 1][ROBOT + i] +
        mip.xsum(mv[t][PRICE + r * 4 + i] for r in range(4))) == 0
  # Maximize geodes
  m.objective = mip.maximize(mv[time - 1][0])
  m.optimize()
  return m.objective_value

def first(blueprints, time):
  return sum((i + 1) * mipsearch(b, time) for i, b in enumerate(blueprints))

def second(blueprints, time):
  ans = 1
  for b in blueprints[:3]:
    ans *= mipsearch(b, time)
  return ans

blueprints = parse()
print(first(blueprints, 24))
print(second(blueprints, 32))

