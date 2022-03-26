#!/bin/bash
: ' 
Your function takes two arguments:

current fathers age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

'
dad_years_old=$1
son_years_old=$2

# First time round solution
double=$(( $1 - ($2 * 2) ))

if [[ $double -lt 0 ]]
then
  echo $double | tr -d "-"
else
  echo $double
fi
exit

# Second time round solution
echo $double | tr -d "-"
