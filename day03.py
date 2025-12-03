import sys
from utils.helpers import *
 
def build1(with_indices, d, length):
    if length == 0:
        return ""
    
    for (x, i) in with_indices:
        if i < d-(length-1):

            remaining = []
            for (y, k) in with_indices:
                if k > i:
                    remaining.append((y, k))


            return x + build1(remaining, d, length-1)

def sol(data, lights):
    total = 0

    for line in data:
        with_indices = [(line[i], i) for i in range(len(line))]
        with_indices.sort(key=lambda x: (x[0], -x[1]), reverse=True)

        number = build1(with_indices, len(line), lights)
        total += int(number)

    return total


if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol(file, 2)

    # part2
    s2 = sol(file, 12)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
