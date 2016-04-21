#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$
#
#######################
# Takes in a list of filenames.
# Checks if each file is readable. 
# Creates file if non-existant.
#######################

for filename in $@
do
if [[ -r $filename ]]
then printf "%s is readable!\n" $filename
else
    if [[ ! -e $filename ]]
    then touch $filename
    fi
fi
done
exit 0