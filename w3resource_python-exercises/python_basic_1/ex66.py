try:
    weight = float(input("please give weight in KG : "))
    height = float(input("please give height in M : "))
except ValueError:
    print("wrong values putted")
    quit()

BMI = weight / height **2

print(str(BMI))
    