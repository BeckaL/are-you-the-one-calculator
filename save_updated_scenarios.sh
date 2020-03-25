#!/bin/zsh
seasonName=$1
scenarios=$2
week_number=$3

cd "$seasonName" || exit
echo "$scenarios" > "week${week_number}.csv"

