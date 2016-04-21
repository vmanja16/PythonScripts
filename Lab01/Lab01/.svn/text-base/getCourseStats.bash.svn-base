#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$


if (( $# != 1 ));then
    echo "Usage: ./getCourseStats.bash <course name>"
    exit 1;
fi 

COURSE=$1
if [[ $COURSE != 'ece337'  &&  $COURSE != 'ece468' && $COURSE != 'ece364' ]];then
    echo "Error: course $COURSE is not a valid option"
    exit 5
fi

FILE_LIST=$(ls gradebooks/$COURSE*)

TOTAL=0

for FILE in $FILE_LIST
do
./getFinalScores.bash $FILE
if (($?!=0));then
    echo " Error while running getFinalScores.bash"

    exit 3
fi

<$FILE
while read LINE
do
((TOTAL++))
done <$FILE

done

echo "Total students: $TOTAL"

TOTAL2=0
OUTLIST=$(ls gradebooks/$COURSE*.out)

MAX=0
STUDENT=""
for F in $OUTLIST
do
<$F
NUMBER2=0
while read LINE
  do
  NUMBER=$(echo $LINE|cut -d "," -f 2)
  if ((NUMBER>MAX));then
    MAX=$NUMBER
    STUDENT=$(echo $LINE|cut -d "," -f 1)
  fi
  ((NUMBER2=NUMBER2+NUMBER))
  done <$F

((TOTAL2=TOTAL2+$NUMBER2))

done

AVERAGE=$((TOTAL2/TOTAL))
echo "Average score: $AVERAGE"
echo "$STUDENT had the highest score of $MAX"

exit 0