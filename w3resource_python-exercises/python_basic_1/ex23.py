input_int = input("Give a number: ")
input_string = input("Give a string: ")



if input_string == "":
    print("no string putted")
    quit()

try:
    input_string = input_string[0]+input_string[1]
except IndexError:
    input_string = input_string[0]

output_string = ""

for i in range(0,int(input_int),1):
    output_string = input_string + output_string

print(output_string)