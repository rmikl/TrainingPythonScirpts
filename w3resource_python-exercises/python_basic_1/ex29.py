print("FORMAT OF LIST NUMBER,NUMBER,NUMBER")
list_1 = input("FIRST LIST : ")
list_2 = input("SECOND LIST: ")

list_1 = list_1.split(",")
list_2 = list_2.split(",")

output_list = []
for i in list_2:
    if i not in list_1:
        output_list.append(i)

print(output_list)
