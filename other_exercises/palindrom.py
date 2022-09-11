import sys

palindrom = sys.argv[1]

rev_palindrom = palindrom [::-1]

if rev_palindrom == palindrom: 
    print("String '" + palindrom + "' is palindrom")
else:
    print("String '" + palindrom + "' is not palindrom")
