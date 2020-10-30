try:
    distance = int(input("Please give a distance in feet : "))
except ValueError:
    print("Please give a int")
    quit()

print("this is " + str(12 * distance) + " in inches")
print("this is " + str((1/3) * distance) + " in yards")
print("this is " + str((1/5280) * distance) + " in miles")