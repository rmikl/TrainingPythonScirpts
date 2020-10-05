import math, sys

PI = math.pi
help_message = """

Usage: python ex4.py RANGE

Script is returning AREA of circle 
"""


try:
    R = sys.argv[1]
except IndexError:
    print(help_message)
    quit()

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(help_message)
    quit()
else:
    print("PI : " + str(PI))
    print("RANGE: " + R)
    AREA = math.pow(float(R),2) * PI
    print("AREA: " + str(AREA))