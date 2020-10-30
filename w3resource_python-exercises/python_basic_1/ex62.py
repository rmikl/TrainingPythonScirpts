menu = """ 
Please choose a time unit: 
1.Year
2.Month
3.Week
4.Day
5.Hour
6.Minute

"""

try:
    unit = int(input(menu))
    amount = int(input("Please give amount: :"))
except ValueError:
    print("Wrong value putted")
    quit()

if unit == 1:
    result = 365 * 24 * 60 * 60 * amount
elif unit == 2:  
    result = 30 * 24 * 60 * 60 * amount
elif unit == 3:  
    result = 7 * 24 * 60 * 60 * amount
elif unit == 4:  
    result = 24 * 60 * 60 * amount   
elif unit == 5:
    result = 60 * 60 * amount
elif unit == 6:
    result = 60 * amount

print(result)

