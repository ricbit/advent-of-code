import sys
import itertools
import aoc
import numpy as np

def solve_numpy(data):
  secret_size = 2001
  buyers = len(data)
  mask = 2 ** 24 - 1
  all_4seq = 19 ** 4

  n = np.array(data, dtype=np.int32)
  all_secrets = np.zeros((secret_size, buyers), dtype=np.int32)
  all_secrets[0,:] = n
  for i in range(1, secret_size):
    n ^= (n << 6) & mask
    n ^= (n >> 5)
    n ^= (n << 11) & mask 
    all_secrets[i,:] = n
  part1 = sum(n.astype(np.uint64))
  value = all_secrets % 10
  diff = value[:-1] - value[1:] + 9
  encode = diff[:-3] + 19 * diff[1:-2] + 19**2 * diff[2:-1] + 19**3 * diff[3:]
  encode += np.arange(buyers) * all_4seq

  flat_value = value[4:].flatten()
  unique_values, unique_indices = np.unique(encode, return_index=True)
  col = np.zeros(all_4seq, dtype=np.uint16)
  np.add.at(col, unique_values % all_4seq, flat_value[unique_indices])
  return part1, max(col)

if __name__ == "__main__":
  data = aoc.ints(sys.stdin.read().splitlines())
  part1, part2 = solve_numpy(data)
  aoc.cprint(part1)
  aoc.cprint(part2)

