inp = input("Please give a list of numbers in format: NUMBER,NUMBER,NUMBER ")
value = input("please put a value to check: ")

inp = inp.split(",")
for i in inp:
    try:
        int(i)
    except ValueError:
        print("Wrong value in a list")
        quit()
    
if value in inp :
    print('value is in list')
else:
    print('value in not in list')

