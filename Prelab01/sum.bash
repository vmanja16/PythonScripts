#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

#######################
# Takes in two or more integer arguments.
# Outputs the sum of those integers
#######################

sum=0
while (($#))
do
((sum=$sum+$1)) 
shift
done
printf "%d\n" $sum
exit 0