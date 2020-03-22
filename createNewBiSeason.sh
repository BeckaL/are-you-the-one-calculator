#!/bin/zsh
seasonName=$1
scenarios=$2
contestants=$3

mkdir "$seasonName" && cd "$seasonName" || exit
touch contestants.txt
touch week0.csv

echo "$contestants" > contestants.txt
echo "$scenarios" > week0.csv

