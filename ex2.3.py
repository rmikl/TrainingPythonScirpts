import csv

with open('okregi.txt') as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True)

    circleList = []

    for row in reader:
        circle = {'x': float(row[0]), 'y': float(row[1]), 'r': float(row[2])}
        circleList.append(circle)

    abstractCircleList = []

    for el in circleList:
        newEl = [el['x'], el['y'], el['r']]
        abstractCircleList.append(newEl)
    count = 0


    abstractCircleList_set = set(tuple(e) for e in abstractCircleList)
    abstractCircleList = [list(x) for x in abstractCircleList_set]

    for el in abstractCircleList:
        if el == "null":
            continue
        el1 = [el[1], el[0] * -1, el[2]]
        el2 = [el[1] * -1, el[0], el[2]]
        el3 = [el[0] * -1, el[1] * -1, el[2]]

        if el2 in abstractCircleList and el1 in abstractCircleList and el3 in abstractCircleList:
            count = count + 4
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el1)] = "null"
            abstractCircleList[abstractCircleList.index(el2)] = "null"
            abstractCircleList[abstractCircleList.index(el3)] = "null"
        elif el2 in abstractCircleList and el1 in abstractCircleList:
            count = count + 2
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el2)] = "null"
            abstractCircleList[abstractCircleList.index(el1)] = "null"
        elif el2 in abstractCircleList and el3 in abstractCircleList:
            count = count + 2
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el2)] = "null"
            abstractCircleList[abstractCircleList.index(el3)] = "null"
        elif el3 in abstractCircleList and el1 in abstractCircleList:
            count = count + 2
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el1)] = "null"
            abstractCircleList[abstractCircleList.index(el3)] = "null"
        elif el2 in abstractCircleList:
            count = count + 1
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el2)] = "null"
        elif el1 in abstractCircleList:
            count = count + 1
            abstractCircleList[abstractCircleList.index(el)] = "null"
            abstractCircleList[abstractCircleList.index(el1)] = "null"

    print(count)
