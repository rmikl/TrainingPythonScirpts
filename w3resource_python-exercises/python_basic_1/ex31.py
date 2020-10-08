def choose_smaller(first_int,second_int):
    if first_int > second_int:
        return second_int
    else:
        return first_int

def choose_gd (first_int, second_int):
    common_divisor = 0
    output = 0
    for i in range(1,choose_smaller(first_int,second_int),1):
        common_divisor = common_divisor + 1
        if first_int % common_divisor == 0 and second_int % common_divisor == 0:
            output = common_divisor
    return output
     
try:    
    first_int = int(input('please give first int : '))
    second_int = int(input('please give second int : '))
except ValueError:
    print('please give int!')
    quit()

print("the greatest common divisor is :"  + str(choose_gd(first_int,second_int)))