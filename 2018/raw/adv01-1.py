import sys
import re
import itertools
import math
import aoc
import heapq
import functools
import copy
from collections import *
from dataclasses import dataclass

line = aoc.ints(sys.stdin.read().strip().split("\n"))
aoc.cprint(sum(line))
