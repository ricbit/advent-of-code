# P01

Goal: 03:47 06:08
Time: 03:55 06:17

Algo: string manipulation

## Fails

- Deducing problem just from the inputs failed. I thought I had to group the values, but actually it was just comparison to neighbour. Also didn't notice the list was circular.
  - FIX: Better reading
- Lots of typos.
  - FIX: Turn off autocomplete, didn't like it.
- Groupby second argument is iterator, not a list.
  - FIX: Memorize
- Too much time typing out the python cmd.
  - FIX: Write script
- Samples were presented inline in the text.
  - FIX: Should have a script for that.
- Too much time clicking on timer.
  - FIX: Stop timer with script.
- Manual copying from p1 into p2.
  - FIX: Script do it automatically but it is too slow. Custom script.
- Vim took too much time to open (1s)
  - FIX: Maybe it gets faster without loading autocomplete.

## Wins

- Script worked. (Remember to have only one chrome window open)
- Timer worked.
- Auto clipboard worked.
- Auto open of input was a big win (to check if the input length was even).

# P02

Goal: 02:18 06:13
Time: 02:04 10:42

Algo: max and min, mod and div

## Fails

- Didn't notice P2 had a different sample than P1.
  - FIX: Maybe printing a warning on the python pane using tmux
- Correct syntax is combinations, not combination.
  - FIX: Memorize, combinations and permutations have s, product does not.
- Forgot to use ./p1 and ./p2 to stop the clock.
  - FIX: This is muscle memory, will come with time.
- Script ./runsample didn't work.
  - FIX: Check the error.
- Script download tried to launch a second timer for P2.
  - FIX: Timer should be launched only for P1
- Didn't update the browser with P2.
  - FIX: Script download should do that.

## Wins

- LEADERBOARD! (for P1)
- Timer in black looks nicer.
- Auto copy of P1 into P2 worked.
- Opening vim is much faster.
- Less typos without autocomplete.
- Script ./full worked nice.
