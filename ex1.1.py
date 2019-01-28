import csv

with open('wspolrzedne.txt') as file:
    reader = csv.reader(file,delimiter='\t')

    triangleList = []

    for row in reader:
        a = {'x':row[0], 'y':row[1]}
        b = {'x':row[2], 'y':row[3]}
        c = {'x':row[4], 'y':row[5]}
        triangle = {'a':a, 'b':b, 'c':c}
        triangleList.append(triangle)


    count = 0

    for e in triangleList:
        if int(e['a']['x']) > 0 and int(e['a']['y']) > 0 and int(e['b']['x']) > 0 and int(e['b']['y']) > 0 and int(e['c']['x']) > 0 and int(e['c']['y']) > 0:
            count = count + 1




    print(count)
