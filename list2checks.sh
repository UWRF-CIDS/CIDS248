#!/bin/bash

if [ $# -ne 1  ]; then
	echo "Usage: list2checks.py <command list file>"
   exit 1
fi

echo "Warning: continuing will overwrite the file \"__init__.py\". Continue? (y/n)"
read choice

if [ "$choice" != "y" ]; then
   echo "Bye!"
   exit 0
fi



header='
import check50
import check50.c

@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")

'

echo "$header" > __init__.py

while IFS= read -r line; do
   sed "s/????/${line}/g" template.py >> __init__.py
done < "$1"
