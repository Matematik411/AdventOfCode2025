import sys
from utils.helpers import *

def parse_data(lines):
    good_ranges = []
    for i, line in enumerate(lines):
        if line == "":
            break
        parts = line.split("-")
        good_ranges.append((int(parts[0]), int(parts[1])))
    
    return good_ranges, lines[i+1:]


def parse_intervals_correctly(lines):
    good_ranges = []

    for i, line in enumerate(lines):
        if line == "":
            break
        parts = line.split("-")
        i1, i2 = int(parts[0]), int(parts[1])

        # find either overlapping or contained ranges
        i1_in = [r for r in good_ranges if r[0] <= i1 and r[1] >= i1]
        i2_in = [r for r in good_ranges if r[0] <= i2 and r[1] >= i2]
        inside_this_one = [r for r in good_ranges if r[0] >= i1 and r[1] <= i2]
    
        # remove all 3
        to_be_removed = inside_this_one + i1_in + i2_in

        lower = i1
        upper = i2

        if i1_in:
            lower = i1_in[0][0]
        if i2_in:
            upper = i2_in[0][1]

        good_ranges = [r for r in good_ranges if r not in to_be_removed]
        good_ranges.append((lower, upper))

    total_fresh = 0
    for r in good_ranges:
        total_fresh += r[1] - r[0] + 1

    
    return total_fresh

def sol1(data):
    ranges, to_check = parse_data(data)

    fresh = 0
    for i in to_check:
        num = int(i)
        for r in ranges:
            if r[0] <= num <= r[1]:
                fresh += 1
                break


    return fresh


def sol2(data):
    total = parse_intervals_correctly(data)

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
