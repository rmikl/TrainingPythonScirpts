integer = int(input("NUMBER TO CHECK:"))

if integer <= 0:
    print("WRONG NUMBER")
elif integer % 2 == 1:
    print("NUMER IS ODD")
else:
    print("NUMER IS EVEN")

