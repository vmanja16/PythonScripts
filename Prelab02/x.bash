#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

if (($#!=1));then echo "Usage ./process_temps.bash <input file>";exit 1;fi
if [[ ! -r $1 ]];then echo "Error: $1 is not a readable file";exit 2;fi

COUNT=0
while read -a ARR
do
  if (( $COUNT==0 ));then COUNT=1;continue;fi
 # ARR=($LINE)
  SUM=0
  for i in ${!ARR[*]}
  do
    if ((i==0));then continue;fi
    (( SUM = $SUM + ${ARR[i]} ))
  done
  (( AVG = $SUM / ((${#ARR[*]}-1)) ))
  TIME=${ARR[0]}
  echo "Average temperature for time $TIME was $AVG C"
done <$1

   
exit 0

