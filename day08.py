import sys
import math
from utils.helpers import *

from unionfind import unionfind


def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)




def sol(points_dict, distances):

    uf = unionfind(len(points_dict))

    connections_made = 0
    i = 0
    while True:
        edge = distances[i]

        if uf.issame(edge[1], edge[2]):
            i += 1
            continue
    
        
        
        uf.unite(edge[1], edge[2])
        connections_made += 1
        i += 1

        if i == 1000: # 10 for test case
            sorted_now = sorted([len(group) for group in uf.groups()], reverse=True)
            sol1 = sorted_now[0] * sorted_now[1] * sorted_now[2]
        
        if connections_made == len(points_dict) - 1: # don't want to always call uf.groups() 
            sol2 = points_dict[edge[1]][0] * points_dict[edge[2]][0]
            break

    return sol1, sol2



if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    data = [tuple(map(int, line.split(","))) for line in file]
    data_dict = {i: tuple(map(int, line.split(","))) for i, line in enumerate(file)}

    all_distances = []

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            all_distances.append( (dist(data[i], data[j]), i, j) )
    all_distances.sort()



    # both parts
    s1, s2 = sol(data_dict, all_distances)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
