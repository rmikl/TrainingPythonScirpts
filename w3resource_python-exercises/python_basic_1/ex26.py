inp = input("Please give a list of numbers in format: NUMBER,NUMBER,NUMBER ")
value = input("please put a value to print: ")

inp = inp.split(",")
for i in inp:
    try:
        int(i)
    except ValueError:
        print("Wrong value in a list")
        quit()
    
for i in inp:
    string = ""
    for j in range(0,int(i),1):
        string = value + string
    print(string)
        
