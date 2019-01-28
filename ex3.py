import csv
import math

with open('wspolrzedneTR.txt') as file:
    reader = csv.reader(file,delimiter='\t')

    triangleList = []

    for row in reader:
        a = {'x': row[0], 'y': row[1]}
        b = {'x': row[2], 'y': row[3]}
        c = {'x': row[4], 'y': row[5]}
        triangle = {'a': a, 'b': b, 'c': c}
        triangleList.append(triangle)

    length = 0

    for el in triangleList:
        AB = math.hypot(int(el['a']['x'])-int(el['b']['x']), int(el['a']['y'])-int(el['b']['y']))
        BC = math.hypot(int(el['b']['x'])-int(el['c']['x']), int(el['b']['y'])-int(el['c']['y']))
        AC = math.hypot(int(el['a']['x'])-int(el['c']['x']), int(el['a']['y'])-int(el['c']['y']))
        circ = AB + AC + BC
        if circ > length:
            length = circ

    print(round(length, 2))





