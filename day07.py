import sys
from utils.helpers import *
from functools import lru_cache


def after_line(beams, splitters):
    after = set()
    splits = 0
    for b in beams:
        if b in splitters:
            after.add(b + 1)
            after.add(b - 1)
            splits += 1
        else:
            after.add(b)

    return after, splits

def sol1(file):
    
    beams = {file[0].index("S")}
    total = 0

    for line in file:
        if "^" in line:
            splitters = [i for i, c in enumerate(line) if c == "^"]
            beams, splits = after_line(beams, splitters)
            total += splits

    return total


def sol2(file):

    # memo function in here so it has access to `file`
    @lru_cache(None)
    def count_ways(line_idx, beam_pos):
        if line_idx >= len(file):
            return 1

        line = file[line_idx]
        total_ways = 0

        if line[beam_pos] == "^":
            total_ways += count_ways(line_idx + 1, beam_pos - 1)
            total_ways += count_ways(line_idx + 1, beam_pos + 1)
        else:
            total_ways += count_ways(line_idx + 1, beam_pos)

        return total_ways

    return count_ways(0, file[0].index("S"))


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
