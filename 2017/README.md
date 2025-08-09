# P25

Goal: 10:38 11:16
Time: 09:52 09:57

Algo: turing machine

# P24

Goal: 16:44 21:02
Time: 08:14 11:45

Algo: memoization

# P23

Goal: 05:03 54:41
Time: 04:42 54:00 

Algo: assembly emulation, optimization

# P22

Goal: 13:47 20:29
Time: 10:45 17:42

Algo: cellular automata

# P21

Goal: 41:11 44:51
Time: 21:55 22:24

Algo: fractal, rotate and flip

# P20
Goal: 10:45 21:33
Time: 14:08 123:19

Algo: particles

# P19

Goal: 15:49 18:04
Time: 17:01 18:29

Algo: path walking

# P18

Goal: 12:50 41:02
Time: 11:08 121:42

Algo: assembly emulation

# P17

Goal: 06:38 15:51 
Time: 07:38 20:00

Algo: mod

# P16

Goal: 08:31 26:37
Time: 15:43 61:05

Algo: permutation power

# P15

Goal: 05:41 09:32
Time: 16:02 20:30

Algo: rng

# P14

Goal: 09:08 25:06
Time: 14:27 24:12

Algo: floodfill

### Fails

- Still having keyboard freezes.
  - FIX: Still don't know.
- Keybindings not ideal.
  - FIX: Change it

### Wins

- Leaderboard P2

# P13

Goal: 10:40 21:46
Time: 11:27 50:35

Algo: simulation, mod

### Fails

- Forgot to ignore trails with no cars.
  - FIX: Attention
- Too sleepy on the first run.
  - FIX: Don’t code after midnight.

### Wins

- Time on P1 was ok, missed by little.

# P12

Goal: 06:24 09:06
Time: 04:58 07:36

Algo: connected components

### Fails

- Lacked aoc.first.
  - FIX: Already added

### Wins

- Leaderboard P1/P2

# P11

Goal: 08:23 11:43
Time: 20:42 23:24

Algo: hex grids

### Fails

- Never had to code an hex grid before.
  - FIX: Learned from reddit.

### Wins

- I was able to deduce how it worked, albeit slowly.

# P10

Goal: 12:24 25:24
Time: 09:09 26:00

Algo: reverse a list, xor

### Fails

- Needs to press end when a page is loaded
  - FIX: Probably on the extension.
- Xor should have been on the horizontal instead of vertical.
  - FIX : Better reading.

### Wins

- Leaderboard P1
- aoc.ints()  

# P09

Goal: 09:25 11:37
Time: 07:29 09:47

Algo: parser

### Fails

- Sample numbering in screen is confusing.
  - FIX: More colors.
- Massive slowdown during streaming.
  - FIX: Investigate.

### Wins

- Leaderboard P1/P2

# P08

Goal: 07:08 08:22
Time: 08:01 09:08

Algo: assembly emulation

### Fails

- Stream was still in 4k.
  - FIX: Settings of OBS.
- Too slow to write a re parser for integer.
  - FIX: Add to the lib?
- Unsure if eval returned the value inline.
  - FIX: Memorize. It does.

### Wins

- ddict and retuple are awesome.
- Fast P2.

# P07

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

# P06

Goal: 07:22 09:30
Time: 07:30 09:40

Algo: circular list

### Fails

- Stream truncated, lost my times.
  - FIX: Assume I didn't make it.

### Wins

- Quick problem.

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
- Script ./runsample didn't work.
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
- Script ./full worked nice.

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


