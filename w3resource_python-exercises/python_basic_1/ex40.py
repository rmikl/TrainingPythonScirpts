try:    
    x_1 = float(input('x1: '))
    x_2 = float(input('x2: '))
    y_1 = float(input('y1: '))
    y_2 = float(input('y2: '))
except ValueError:
    print('please give int!')
    quit()
 
output = (( x_2 - x_1 ) ** 2  + (y_2 - y_1) ** 2) ** ( 1 / 2 )

print("distance points is : " + str(output))