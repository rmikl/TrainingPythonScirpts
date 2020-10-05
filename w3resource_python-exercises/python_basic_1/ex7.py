import sys

try:
    filename = sys.argv[1]
except IndexError:
    print('missing argument')
    quit()

try:
    filename.split(".")[1]
except IndexError:
    print("File without ext")

print("EXT: " +  filename.split(".")[-1] )