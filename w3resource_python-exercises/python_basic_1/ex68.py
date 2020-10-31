import sys

help_message = """

Usage: python ex4.py INT

Script is counting the sum of the digits in an integer
"""
try:
    sys.argv[1]
except IndexError:
    print(help_message)
    quit()

if sys.argv[1] == "-h": 
    print(help_message)
    quit()
else:
    counter = 0
    for i in sys.argv[1]:
        counter = counter + int(i)
    print(str(counter))