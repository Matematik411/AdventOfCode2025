import sys
from utils.helpers import *


def sol(data, max_split):
    ranges = data.split(",")
    invalids = 0

    for r in ranges:
        bounds = r.split("-")
        lower = bounds[0]
        upper = bounds[1]

        for k in range(int(lower), int(upper)+1):
            s = str(k)
            d = len(s)

            delitve = d
            # part 2 doda max_split = 2
            if max_split:
                delitve = max_split

            for i in range(2, delitve + 1):
                if d % i == 0:
                    if s == s[:d // i] * i:
                        invalids += k
                        break

    return invalids

if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    # part1
    s1 = sol(file[0], 2)
    s2 = sol(file[0], None)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
