#!/bin/bash

: '
Bob needs a fast way to calculate the volume of a cuboid with three values: length, width and the height of the cuboid. Write a function to help Bob with this calculation.

In bash the script is ran with the following 3 arguments: length width height
'
length=$1
width=$2
height=$3

function VoCuboid() {
  echo $length*$width*$height | bc
}

VoCuboid length width height
