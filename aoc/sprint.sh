for i in `seq -f "%02g" 1 25` ; do 
  if [ -f adv$i-r.py ] ; then
    echo
    echo "Problem $i"
    time python3.12 adv$i-r.py < input.$i.txt 
  fi ;
done
