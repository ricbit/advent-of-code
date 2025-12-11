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
import networkx as nx
import tqdm

class Graph:
  def __init__(self, g):
    self.g = g

  @functools.cache
  def count(self, src, cur, skip):
    if cur in skip:
      return 0
    if src == cur:
      return 1
    return sum(self.count(src, node, skip) for node in self.g[cur])

def solve(data):
  g = aoc.ddict(lambda: [])
  for line in data:
    for node in line.dst.split():
      g[node].append(line.src)
  graph = Graph(g)
  svr_fft = graph.count("svr", "fft", ("out", "dac"))
  svr_dac = graph.count("svr", "dac", ("out", "fft"))
  dac_fft = graph.count("dac", "fft", ("out"))
  fft_dac = graph.count("fft", "dac", ("out"))
  dac_out = graph.count("dac", "out", ("fft"))
  fft_out = graph.count("fft", "out", ("dac"))
  return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out

data = aoc.retuple_read("src dst", r"(\w+): (.*)$")
aoc.cprint(solve(data))
