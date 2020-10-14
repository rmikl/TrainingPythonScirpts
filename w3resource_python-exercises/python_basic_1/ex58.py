
try:
    n = int(input("Please give n: "))
except ValueError():
    print("its not a integer")
    quit()

sum = 0
for i in range(1,n+1,1):
    sum = sum + i

print(sum)