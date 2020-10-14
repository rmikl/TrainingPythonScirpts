try:
    feet = int(input("please give how many feets :"))
    inch = int(input("please give how many inches :"))
except ValueError:
    print("please give integers")
    quit()

print (str(float(feet)*30.48 + float(inch)*2.54))
    
