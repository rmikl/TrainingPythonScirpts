string = input("GIVE STRING TO MULTIPLY: ")
integer = input("NON NEGATIVE INTEGER: ")

if int(integer) < 1:
    print("IT IS NOT NON NEGATIVE INTEGER")
    quit()

STRING = ""

for i in range(0,int(integer),1):
    STRING = STRING + string

print(STRING) 