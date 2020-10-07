inp = input("Please give a list of numbers in format: NUMBER,NUMBER,NUMBER ")

inp = inp.split(",")
for i in inp:
    try:
        int(i)
    except ValueError:
        print("Wrong value in a list")
        quit()

string = ""
for i in inp:
    string = string + i

print(string)