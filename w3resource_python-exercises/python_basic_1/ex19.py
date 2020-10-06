import re
string = input("GIVE A STRING : ")

try:
    print(re.search("^Is",string).string)
except AttributeError:
    print("Is " + string)
