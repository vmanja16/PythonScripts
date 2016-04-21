#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

if (($#!=1));then
    echo "Usage: yards.bash <filename>"
    exit 1
fi    

if [[ ! -r $1 ]];then
    echo "Error: $1 is not readable"
    exit 2
fi

MAX=0

while read -a LINE
do
    Conference=${LINE[0]}
    (( NumberOfScores=${#LINE[*]} - 1 ))
    
    SUM=0
    for i in ${!LINE[*]}
    do
        if (($i!=0));then
            ((SUM=SUM+${LINE[$i]}))
        fi
    done
   ((Average=$SUM/$NumberOfScores))
    if (($Average>$MAX));then MAX=$Average;fi

    TOTAL=0
    for i in ${!LINE[*]}
    do
        if (($i!=0));then
            (( DIFF=${LINE[$i]}-$Average ))
            (( TOTAL=$TOTAL+$DIFF**2 ))
        fi
    done    
    ((VARIANCE=$TOTAL/$NumberOfScores))

    echo "$Conference schools averaged $Average yards receiving with a variance of $VARIANCE"

done <$1

echo "The largest average yardage was $MAX" 
exit 0

