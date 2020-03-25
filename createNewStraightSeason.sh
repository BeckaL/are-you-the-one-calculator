#!/bin/zsh
seasonName=$1
scenarios=$2
women=$3
men=$4

mkdir "$seasonName" && cd "$seasonName" || exit

echo "$men" > men.txt
echo "$women" > women.txt
echo "$scenarios" > week0.csv

