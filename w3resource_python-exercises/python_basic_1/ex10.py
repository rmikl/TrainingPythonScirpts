import sys

try:
    sys.argv[1]
except IndexError:
    print("no args given")
    quit()

n = sys.argv[1]
nn = n + n
nnn = n + n + n

try:
    int(nn)
except ValueError:
    print("cannot convert argument please give aa number as an argument")
    quit()

print(int(n) + int(nn) + int(nnn))


