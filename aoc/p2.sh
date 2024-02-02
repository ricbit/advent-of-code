echo -n "stop 2" | nc 'localhost' 12345 -q 0
CUR=`cat advcurrent.txt | grep -o -P "(\w+)" | head -1`
PART=`cat advcurrent.txt | grep -o -P "(\w+)$" | head -1`
REFAC="adv$CUR-r.py"
if [ ! -f $REFAC ]; then
  cp "adv$CUR-2.py" $REFAC
fi

