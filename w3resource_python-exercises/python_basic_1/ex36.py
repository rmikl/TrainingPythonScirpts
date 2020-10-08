try:    
    first_int = int(input('please give first int : '))
    second_int = int(input('please give second int : '))
except ValueError:
    print('please give int!')
    quit()

print(str(first_int+second_int))