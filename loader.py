from hexlib import *

# Hex grid with collumns doubled
# _grid = [
#     DoubledCoord(1, 4),
#     DoubledCoord(2, 4),
#     DoubledCoord(3, 4),
#     DoubledCoord(4, 4),
#     DoubledCoord(5, 4),
#     DoubledCoord(6, 4),
# ]

def load_grid_file(file):
    grid = []
    with open(file, "r") as f:
        for row, line in enumerate(f.readlines()):
            for col, char in enumerate(line):
                if char != " ":
                    grid.append(DoubledCoord(col+2, row+1))

    return grid

file = "chapter1.txt"
_grid = load_grid_file(file)

# grid now in cube coordinates
grid = [rdoubled_to_cube(hex) for hex in _grid]

# def optimize_grid(_grid):
#     grid = []
#     for hex in _grid:
#         grid.append(polygon_corners(normal_layout, hex)
# 
#     return grid


