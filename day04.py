import sys
from utils.helpers import *



def can_be_removed(data):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    accessible = []
    for j in range(len(data)):
        row = data[j]
        for i in range(len(row)):
            if row[i] == '@':

                neighbors = 0
                for d in dirs:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if 0 <= new_i < len(row) and 0 <= new_j < len(data):
                        if data[new_j][new_i] == '@':
                            neighbors += 1

            
                if neighbors < 4:
                    accessible.append((j, i))

    return accessible


def sol(data, part):

    total = 0
    while True:

        removable = can_be_removed(data)
        total += len(removable)

        if part == 1:
            break

        print(f"Removed {len(removable)} items")

        if len(removable) == 0:
            break

        new_grid = []
        for j in range(len(data)):
            new_row = ""
            for i in range(len(data[j])):
                if (j, i) in removable:
                    new_row += "."
                else:
                    new_row += data[j][i]
            new_grid.append(new_row)

        data = new_grid

    return total


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol(file, 1)

    # part2
    s2 = sol(file, 2)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
