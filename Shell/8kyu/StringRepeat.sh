#!/bin/bash
:' 
Write a function called repeatStr which repeats the given string string exactly n times.

repeatStr(6, "I") // "IIIIII"
repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
'
# My solution
repeat=$1
string=$2
result=""

for each in $(seq 1 $repeat)
do
    result+=$string
done

echo $result

# Better Solution
for i in `seq 1 $repeat`; do echo -n $string; done


