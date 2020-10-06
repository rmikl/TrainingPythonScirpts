import sys

try: 
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    third = int(sys.argv[3])
except IndexError:
    print("scripts takes 3 args")
    quit()

if first == second == third:
    print(str(first*second*third*3))
else:
    print(str(first+second+third))