try:    
    first_int = int(input('please give first int : '))
    second_int = int(input('please give second int : '))
except ValueError:
    print('please give int!')
    quit()

if first_int == second_int or first_int+second_int == 5 or abs(first_int - second_int) == 5:
    print("True")
else:
    print("False") 