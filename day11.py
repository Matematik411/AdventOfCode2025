import sys
from utils.helpers import *
from functools import lru_cache


def sol1(data):

    graph = {}

    for line in data:
        node, edges = line.split(":")

        edges = edges.strip().split()

        graph[node] = edges


    @lru_cache(None)
    def dfs(node, visited):

        if node == "out":
            return 1

        visited = set(visited)
        visited.add(node)

        total_paths = 0

        for e in graph[node]:
            if e not in visited:
                total_paths += dfs(e, tuple(visited))

        return total_paths
    
    return dfs("you", tuple())


def sol2(data):

    graph = {}

    for line in data:
        node, edges = line.split(":")

        edges = edges.strip().split()

        graph[node] = edges


    # this works, as there are no loops that can be formed while visiting dac and fft
    @lru_cache(None)
    def check(node, dac, fft):

        if node == "out":
            if dac and fft:
                return 1
            else:
                return 0

        if node == "dac":
            dac = True
        if node == "fft":
            fft = True

        total_paths = 0

        for e in graph[node]:
            total_paths += check(e, dac, fft)

        return total_paths
    
    return check("svr", False, False)


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
