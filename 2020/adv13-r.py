import sys
import aoc
from sympy.ntheory.modular import crt

def part1(dep, buses):
  wait, bus = min(((-dep) % bus, bus) for bus in buses)
  return bus * wait

def part2(buses):
  bus, times = list(zip(*buses.items()))[::-1]
  times = [-i for i in times]
  return crt(bus, times)[0]

departure, bus = sys.stdin.read().splitlines()
departure = int(departure)
bus = {i:int(b) for i, b in enumerate(bus.split(",")) if b != "x"}
aoc.cprint(part1(departure, bus.values()))
aoc.cprint(part2(bus))
