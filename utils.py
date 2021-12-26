from hexlib import *
from objects import *

def load_grid_file(file):
    grid = {}
    with open(file, "r") as f:
        for row, line in enumerate(f.readlines()):
            for col, char in enumerate(line):
                if char == ".":
                    hex = rdoubled_to_cube(DoubledCoord(col+2, row+1))
                    grid[hex] = default_hex_data

    return grid


def assign_position(char, hex, positions):
    try:
        positions.remove(hex)
    except:
        pass
    
    positions[hex] = char


