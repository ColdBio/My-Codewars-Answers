#!/bin/bash
: '
Simple, remove the spaces from the string, then return the resultant string.
Question
'
var="$1"

# removes all whitespaces in a string
echo $var | sed 's/ //g'

# Another solution
echo "$1" | tr -d " "
