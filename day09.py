import sys
from utils.helpers import *


def sol1(data):

    max_val = 0

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            val = (abs(data[i][0] - data[j][0]) + 1)* (abs(data[i][1] - data[j][1]) + 1)
            if val > max_val:
                max_val = val

    return max_val


# on x axis it's always connected !!!




def is_it_valid(p1, p2, horizontal_lines):

    x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
    y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

    for y in range(y_min, y_max + 1):
        if y not in horizontal_lines:
            return False
        x0, x1 = horizontal_lines[y]
        if x0 > x_min or x1 < x_max:
            return False

    return True







def sol2(data):

    allowed_by_y = {}
    
    for i in range(len(data)):
        p1 = data[i]
        p2 = data[(i + 1) % len(data)]
        
        x1, y1 = p1
        x2, y2 = p2
        
        # vertical
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1): 
                if y not in allowed_by_y: 
                    allowed_by_y[y] = [x1, x1] 
                else: 
                    allowed_by_y[y][0] = min(allowed_by_y[y][0], x1)
                    allowed_by_y[y][1] = max(allowed_by_y[y][1], x1)
        
        # horizontal
        elif y1 == y2:
            if y1 not in allowed_by_y: 
                allowed_by_y[y1] = [min(x1, x2), max(x1, x2)]
            else: 
                allowed_by_y[y1][0] = min(allowed_by_y[y1][0], x1, x2)
                allowed_by_y[y1][1] = max(allowed_by_y[y1][1], x1, x2)


    # check each pair
    max_val = 0

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if is_it_valid(data[i], data[j], allowed_by_y):
                
                val = (abs(data[i][0] - data[j][0]) + 1)* (abs(data[i][1] - data[j][1]) + 1)
                max_val = max(max_val, val)

    return max_val



# --------------------------
# this doesn't work 
def turn_left(direction):
    dirs = ["up", "left", "down", "right"]

    return dirs[(dirs.index(direction) + 1) % 4]

def turn_right(direction):
    dirs = ["up", "right", "down", "left"]

    return dirs[(dirs.index(direction) + 1) % 4]


def sol2_with_edges(data):

    edges = []
    # first is vertical, try for inside to be on the right
    inside = "right"
    inside = "down"
    inside = "left"
    for i in range(len(data)):
        if i == len(data) - 1:
            j = 0
            k = 1
        elif i == len(data) - 2:
            j = i + 1
            k = 0
        else:
            j = i + 1
            k = j + 1


    
        if data[i][0] == data[j][0]:
            edges.append( (inside, data[i][0], min(data[i][1], data[j][1]), max(data[i][1], data[j][1])))

            #moving down
            if data[i][1] < data[j][1]:
                if data[k][0] < data[i][0]:
                    inside = turn_right(inside)
                else:
                    inside = turn_left(inside)

            else: # moving up   
                if data[k][0] < data[i][0]:
                    inside = turn_left(inside)
                else:
                    inside = turn_right(inside) 

        else: # horizontal edge
            edges.append( (inside, data[i][1], min(data[i][0], data[j][0]), max(data[i][0], data[j][0])))

            # moving right
            if data[i][0] < data[j][0]:
                if data[k][1] > data[i][1]:
                    inside = turn_right(inside)
                else:
                    inside = turn_left(inside)

            else: # moving left
                if data[k][1] > data[i][1]:
                    inside =  turn_left(inside)
                else:
                    inside = turn_right(inside)
    

    # print([e[0] for e in edges])
    # return

    
    
    max_val = 0

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            val = (abs(data[i][0] - data[j][0]) + 1)* (abs(data[i][1] - data[j][1]) + 1)

            x_min, x_max = min(data[i][0], data[j][0]), max(data[i][0], data[j][0])
            y_min, y_max = min(data[i][1], data[j][1]), max(data[i][1], data[j][1])

            if min(x_max - x_min, y_max - y_min) <= 1:
                if val > max_val:
                    # print(f"STRAIGHT LINE: New max area {val} between points {data[i]} and {data[j]}")
                    max_val = val
                continue


            for e in edges:

                if e[0] in ["left", "right"]: # vertical edge
                    if max(y_min, e[2]+1) <= min(y_max, e[3]-1):
                        if e[0] == "left" and e[1] < x_max:
                            val = 0
                            # print("fails left for points", data[i], data[j], "with edge", e)
                        
                            break
                        elif e[0] == "right" and e[1] > x_min:
                            val = 0
                            # print("fails right for points", data[i], data[j], "with edge", e)
                            break
                else: # horizontal edge
                    if max(x_min, e[2]+1) <= min(x_max, e[3]-1):
                        if e[0] == "down" and e[1] > y_min:
                            # print("fails down for points", data[i], data[j], "with edge", e)
                            val = 0
                            break
                        elif e[0] == "up" and e[1] < y_max:
                            # print("fails up for points", data[i], data[j], "with edge", e)
                            val = 0
                            break

            # if val > 0:
            #     print(f"Valid area {val} between points {data[i]} and {data[j]}")

            if val > max_val:
                # print(f"New max area {val} between points {data[i]} and {data[j]}")
                max_val = val


    return max_val
# ---------------------------



if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    pairs = [tuple(map(int, line.split(","))) for line in file]

    # print(file)

    # part1
    s1 = sol1(pairs)

    # part2
    s2 = sol2(pairs)
    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
