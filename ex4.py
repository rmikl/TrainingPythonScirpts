import csv
import numpy as np


def lineequasion(point1, point2):
    if int(point1['x']) == int(point2['x']):
        return False
    elif int(point1['y']) == int(point2 ['y']):
        return 0
    arr1 = np.array([[int(point1['x']), 1], [int(point2['x']), 1]])
    arr2 = np.array([int(point1['y']), int(point2['y'])])
    x = np.linalg.solve(arr1, arr2)

    return x[0]


with open('wspolrzedneTR.txt') as file:
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
        AB = lineequasion(element['a'], element['b'])
        BC = lineequasion(element['b'], element['c'])
        AC = lineequasion(element['a'], element['c'])

        if AB * AC == -1 or AB * BC == -1 or BC * AC == -1:
            count = count + 1
        elif (AB == False and (BC == 0 or AC == 0)) or (BC == False and (AB == 0 or AC == 0)) or (AC == False and (BC == 0 or AB == 0)):
            count = count + 1
    print(count)


