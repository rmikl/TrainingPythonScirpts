import sys

help_message = """

Usage: python ex4.py INT INT INT

Script is counting the sum of the digits in an integer
"""

try:
    list = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
except IndexError:
    print(help_message)
    quit()

if sys.argv[1] == "-h": 
    print(help_message)
    quit()
else:
    list.sort()
    print(list)
