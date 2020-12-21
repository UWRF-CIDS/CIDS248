#!/usr/bin/python

import sys

check_imports = '''
import check50
import check50.c
'''

exists_check = '''
@check50.check()
def exists():
    """typescript file exists"""
    check50.exists("typescript")
'''

check_template = '''
@check50.check(exists)
def contains_{x}():
    """command "{x}" is present"""
    output = check50.run("grep -c -w '{x}' typescript").stdout()
    if output == "0\\n":
        help = "Make sure that you try all commands in the lab. To start the script command so that it appends to you typescript file, use 'script -a typescript'"
        raise check50.Failure(help)

'''


filename = sys.argv[1]

print(check_imports)
print(exists_check)

with open(filename, "r") as file_object:
    # read file content
    data = file_object.readlines()
    # print file contents
    for line in data:
        print(check_template.format(x = line.strip()))
