CUR=`cat advcurrent.txt | grep -o -P "(\w+)" | head -1`
PART=`cat advcurrent.txt | grep -o -P "(\w+)$" | head -1`
time python3.12 adv$CUR-$PART.py < sample.$CUR.$1.txt

