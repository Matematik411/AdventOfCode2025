import sys
from utils.helpers import *


def sol1(data):
    d = 50
    pass_count = 0

    for line in data:
        change = line[0]
        n = int(line[1:])

        if change == "R":
            d = (d + n) % 100
        else:
            d = (d - n) % 100
        
        if d == 0:
            pass_count += 1

    return pass_count


def sol2(data):
    d = 50
    pass_count = 0

    for line in data:
        change = line[0]
        n = int(line[1:])

        if change == "R":
            nov_d = (d + n) % 100

            pass_count += n // 100
            if d != 0 and nov_d < d: # ce prej na nicli, ne smes stet se enkrat
                pass_count += 1
        else:
            nov_d = (d - n) % 100

            pass_count += n // 100
            if d != 0 and (nov_d > d or nov_d == 0): # ce prej na nicli, ne smes stet se enkrat
                pass_count += 1
        
        d = nov_d

    return pass_count


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
