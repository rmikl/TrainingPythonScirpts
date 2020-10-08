try:    
    first_int = int(input('please give first int : '))
    second_int = int(input('please give second int : '))
    third_int = int(input('please give third int : '))
except ValueError:
    print('please give int!')
    quit()

if first_int == second_int or second_int == third_int or first_int == third_int:
    print(0)
else:
    print(str(first_int + second_int + third_int))