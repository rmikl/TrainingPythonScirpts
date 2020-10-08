try:
    amt = int(input('please give amount of borrowed money: '))
    rat_of_int = float(input('please give rate of interest in percent: ')) /100
    years = int(input('please give number of years : '))
except ValueError:
    print('please give int!')
    quit()

y = 1 + (rat_of_int /12)
n =  years * 12 
_sum =  amt * (y ** n ) * ( y - 1 ) / ( y ** n - 1 )  

output = 0
for i in range(0,n,1):
    output = output + _sum

print(str(output))
