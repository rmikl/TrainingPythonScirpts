try:    
    first_int = int(input('please give first int : '))
    second_int = int(input('please give second int : '))
except ValueError:
    print('please give int!')
    quit()


if first_int + second_int > 15 and first_int + second_int < 20:
    print("20")
else:
    print(str(first_int+second_int))