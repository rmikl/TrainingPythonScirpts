inp = input("Please give a list of numbers in format: NUMBER,NUMBER,NUMBER ")

inp = inp.split(",")
counter = 0

for i in inp:
    try:
        int(i)
    except ValueError:
        print("Wrong value in a list")
        quit()
    if int(i) == 4:
        counter = counter+1

print(counter)