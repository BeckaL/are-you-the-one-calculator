#!/bin/zsh
seasonName=$1
scenarios=$2
women=$3
men=$4

mkdir "$seasonName" && cd "$seasonName" || exit
touch men.txt
touch women.txt
touch week1.csv

echo "$men" > men.txt
echo "$women" > women.txt
echo "$scenarios" > week1.csv

