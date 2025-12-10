import sys
from utils.helpers import *
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def solve1(lights, buttons):

    # brute force, check each subset, press it once
    m = len(buttons)
    best = m * 2
    for mask in range(1 << m):
        state = lights[:]
        presses = 0
        for i in range(m):
            if (mask >> i) & 1:
                presses += 1
                for pos in buttons[i]:
                    state[pos] = 1 - state[pos]

        if sum(state) == 0:
            best = min(best, presses)
        
    return best

def update_state(state, button):
    new_state = list(state)
    for pos in button:
        new_state[pos] = 1 - new_state[pos]
    return tuple(new_state)


def solve2(buttons, powers):

    n = len(powers)
    m = len(buttons)

    # build a system of equations A x = b
    A = np.zeros((n, m), dtype=int)
    for j in range(m):
        for pos in buttons[j]:
            A[pos][j] = 1
    b = np.array(powers)    
    constraints = LinearConstraint(A, b, b)

    # minimize total presses
    bounds = Bounds(0, np.inf)
    c = np.array([1 for _ in range(m)])                   
    integrality = np.ones(m)
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    return round(result.fun) # this is the sum of the resulting vector x

def sol(data):
    
    total_presses_1 = 0
    total_presses_2 = 0

    for machine in data:
        vals = machine.split()
        lights = vals[0]
        buttons = vals[1:-1]
        powers = vals[-1]


        lights = [0 if c == '.' else 1 for c in lights[1:-1]]
        buttons = [[int(x) for x in b[1:-1].split(',')] for b in buttons]
        powers = [int(x) for x in powers[1:-1].split(',')]

        res1 = solve1(lights, buttons)
        res2 = solve2(buttons, powers)
        total_presses_1 += res1
        total_presses_2 += res2
       
    return total_presses_1, total_presses_2



if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()


    # part1 and part2
    s1, s2 = sol(file)

    print(f"Part one: {s1}")
    print(f"Part two: {s2}")
