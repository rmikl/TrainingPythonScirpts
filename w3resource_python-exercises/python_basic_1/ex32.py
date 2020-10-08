def choose_bigger(first_int,second_int):
    if first_int > second_int:
        return first_int
    else:
        return second_int

def LCM(first_int,second_int):
    counter = choose_bigger(first_int,second_int)
    while True:
        if counter % first_int == 0 and counter % second_int == 0:
            return(counter)
        else:
            counter = counter + 1 

try:    
    first_int = int(input('please give first int : '))
    second_int = int(input('please give second int : '))
except ValueError:
    print('please give int!')
    quit()

print("LCM is : " + str(LCM(first_int,second_int)))