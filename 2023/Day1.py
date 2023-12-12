import csv

file = '2023/Advent of Code Day 1 - Sheet1.csv'

with open(file) as file:
    reader = csv.reader(file)
    codeValue = []
    totalValue = 0

    for row in reader:
        calibrationValue = row[0]
        for element in calibrationValue:
            try:
                if (len(codeValue) < 2):
                    codeValue.append(int(element))
                else:
                    codeValue[1] = int(element)
            except ValueError:
                pass
        try:
            finalCodeValue = (codeValue[0] * 10) + codeValue[1]
        except IndexError:
            finalCodeValue = (codeValue[0] * 10) + codeValue[0]
        totalValue += finalCodeValue
        codeValue = []
    print(totalValue)