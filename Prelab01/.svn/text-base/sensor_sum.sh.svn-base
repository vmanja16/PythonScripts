#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

#######################
#sensor_sum.sh
#######################
if (($#==0));then
echo "usage: sensor_sum.sh <filename>";exit 0;fi

if (($#!=1));then
echo "error: too many arguments";exit 1;fi

if [[ ! -r $1 ]];then
echo "error: $1 is not a readable file!";exit 2;fi


while read LINE
do
SENSOR=$(echo $LINE| head -c 2)
N0=$(echo $LINE|tr -s " "|cut -d " " -f 2)
N1=$(echo $LINE|tr -s " "|cut -d " " -f 3)
N2=$(echo $LINE|tr -s " "|cut -d " " -f 4) 
((SUM=$N0+$N1+$N2))
echo $SENSOR $SUM
done <$1
exit 0
