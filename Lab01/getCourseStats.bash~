#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$


if (( $# != 1 ));then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1;
fi 

FILE=$1

if [[ ! -r $FILE ]];then
    echo "Error reading input file: $FILE"
    exit 2
fi
BASE=$(echo $FILE|cut -d "." -f 1)
OUTPUT=$(echo $BASE.out|head -n 1)
if [[ -e $OUTPUT ]];then
    echo "Output file $OUTPUT already exists"
    exit 3
fi

while read LINE
do
NAME=$(echo $LINE|cut -d "," -f 1)
AS=$(echo $LINE|cut -d "," -f 2)
M1=$(echo $LINE|cut -d "," -f 3)
M2=$(echo $LINE|cut -d "," -f 4)
PR=$(echo $LINE|cut -d "," -f 5)
((SCORE=15*$AS/100 + 30*$M1/100 + 30*$M2/100+ 25*$PR/100))

echo $NAME,$SCORE >>$OUTPUT

done <$1

exit 0


