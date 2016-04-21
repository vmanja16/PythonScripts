#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

#######################
#svncheck.bash
#######################

while read FILENAME
do

STATUS=$(svn status $FILENAME| head -c 1)

#FILENAME EXISTS
if [[ -e $FILENAME ]];then
    if [[ -z $STATUS ]];then
#     *svn file*      
        if [[ ! -x $FILENAME ]];then 
           svn propset svn:executable ON $FILENAME
        fi
#   * not svn *
    else
        if [[ ! -x $FILENAME ]];then
          read -p "Make $FILENAME executable (y/n)?" INPUT </dev/tty
            if (($INPUT=="y")); then
                chmod +x $FILENAME
            fi
        fi    
    svn add $FILENAME   
    fi

# FILENAME DOES NOT EXIST
else if [[ -z $STATUS ]];then 
     echo "Error: File $FILENAME appears to not exist here or in svn"
     fi
fi

done <$1

svn commit -m "Auto-commiting code"

exit 0
