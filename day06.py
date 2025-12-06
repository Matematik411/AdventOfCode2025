import sys
from utils.helpers import *



def sol1(data):

    columns = []
    last_row = False
    for line in data:
        parts = line.split()
        if columns == []:
            columns = [[] for _ in range(len(parts))]
        elif len(columns[0]) == len(data) - 1:
            last_row = True
        
        for i, p in enumerate(parts):
            if last_row:
                columns[i].append(p)
            else:       
                columns[i].append(int(p))

    total = 0

    for c in columns:
        operation = c.pop()

        if operation == "+":
            total += sum(c)
        elif operation == "*":
            prod = 1
            for x in c:
                prod *= x
            total += prod

    return total


def sol2(data):

    columns = []
    last_row = data[-1] 

    i = 0
    numbers = []
    operation = None
    while i < len(last_row): 
        # moving from left to right as it doesn't matter

        number = "" # build number for the column
        for c in range(len(data[:-1])):
            if data[c][i] != " ":
                number += data[c][i]

        if number != "":
            numbers.append(int(number))
        else:
            columns.append([numbers, operation]) # number is null exactly on the column before the operation
            numbers = []
        
    
        if last_row[i] != " ":
            operation = last_row[i]

        i += 1

    # add last column
    columns.append([numbers, operation])



    total = 0
    for i in range(len(columns)):
        column, operation = columns[i]


        if operation == "+":
            total += sum(column)
        elif operation == "*":
            prod = 1
            for x in column:
                prod *= x
            total += prod


    return total



if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol1(file)

    # part2
    s2 = sol2(file)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
