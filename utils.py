from hexlib import *
from objects import *

def load_grid_file(file):
    grid = {}
    with open(file, "r") as f:
        for row, line in enumerate(f.readlines()):
            for col, char in enumerate(line):
                if char == ".":
                    grid[rdoubled_to_cube(DoubledCoord(col+2, row+1))] = default_hex_data

    return grid


def assign_position(char, hex, positions):
    try:
        positions.remove(char.position)
    except:
        pass
    
    char.position = hex
    positions.append(hex)



def test():
    file = "chapter1.txt"
    grid = load_grid_file(file)
    for hex in grid:
        print(grid[hex].block_direction)

# test()
