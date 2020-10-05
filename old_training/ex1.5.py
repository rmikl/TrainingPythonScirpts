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

    #BC = [int(triangleList[0]['c']['x']) - int(triangleList[0]['b']['x'])]
    for el in triangleList:
        d = {'x': int(el['c']['x']) - int(el['b']['x']) + int(el['a']['x']),
             'y': int(el['c']['y']) - int(el['b']['y']) + int(el['a']['y'])}
        if int(d['x']) == int(d['y']):
            print('\n3 vertices of the triangle:  ')
            print(el)
            print('point d: ')
            print(d)
            print("\n!!!!!!!!!!!!!!!!!!!!!!\nis also within function y=x\n!!!!!!!!!!!!!!!!!!!\n--------------\n")
        else:
            print('3 vertices of the triangle:  ')
            print(el)
            print('point d: ')
            print(d, '\n--------------------\n\n')

