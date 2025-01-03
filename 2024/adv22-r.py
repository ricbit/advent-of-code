import sys
import aoc
import numpy as np

def solve_numpy(data):
  # This is a vectorized solution using numpy.

  # Let "monkeys" be the number of monkeys,
  # and "secrets" be the total number of secrets.
  #
  # The number of secrets for each monkey is 2001,
  # since there is one starting secret plus 2000 new generated ones.
  secrets = 2001
  monkeys = len(data)

  # We start with the initial data as int32,
  # we're using the smallest data type that can hold the secrets.
  n = np.array(data, dtype=np.int32)

  # Now we build a matrix will all secrets.
  # The first row has the original data.
  all_secrets = np.zeros((secrets, monkeys), dtype=np.int32)
  all_secrets[0, :] = n

  # Construct each row from the previous one.
  # The operations on each column are vectorized,
  # but I couldn't find a way to vectorize the rows.
  # Therefore ee use a simple loop for each row,
  # fortunately this turns out to be very fast anyway.
  # Also notice the mask ("prune") is not needed on the second operation.
  mask = 2 ** 24 - 1
  for i in range(1, secrets):
    n ^= (n << 6) & mask
    n ^= (n >> 5)
    n ^= (n << 11) & mask
    all_secrets[i, :] = n

  # Part one is just the sum of the final secret numbers for each monkey,
  # which at this point is still stored in the array "n".
  # We need to upgrade the data to uint64 though,
  # the sum won't fit in int32.
  part1 = sum(n.astype(np.uint64))

  # For part two, we start by building a "prices" matrix,
  # which is just the last digit of the secrets.
  prices = all_secrets % 10

  # Then we find the differences between each row.
  # This will be in the range [-9, 9],
  # we add 9 to each diff in order to make the range be [0, 18].
  diff = prices[:-1] - prices[1:] + 9

  # Now we encode each 4-tuple of differences in a base-19 number.
  # At this point the matrix "encode" has the encoded 4-tuples
  # in the order they appear to each monkey.
  # However each 4-tuple has the same value in any monkey.
  encoded = diff[:-3] + 19 * diff[1:-2] + 19**2 * diff[2:-1] + 19**3 * diff[3:]

  # We want to make 4-tuples unique to each monkey.
  # Since they are encoded as 4 digits of base-19 numbers,
  # this means each value is always smaller than 19 ** 4,
  # let's call this "maxvalue".
  maxvalue = 19 ** 4

  # If we multiply the index of each monkey by "maxvalue",
  # and add it to the "encoded" matrix,
  # then each element of the matrix will be
  # unique for a pair (4-value, monkey).
  # The objetive is to emulate a list[set] using numpy matrixes.
  encoded += np.arange(monkeys) * maxvalue

  # Now we filter only the first appearance of each 4-tuple for each monkey.
  # This is done by np.unique(), which will flatten the matrix,
  # sort all elements and return the indices where they first appeared.
  unique_tuple_monkey, unique_indices = np.unique(encoded, return_index=True)

  # Since the "encoded" matrix was flattened by np.unique(),
  # we also flatten the "prices" matrix
  # (after removing the first 4 rows, which are not valid 4-tuples).
  # At this point, the unique_indices into "encoded"
  # are also valid in "flat_prices", they are one to one.
  flat_prices = prices[4:].flatten()

  # Now we want to sum the prices for every 4-tuple,
  # ignoring the monkey they come from.
  # In order to ignore the monkey where each price come from,
  # we just need to take the values mod "maxvalue".
  unique_tuples = unique_tuple_monkey % maxvalue

  # Build an array where we'll accumulate the prices for each tuple.
  sum_tuples = np.zeros(maxvalue, dtype=np.uint16)

  # Then we use np.add.at, which will take the price for that tuple
  # and add it at the correct place in "sum_tuples".
  np.add.at(sum_tuples, unique_tuples, flat_prices[unique_indices])

  # Now the result for part two is just the max fo all sum_tuples.
  return part1, max(sum_tuples)

if __name__ == "__main__":
  data = aoc.ints(sys.stdin.read().splitlines())
  part1, part2 = solve_numpy(data)
  aoc.cprint(part1)
  aoc.cprint(part2)
