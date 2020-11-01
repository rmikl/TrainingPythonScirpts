import os,pathlib
from datetime import datetime

folder = input("please give folder to check, give 'current' if You want current folder. \n")

list= []

if folder == "":    
    list = os.listdir()
    folder = str(pathlib.Path().absolute())
else: 
    try:
        list = os.listdir(folder)
    except FileNotFoundError:
        print("please provide correct folder path")
        quit()

list_of_dict = []
for i in list:
    folder_dict = {
        "name" : i,
        "mod_time" : datetime.fromtimestamp( os.path.getctime(os.path.join(folder,i))).strftime('%Y-%m-%d %H:%M:%S')    
    }
    list_of_dict.append(folder_dict)

list_of_dict =  sorted(list_of_dict, key = lambda i: i['mod_time'])

for i in list_of_dict:
    print()
    for x in i:
        print(i[x],end=" ")
print()
        