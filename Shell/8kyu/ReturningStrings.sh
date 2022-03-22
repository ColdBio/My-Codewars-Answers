#!/usr/bin/env bash

echo "Hello, $1 how are you doing today?"

for each in $(ls); do
  echo $each 
done
