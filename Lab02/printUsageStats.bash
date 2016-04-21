#! /bin/bash
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

if (( $# != 1 )); then echo "Usage: ./printUsageStats.bash <filename>";exit 1; fi
if [[ ! -r $1 ]]; then echo "Error: $1 is no readable!"; exit 2; fi

TIMESTAMP=$(head -1 $1|cut -f 3 -d " ")
echo "Parsing file \"$1\". Timestamp: $TIMESTAMP"

echo "Your choices are"
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N Highest memusages"
echo "4) Top 3 longest running processes"
echo "5) All processes by a specific user"
echo "6) Exit"

x=0
while (( x==0)) 
do
read -p "Please enter your choice: " CHOICE </dev/tty

# CHOICE 1
if (( $CHOICE == 1 ));then
  USERS=$(head -n 1 $1| cut -f 8 -d " ")
  echo "Total number of active user IDs: $USERS"
fi

# CHOICE 2
if (( $CHOICE == 2 ));then
  read -p "Enter a value for N: " PEOPLE </dev/tty
  for ((i=1; i<PEOPLE+1; i++))
  do
    NAME=$(tail -n +8 $1| tail -n +$i|head -n 1| cut -f 2 -d " ")
    USAGE=$(tail -n +8 $1| tail -n +$i|head -n 1| cut -f 9 -d " ")
    echo $NAME $USAGE%
  done
fi

# CHOICE 3
if (( $CHOICE == 3 )); then
  read -p "Enter a value for N: " PEOPLE </dev/tty
  for (( i=1; i<PEOPLE+1; i++))
  do
    NAME=$(tail -n +8 $1|sort -k 10 -n -r| tail -n +$i| head -n 1| cut -f 2 -d " ")
    MEM=$(tail -n +8 $1|sort -k 10 -n -r| tail -n +$i| head -n 1|  cut -f 10 -d " ")
    echo "User $NAME is utilizing mem resources at $MEM%"
  done
fi

# CHOICE 4
if (( $CHOICE == 4 )); then
  for (( i=1; i<4; i++))
  do
    PID=$(tail -n +8 $1|sort -k 11 -n -r| tail -n +$i| head -n 1| cut -f 1 -d " ")
    CMD=$(tail -n +8 $1|sort -k 11 -n -r| tail -n +$i| head -n 1|  cut -f 12 -d " ")
    echo "PID: $PID, Cmd: $CMD"
  done
fi

# CHOICE 5
if (( $CHOICE == 5 ));then
  read -p "Please enter a valid username: " USERNAME </dev/tty
  tail -n +8 $1|grep $USERNAME >>/dev/null
  if (( $? == 0)); then 
    tail -n +8 $1|grep $USERNAME|cat >> temp_b04.txt
    LINES=$(cat temp_b04.txt|wc -l|cut -f 1 -d " ") 
for (( i=1; i < $LINES+1; i++))
    do
      DATA=$(tail -n +$i temp_b04.txt|head -n 1)
      CPU=$(echo $DATA| cut -f 10 -d " ")
      CMD=$(echo $DATA| cut -f 12 -d " ")
      echo "$CPU $CMD"
    done <temp_b04.txt
   rm temp_b04.txt
  else echo "No match found";fi
fi

if (( $CHOICE == 6 )); then exit 0; fi

done


