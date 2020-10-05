import csv
import numpy as np



with open('okregi.txt') as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True)

    circleList = []

    for row in reader:
        circle = {'x': float(row[0]), 'y': float(row[1]), 'r': float(row[2])}
        circleList.append(circle)

    abstractCircleList = []

    for el in circleList:
        newEl = [abs(el['x']), abs(el['y']), el['r']]
        abstractCircleList.append(newEl)


    count = 0
    for el in abstractCircleList:
        if el == "null":
            continue
        elif abstractCircleList.count(el) == 1:
            continue
        elif abstractCircleList.count(el) == 2:
            count = count + 1
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el)] = "null"
        elif abstractCircleList.count(el) == 3:
            count = count + 2
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el)] = "null"
        elif abstractCircleList.count(el) == 4:
            count = count + 4
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el)] = "null"

    print(count)

