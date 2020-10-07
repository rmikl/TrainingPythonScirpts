inp = input("Please give a list of numbers in format: NUMBER,NUMBER,NUMBER ")
value = int(input("after what value stop print: "))


inp = inp.split(",")
for i in inp:
    try:
        int(i)
    except ValueError:
        print("Wrong value in a list")
        quit()

for i in inp:
    if int(i) > value:
        quit() 
    elif int(i) % 2 == 0:
        print(i)