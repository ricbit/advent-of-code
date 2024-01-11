# P06

Goal: 05:40 25:21
Time: 12:12 46:48

Algo: topological sorting

### Fails

- Misread the problem, should have returned weight, instead returned name.
  - FIX: Better reading
- Scrolling on Chrome for P2.
  - FIX: Script ./download should automatically scroll to the end.

### Wins

- All scripts worked.

# P05

Goal: 03:18 04:46
Time: 05:12 07:30

Algo: traverse a list

### Fails

- Misread the problem, started to write a bfs which I didn't use.
  - FIX: Better reading
- Sample numbers in screen are confusing.
  - FIX: Change colors maybe.

### Wins

- Sound was good, window open.

# P04

Goal: 01:53 03:40
Time: 01:43 03:20

Algo: deduplication, anagrams

### Fails

- Forgot to add the script to stop the timer.
  - FIX: Add the script
- Very bad echo on sound
  - FIX: I think this was the monitor option in obs, turn it off.

### Wins

- LEADERBOARD for P1 and P2.

# P03

Goal: 08:29 23:19
Time: 19:58 33:32

Algo: spiral of integers

### Fails

- This is a common problem, I should have had it in my lib.
  - FIX: Add to lib
- Forgetting to add part number to ./full.
  - FIX: Exporting part number from the download script.
- Script ./runsample didin't work.
  - FIX: Update it.
- Too much noise in streaming.
  - FIX: Use a filter.
- Too much copy and paste led to code difficult to update in part2.
  - FIX: There is always a way to refactor copy and paste.
- Forgot to stop the timer.
  - FIX: Make it automatic inside the download script
- Should have used complex numbers from the start, much easier this way.
  - FIX: If the algo has 90 degrees turns somewhere, use complex.

### Wins
- Reasonable complex algorithm, worked on first attempt for P1 and P2.
- Chrome extension to enumerate samples worked.
- Timer is launched automatically by ./download.

# P02

Goal: 02:18 06:13
Time: 02:04 10:42

Algo: max and min, mod and div

### Fails

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

### Wins

- LEADERBOARD! (for P1)
- Timer in black looks nicer.
- Auto copy of P1 into P2 worked.
- Opening vim is much faster.
- Less typos without autocomplete.
- Script ./full worked nice.# P01

# P01

Goal: 03:47 06:08
Time: 03:55 06:17

Algo: string manipulation

### Fails

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

### Wins

- Script worked. (Remember to have only one chrome window open)
- Timer worked.
- Auto clipboard worked.
- Auto open of input was a big win (to check if the input length was even).


