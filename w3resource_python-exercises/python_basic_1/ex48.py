fl = input("give a float : ")
it = input("give integer : ")

try:
    new_it = int(it)
    new_fl =float(fl)
except ValueError:
    print ("numbers given cannot be converted. ")

print(str(new_it), " + " , str(new_fl))

