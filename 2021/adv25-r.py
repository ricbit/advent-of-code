import sys
import aoc
import numpy as np

def move_vectorized(arr, cdir, caxis):
  rows, cols = arr.shape
  right_mask = arr == cdir
  next_positions = np.roll(arr, -1, axis=caxis)  
  can_move_right = right_mask & (next_positions == '.')
  new_arr = arr.copy()
  new_arr[can_move_right] = '.'
  move_to_positions = np.roll(can_move_right, 1, axis=caxis)  
  new_arr[move_to_positions] = cdir
  return new_arr

def npstep(arr):
  narr = np.array(arr)
  narr = move_vectorized(narr, '>', 1)
  narr = move_vectorized(narr, 'v', 0)
  return narr

state = [list(line.strip()) for line in sys.stdin]
w, h = len(state[0]), len(state)

ans = 0
while True:
  newstate = npstep(state)
  ans += 1
  if np.array_equal(newstate, state):
    break
  state = newstate

aoc.cprint(ans)

