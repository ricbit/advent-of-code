start=${1:-1}
end=${2:-25}
for i in `seq -f "%02g" $start $end` ; do 
  if [ -f adv$i-r.py ] ; then
    echo
    echo "Problem $i"
    time python3.13 adv$i-r.py < input.$i.txt 
  fi 
done
