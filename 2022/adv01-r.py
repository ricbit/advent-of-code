import aoc
import heapq

blocks = aoc.line_blocks()
sum_blocks = [sum(int(line) for line in block) for block in blocks]
aoc.cprint(max(sum_blocks))
aoc.cprint(sum(heapq.nlargest(3, sum_blocks)))
