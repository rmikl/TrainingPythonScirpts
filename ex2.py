import csv
import numpy as np

with open('wspolrzedne.txt') as file:
    reader = csv.reader(file,delimiter='\t')

    triangleList = []

    for row in reader:
        a = {'x': row[0], 'y': row[1]}
        b = {'x': row[2], 'y': row[3]}
        c = {'x': row[4], 'y': row[5]}
        triangle = {'a': a, 'b': b, 'c': c}
        triangleList.append(triangle)
    count = 0

    for element in triangleList:
        if int(element['a']['x']) == int(element['b']['x']) == int(element['c']['x']) or int(element['a']['y']) == int(element['b']['y']) == int(element['c']['y']):
            count = count + 1
            continue
        elif int(element['a']['x']) == int(element['b']['x']) != int(element['c']['x']) or int(element['a']['y']) != int(element['b']['y']) == int(element['c']['y']):
            continue
        elif int(element['a']['x']) != int(element['b']['x']) == int(element['c']['x']) or int(element['a']['y']) == int(element['b']['y']) != int(element['c']['y']):
            continue
        elif int(element['a']['x']) != int(element['c']['x']) == int(element['b']['x']) or int(element['a']['y']) == int(element['c']['y']) != int(element['b']['y']):
            continue
        arr1 = np.array([[int(element['a']['x']), 1], [int(element['b']['x']), 1]])
        arr2 = np.array([int(element['a']['y']), int(element['b']['y'])])
        x = np.linalg.solve(arr1, arr2)
        a = int(x[0])
        b = int(x[1])

        if int(element['c']['y'] == a * int(element['b']['x'])) + b :
            count = count + 1


    print(count)