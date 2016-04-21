#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

#######################
# 
# 
#######################

if (($#==00))
then echo "Usage: ./check_file.bash <filename>"
     exit 1
fi

if (($#!=1))
then echo "Error: too many arguments for check_file.bash"
     exit 2
fi

FILE=$@

if [[ -e $FILE ]]
then echo "$FILE exists"
else echo "$FILE does not exist"
fi

if [[ -d $FILE ]]
then echo "$FILE is a directory"
else echo "$FILE is not a directory"
fi

if [[ -f $FILE ]]
then echo "$FILE is an ordinary file"
else echo "$FILE is not an ordinary file"
fi

if [[ -r $FILE ]]
then echo "$FILE is readable"
else echo "$FILE is not readable"
fi

if [[ -w $FILE ]]
then echo "$FILE is writable"
else echo "$FILE is not writable"
fi

if [[ -x $FILE ]]
then echo "$FILE is executable"
else echo "$FILE is not executable"
fi
exit 0
