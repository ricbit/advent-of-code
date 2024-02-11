import sys

D = 14
for line in sys.stdin:
  for index in range(len(line.strip()) - D):
    if len(set(line[index:index + D])) == D:
      print(index + D)
      break
      
