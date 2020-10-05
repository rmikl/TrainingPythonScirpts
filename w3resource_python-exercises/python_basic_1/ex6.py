import sys

try:
    l = sys.argv[1]
except IndexError:
    print("Missing argument")
    quit()

print ("list : " + str(l.split(",")))
print ("tuple : " + str(tuple( l.split(","))))