import sys
import string
import re
import itertools
import math
import cmath
import aoc
import heapq
import functools
import copy
from collections import Counter, deque
from dataclasses import dataclass

def solve(dep, buses):
  wait, bus = min(((-dep) % bus, bus) for bus in buses)
  return bus * wait

departure, bus = sys.stdin.read().splitlines()
departure = int(departure)
bus = [int(i) for i in bus.split(",") if i != "x"]
aoc.cprint(solve(departure, bus))
