#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

if (($#!=2));then echo "Usage ./run.bash <simfile> <outputfile>";exit 1;fi

rm quick_sim 2>>/dev/null
gcc $1 -o quick_sim
if (( $? == 1 ));then 
    echo "error: quick_sim could not be compiled!"
    exit 2
fi

OUTPUT=$2
if [[ -e $OUTPUT ]];then
    read -p "$OUTPUT exists. Would you like to delete it? " ANS </dev/tty
    if [[ $ANS == 'y' ]];then rm $OUTPUT 2>/dev/null;fi
    if [[ $ANS == 'n' ]];then read -p "Enter a new filename: " OUTPUT </dev/tty
    rm $OUTPUT 2>>/dev/null;fi
fi



CACHE=(1 2 4 8 16 32)
WIDTH=(1 2 4 8 16)
PROCESSORS=(a i)
MAX_TIME=100000000

for C in ${CACHE[*]}
do
  for W in ${WIDTH[*]}
  do
    for P in ${PROCESSORS[*]}
    do
      DATA=$(./quick_sim $C $W $P)
      CPI=$(echo $DATA|cut -d ":" -f 8)
      TIME=$(echo $DATA|cut -d ":" -f 10)
      PROC=$(echo $DATA|cut -d ":" -f 2)
      if (( $TIME < $MAX_TIME));then 
        MAX_TIME=$TIME
        MAX_WIDTH=$W
        MAX_PROC=$PROC
        MAX_CACHE=$C
      fi
      echo "$PROC:$C:$W:$CPI:$TIME" >>$OUTPUT
    done
  done
done
echo "Fastest run time achieved by $MAX_PROC with cache size \
$MAX_CACHE and issue width $MAX_WIDTH was $MAX_TIME"

exit 0

