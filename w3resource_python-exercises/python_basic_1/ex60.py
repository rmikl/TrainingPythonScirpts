try:
    leg_1 = float(input("please give 1 leg: "))
    leg_2 = float(input("please give 2 leg: "))
except ValueError:
    print("please give integers")
    quit()

hypotenuse = (leg_1**2 + leg_2**2) ** (1/2)

print(str(hypotenuse))
