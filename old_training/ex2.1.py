import csv

with open('okregi.txt') as file:
    reader = csv.reader(file, delimiter=' ', skipinitialspace=True)

    circleList = []

    for row in reader:
        circle = {'x': float(row[0]), 'y': float(row[1]), 'r': float(row[2])}

        circleList.append(circle)

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0

    for el in circleList:
        if abs(el['r']) >= abs(el['x']) or abs(el['r']) >= abs(el['y']):
            count5 = count5 + 1
        elif el['x'] > 0 and el['y'] > 0:
            count1 = count1 + 1
        elif el['x'] > 0 and el['y'] < 0:
            count2 = count2 + 1
        elif el['x'] < 0 and el['y'] > 0:
            count3 = count3 + 1
        elif el['x'] < 0 and el['y'] < 0:
            count4 = count4 + 1

    print('circle within more than one quarter :', count5)
    print('first quarter :', count1)
    print('second quarter :', count2)
    print('third quarter :', count3)
    print('fourth quarter :', count4)



