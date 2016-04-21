#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$
#
#######################
# Takes in a filename.
# Printouts out file with line numbers 
#######################

if (($#==0))
then echo "Usage: line_num.bash <filename>"
exit 0
fi

if (($#!=1))
then echo "Error: line_num.bash requires only one input filename"
exit 1
fi

if ! [[ -r $1 ]]
then echo "Cannot read $1"
exit 2
fi

count=0
while read line
do
((count++))
echo "${count}:${line}"
done <$1

exit 0 