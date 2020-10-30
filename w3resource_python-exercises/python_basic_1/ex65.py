try:
    input = int(input("please give number of seconds"))
except ValueError:
    print("Wrong Value")
    quit()

year = month = week = day = hour = minute =0

if input >= 31557600:
    year = (input - (input%31557600)) / 31557600
    input = input % 31557600
if input >= 2629800:
    month = (input - (input%2629800)) / 2629800
    input = input % 2629800    
if input >= 604800:
    week = (input - (input%604800)) / 604800
    input = input % 604800  
if input >= 86400:
    day = (input - (input%86400)) / 86400
    input = input % 86400      
if input >= 3600:
    hour = (input - (input%3600)) / 3600
    input = input % 3600
if input >= 60:
    minute = (input - (input%60)) / 60
    input = input % 60

print("Year: " + str(year))
print("Month: " + str(month))
print("Week: " + str(week))
print("Day: " + str(day))
print("Hour: " + str(hour))
print("Minute: " + str(minute))
print("Seconds: " + str(input))








