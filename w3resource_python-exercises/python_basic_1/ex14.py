import datetime, sys

help_message = """
Day Calulator

USAGE:

python ex14.py FIRST_DATE_YEAR,FIRST_DATE_MONTH,FIRST_DATE_DAY SECOND_DATE_YEAR,SECOND_DATE_MOTNH,SECOND_DATE_DAY


"""

if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(help_message)
    quit()
    

try:
    s_date = sys.argv[2]
    f_date = sys.argv[1]    
except IndexError:
    print("script without needed arguments")
    quit()

s_date_list = s_date.split(",")
f_date_list = f_date.split(",")

if len(s_date_list) == 3 or len(f_date_list) == 3:
    try:
        first_date = datetime.date(int(f_date_list[0]),int(f_date_list[1]),int(f_date_list[2]))
        second_date = datetime.date(int(s_date_list[0]),int(s_date_list[1]),int(s_date_list[2]))
    except ValueError:
        print("bad format for argument")
        quit()        
else :
    print("bad format for argument")
    quit()


print(first_date - second_date)