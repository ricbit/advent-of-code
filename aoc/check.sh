day=$(printf "%02d" $1)
time python3.12 adv${day}-r.py < altinputs/input.${day}.txt 
