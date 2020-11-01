try:
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
except ValueError:
    print("please give correct args")
    quit()


print("midpoint of line: (" + str((x1+x2)/2) + "," + str((y1+y2)/2) + ")")
    