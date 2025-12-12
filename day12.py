import sys
from utils.helpers import *


def try_present(current_reg, present_forms, w, h):
    possible_positions = []

    # i only take the first possible position for each form !

    for form in present_forms:   
        form_placed = False 
        for r in range(w - 2):
            if form_placed:
                break
            for c in range(h - 2):
                if form_placed:
                    break
                
                can_place = True
                new_cells = set()

                for pos in form:
                    rr = r + pos[0]
                    cc = c + pos[1]

                    if (rr, cc) in current_reg:
                        can_place = False
                        break
                    new_cells.add((rr, cc))

                if can_place:
                    c_reg_cpy = current_reg.copy() # only copy if we can place it
                    for cell in new_cells:
                        c_reg_cpy.add(cell)
                    possible_positions.append(c_reg_cpy)
                    form_placed = True

    return possible_positions



def fill_region(region, all_forms):
    w, h = region[0]
    vals = region[1]

    # by looking at input, some are directly too small !
    total_cells_needed = sum(vals[j] * len(all_forms[j][0]) for j in range(len(vals)))
    empty_cells = w * h
    if total_cells_needed > empty_cells:
        return False

    filled = set() # filled coordinates

    def to_put(n_ps, current_reg):

        if sum(n_ps) == 0:
            nice_print_grid_coords(current_reg, w, h)
            return True

        for i, v in enumerate(n_ps):
            if v > 0:
                possible_positions = try_present(current_reg, all_forms[i], w, h)
                numbers_cpy = [n_ps[j] if j != i else n_ps[j]-1 for j in range(len(n_ps))]
                for pos in possible_positions:
                    if to_put(numbers_cpy, pos):
                        return True
                
                if possible_positions == []:
                    return False

        return False
    

    return to_put(vals, filled)




def sol1(regions, all_forms):

    total_filled = 0

    for r in regions:
        if fill_region(r, all_forms):
            total_filled += 1        
        print("-------- region done -------", total_filled)



    return total_filled


def nice_print(shape):
    for row in shape:
        print(row)
    print()

def nice_print_grid_coords(grid_coords, w, h):
    grid = []
    for r in range(w):
        row = ""
        for c in range(h):
            if (r,c) in grid_coords:
                row += "#"
            else:
                row += "."
        grid.append(row)

    nice_print(grid)

def nice_print_coords(coords):

    grid = []
    for r in range(3):
        row = ""
        for c in range(3):
            if (r,c) in coords:
                row += "#"
            else:
                row += "."
        grid.append(row)

    nice_print(grid)

def rotate_shape(shape):
    rows = len(shape)
    cols = len(shape[0])

    new_shape = []
    for c in range(cols):
        new_row = ""
        for r in range(rows-1, -1, -1):
            new_row += shape[r][c]
        new_shape.append(new_row)

    return new_shape

def flip_shape(shape):
    rows = len(shape)
    cols = len(shape[0])

    new_shape = []
    for r in range(rows):
        new_row = ""
        for c in range(cols-1, -1, -1):
            new_row += shape[r][c]
        new_shape.append(new_row)

    return new_shape

def get_all_forms(shape):
    forms = []

    shape0 = shape
    forms.append(shape0)
    for _ in range(3):
        shape1 = rotate_shape(shape0)
        forms.append(shape1)
        shape0 = shape1


    shape0 = flip_shape(shape)
    forms.append(shape0)
    for _ in range(3):
        shape1 = rotate_shape(shape0)
        forms.append(shape1)
        shape0 = shape1


    unique_forms = set()
    for f in forms:
        nonzero = []
        for i in range(len(f)):
            for j in range(len(f[0])):
                if f[i][j] == "#":
                    nonzero.append((i,j))
        nonzero = tuple(nonzero)

        unique_forms.add(nonzero)

    return unique_forms



if __name__ == "__main__":
    file = sys.stdin.read().split("\n")
    if file[-1] == "":
        file.pop()

    shapes = []
    k = -1 
    for line in file:
        k += 1
        if ":" in line:
            i = int(line[0])
            shape = []
            continue
        
        if line == "":
            shapes.append(shape)
            if i == 5:
                break
            continue
    
        shape.append(line)

    spaces = []
    for line in file[k+1:]:
        dims, vals = line.split(":")
        dims = tuple(map(int, dims.split("x")))
        vals = list(map(int, vals.strip().split()))

        spaces.append((dims, vals))

    all_forms = {}
    for i in range(len(shapes)):
        all_forms[i] = list(get_all_forms(shapes[i]))


    # part1
    s1 = sol1(spaces, all_forms)

    print(f"Part one: {s1}")
    print(f"Part two: We are done!!!")
